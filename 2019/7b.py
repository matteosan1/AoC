import itertools
from multiprocessing import Process, Queue
from threading import Thread

with open("input7a.txt") as f:
    code = f.readline()

#code = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
#code = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"

class Computer:
    def __init__(self, name, code, q_in, q_out=None):
        self.name = name
        self.code = code
        self.q_in = q_in
        self.q_out = q_out
        self.outputs = []

    def run (self):
        intcode = list(map(int, self.code.split(",")))
        index = 0
        while index < len(intcode):
            optcode = intcode[index] % 100
            modes = [int(d) for d in str(intcode[index] // 100)[::-1]]
            if len(modes) == 1:
                modes.append(0)
            val = []
            if optcode == 99:
                print ("{} ended". format(self.name))
                print (self.outputs)
                break
            elif optcode == 1:
                for im in range(2):
                    if modes[im] == 0:
                        val.append(intcode[intcode[index + 1 + im]])
                    else:
                        val.append(intcode[index + 1 + im])
                intcode[intcode[index + 3]] = val[0] + val[1]
                index += 4
            elif optcode == 2:
                for im in range(2):
                    if modes[im] == 0:
                        val.append(intcode[intcode[index + 1 + im]])
                    else:
                        val.append(intcode[index + 1 + im])
                intcode[intcode[index + 3]] = val[0] * val[1]
                index += 4
            elif optcode == 3:
                print ("{} is waiting...".format(self.name))
                v = self.q_in.get()
                print ("{} is going to use input:{}".format(self.name, v))
                intcode[intcode[index + 1]] = v
                #if inputs is []:
                #    intcode[intcode[index + 1]] = int(input('Input: '))
                #else:
                #    #print ("going to use input {}:{}".format(input_counter, inputs[input_counter]))
                #    intcode[intcode[index + 1]] = inputs[input_counter]
                #    input_counter += 1
                index += 2
            elif optcode == 4:
                if modes[0] == 0:
                    val.append(intcode[intcode[index + 1]])
                else:
                    val.append(intcode[index + 1])
                print ("{} output {}".format(self.name, val[0]))
                self.outputs.append(val[0])
                if self.q_out is not None:
                    self.q_out.put(val[0])
                index += 2
            elif optcode == 5:
                for im in range(2):
                    if modes[im] == 0:
                        val.append(intcode[intcode[index + 1 + im]])
                    else:
                        val.append(intcode[index + 1 + im])
                if val[0] != 0:
                    index = val[1]
                else:
                    index += 3
            elif optcode == 6:
                for im in range(2):
                    if modes[im] == 0:
                        val.append(intcode[intcode[index + 1 + im]])
                    else:
                        val.append(intcode[index + 1 + im])
                if val[0] == 0:
                    index = val[1]
                else:
                    index += 3
            elif optcode == 7:
                for im in range(2):
                    if modes[im] == 0:
                        val.append(intcode[intcode[index + 1 + im]])
                    else:
                        val.append(intcode[index + 1 + im])
                if val[0] < val[1]:
                    intcode[intcode[index + 3]] = 1
                else:
                    intcode[intcode[index + 3]] = 0
                index += 4
            elif optcode == 8:
                for im in range(2):
                    if modes[im] == 0:
                        val.append(intcode[intcode[index + 1 + im]])
                    else:
                        val.append(intcode[index + 1 + im])
                if val[0] == val[1]:
                    intcode[intcode[index + 3]] = 1
                else:
                    intcode[intcode[index + 3]] = 0
                index += 4

phases = [9, 8, 7, 6, 5]
max_out = 0
seq = 0
names = ["A", "B", "C", "D", "E"]

for p in itertools.permutations(phases, len(phases)):
    processes = []
    computers = []
    q_in = [Queue() for _ in range(5)]

    for i in range(5):
        if i != 4:
            computers.append(Computer(names[i], code, q_in[i], q_in[i + 1]))
            processes.append(Thread(target=computers[-1].run, args=[]))
        else:
            computers.append(Computer(names[i], code, q_in[i], q_in[0]))
            #computers.append(Computer(names[i], code, q_in[i]))
            processes.append(Thread(target=computers[-1].run, args=[]))

    for iq, q in enumerate(q_in):
        q.put(p[iq])
    q_in[0].put(0)

    for i in range(5):
        processes[i].start()
    for i in range(5):
        processes[i].join()

    out = computers[-1].outputs[-1]
    if out > max_out:
        max_out = out
        seq = p

print (max_out, seq)

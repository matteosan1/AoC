from multiprocessing import Queue
from threading import Thread

DEBUG = False

with open("input9a.txt") as f:
    code = f.readline()

#code = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
#code = "1102,34915192,34915192,7,4,7,99,0"
#code = "104,1125899906842624,99"

class Computer:
    def __init__(self, name, code, q_in, q_out=None):
        self.name = name
        self.code = code
        self.q_in = q_in
        self.q_out = q_out
        self.outputs = []
        self.index = 0
        self.offset = 0
        self.intcode = []

    def interpretedmode(self, im, modes):
        if modes[im] == 0:
            reg = self.intcode[self.index + 1 + im]
        elif modes[im] == 1:
            reg = self.index + 1 + im
        elif modes[im] == 2:
            reg = self.intcode[self.index + 1 + im] + self.offset

        if reg > len(self.intcode):
            self.intcode.extend([0] * (reg + 1 - len(self.intcode)))
        val = self.intcode[reg]

        return val

    def literalmode(self, im, modes):
        if modes[im] != 2:
            reg = self.index + 1 + im
            val = self.intcode[reg]
        else:
            reg = self.index + 1 + im
            val = self.intcode[reg] + self.offset

        return val

    def run (self):
        self.intcode = list(map(int, self.code.split(",")))
        while self.index < len(self.intcode):
            optcode = self.intcode[self.index] % 100
            modes = [int(d) for d in str(self.intcode[self.index] // 100)[::-1]]
            if len(modes) < 3:
                modes += [0] * (3 - len(modes))
            val = []
            try:
                if optcode == 99:
                    if DEBUG:
                        print ("{} ended". format(self.name))
                    break
                elif optcode == 1:
                    if DEBUG:
                        print(self.intcode[self.index:self.index + 4], modes)
                    for im in range(2):
                        val.append(self.interpretedmode(im, modes))
                    reg = self.literalmode(2, modes)
                    self.intcode[reg] = val[0] + val[1]
                    if DEBUG:
                        print ("SUM {} {} into {}".format(val[0], val[1], reg))
                    self.index += 4
                elif optcode == 2:
                    if DEBUG:
                        print(self.intcode[self.index:self.index + 4], modes)

                    for im in range(2):
                        val.append(self.interpretedmode(im, modes))
                    reg = self.literalmode(2, modes)
                    self.intcode[reg] = val[0] * val[1]
                    if DEBUG:
                        print ("MUL {} {} into {}".format(val[0], val[1], reg))
                    self.index += 4
                elif optcode == 3:
                    if DEBUG:
                        #print(self.intcode[self.index:self.index + 2], modes)
                        print ("{} is waiting...".format(self.name))
                    v = self.q_in.get()
                    reg = self.literalmode(0, modes)
                    if DEBUG:
                        print ("{} is going to set value {} into {}".format(self.name, v, reg))
                    self.intcode[reg] = v
                    #if inputs is []:
                    #    intcode[intcode[index + 1]] = int(input('Input: '))
                    #else:
                    #    #print ("going to use input {}:{}".format(input_counter, inputs[input_counter]))
                    #    intcode[intcode[index + 1]] = inputs[input_counter]
                    #    input_counter += 1
                    self.index += 2
                elif optcode == 4:
                    val.append(self.interpretedmode(0, modes))
                    if DEBUG:
                        #print(self.intcode[self.index:self.index + 2], modes)
                        print ("{} output {}".format(self.name, val[0]))
                    self.outputs.append(val[0])
                    if self.q_out is not None:
                        self.q_out.put(val[0])
                    self.index += 2
                elif optcode == 5:
                    for im in range(2):
                        val.append(self.interpretedmode(im, modes))
                    if val[0] != 0:
                        self.index = val[1]
                    else:
                        self.index += 3
                    if DEBUG:
                        print("if [{}] {} != 0 goto {} else goto {}".format(val[0], val[1], self.index + 3))
                elif optcode == 6:
                    for im in range(2):
                        val.append(self.interpretedmode(im, modes))
                    if DEBUG:
                        #print(self.intcode[self.index:self.index + 3], modes)
                        print("if {} == 0 goto {} else goto {}".format(val[0], val[1], self.index + 3))
                    if val[0] == 0:
                        self.index = val[1]
                    else:
                        self.index += 3
                elif optcode == 7:
                    for im in range(2):
                        val.append(self.interpretedmode(im, modes))
                    reg = self.literalmode(2, modes)
                    if val[0] < val[1]:
                        self.intcode[reg] = 1
                    else:
                        self.intcode[reg] = 0
                    if DEBUG:
                        #print(self.intcode[self.index:self.index + 4], modes)
                        print ("if {} < {} reg {}  = 1 else = 0 ".format(val[0], val[1], reg))
                    self.index += 4
                elif optcode == 8:
                    for im in range(2):
                        val.append(self.interpretedmode(im, modes))
                    reg = self.literalmode(2, modes)
                    if val[0] == val[1]:
                        self.intcode[reg] = 1
                    else:
                        self.intcode[reg] = 0
                    if DEBUG:
                        #print(self.intcode[self.index:self.index + 4], modes)
                        print ("if {} == {} reg {}  = 1 else = 0 ".format(val[0], val[1], reg))
                    self.index += 4
                elif optcode == 9:
                    val.append(self.interpretedmode(0, modes))
                    if DEBUG:
                        #print(self.intcode[self.index:self.index + 2], modes)
                        print ("offset changed from {} of {}".format(self.offset, val[0]))
                    self.offset += val[0]
                    self.index += 2
            except IndexError:
                if reg > self.index:
                    self.intcode.extend([0] * (reg + 1 - len(self.intcode)))
                else:
                    self.intcode.extend([0] * (self.index + 1 - len(self.intcode)))
            finally:
                pass

q_in = [Queue() for _ in range(2)]
c = Computer("A", code, q_in[0], None)

process = Thread(target=c.run, args=[])
q_in[0].put(2)

process.start()
process.join()

print (c.outputs)

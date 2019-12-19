from multiprocessing import Queue
from threading import Thread

DEBUG = False

filename = "input19a.txt"
with open(filename, "r") as f:
    code = f.readline()

class Computer:
    def __init__(self, name, code, q_in, q_out=None):
        self.name = name
        self.code = code
        self.q_in = q_in
        self.q_out = q_out
        self.inputs = []
        self.outputs = []
        self.index = 0
        self.offset = 0
        self.intcode = list(map(int, self.code.split(",")))

    def set_address(self, address, value):
        self.intcode[address] = value
        
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

    def run (self, manual_stopping=False):
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
                    if self.q_out is not None and not manual_stopping:
                        self.q_out.put("END")
                    if not manual_stopping:
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
                    #self.q_out.put("MOVE")
                    #if DEBUG:
                        #print(self.intcode[self.index:self.index + 2], modes)
                    #    print ("{} is waiting...".format(self.name))
                    #v = self.q_in.get(timeout=1)
                    #v = input()
                    v = self.inputs.pop(0)
                    #print ("INPUT", v)
                    reg = self.literalmode(0, modes)
                    if DEBUG:
                        print ("{} is going to set value {} into {}".format(self.name, v, reg))
                    if v == "QUIT" and manual_stopping:
                        break
                    self.intcode[reg] = int(v)
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
                        print("if [{}] {} not= 0 goto {} else goto {}".format(val[0], val[1], self.index + 3))
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

manual_stopping = False

q_in = Queue()
q_out = Queue()
beam_map = {}

points = 0
for y in range(50):
    for x in range(50):
        c = Computer("A", code, q_in)#, q_out)
        c.inputs.append(1000)
        c.inputs.append(x)
        c.inputs.append(y)
        #process = Thread(target=c.run, args=[manual_stopping])
        c.run(manual_stopping) #.start()
        if c.outputs[0] == 1:
            beam_map[(x, y)] = c.outputs[0]
            points += 1

ymin = min([x[1] for x in beam_map.keys() if x[0] == 49])
ymax = max([x[1] for x in beam_map.keys() if x[0] == 49])
print (ymin, ymax)

xmin = min([x[0] for x in beam_map.keys() if x[0] != 0])
print (xmin)
print (beam_map)
def line(x1, x2):
    m = (x2[1] - x1[1])/(x2[0] - x1[0])
    q = x1[1] - m*x1[0]
    return m,q

x1 = (4, 3)
x2 = (49, 36)
x3 = (49, 44)
m1, q1 = line(x1, x2)
m2, q2 = line(x1, x3)

for x in range(1500):
    y1 = m1*x + q1

    print (x, y1)

#for y in range(50):
#    for x in range(50):
#        if beam_map[(x, y)] == 1:
#            print ("#", end='')
#        else:
#            print (".", end='')
#    print ("")

#print (points)


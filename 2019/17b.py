from multiprocessing import Queue
from threading import Thread
import pickle

def findBot(image):
    for k, v in image.items():
        if v != "#" and v != ".":
            if v == "v":
                direction = 2
            elif v == "^":
                direction = 0
            elif v == "<":
                direction = 3
            elif v == ">":
                direction = 1                 
            return k, direction

DEBUG = False

with open("input17b.txt") as f:
    code = f.readline()

with open("map17.pk", "rb") as f:
    image = pickle.load(f)

class Computer:
    def __init__(self, name, code, q_in, q_out=None):
        self.name = name
        self.code = code
        self.q_in = q_in
        self.q_out = q_out
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

    def run (self):
        while self.index < len(self.intcode):
            optcode = self.intcode[self.index] % 100
            modes = [int(d) for d in str(self.intcode[self.index] // 100)[::-1]]
            if len(modes) < 3:
                modes += [0] * (3 - len(modes))
            val = []
            try:
                if optcode == 99:
                    if not DEBUG:
                        print ("{} ended". format(self.name))
                    if self.q_out is not None:
                        self.q_out.put("END")
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
                    self.q_out.put("MOVE")
                    if not DEBUG:
                        #print(self.intcode[self.index:self.index + 2], modes)
                        print ("{} is waiting...".format(self.name))
                    v = self.q_in.get()
                    #v = input()
                    print ("INPUT", v)
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
                    if not DEBUG:
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

class Robot:
    def __init__(self, current_position, direction, image):
        self.position = current_position
        self.visited = set()
        self.visited.add(current_position)
        self.direction = direction
        self.image = image

    def move(self, direction):
        if direction == "L":
            new_dir = self.direction - 1
            new_dir = new_dir % 4
        elif direction == "R":
            new_dir = self.direction + 1
            new_dir = new_dir % 4
        else:
            new_dir = self.direction

        if new_dir == 0:
            new_pos = (self.position[0], self.position[1] - 1)
        elif new_dir == 1:
            new_pos = (self.position[0] + 1, self.position[1])
        elif new_dir == 2:
            new_pos = (self.position[0], self.position[1] + 1)
        elif new_dir == 3:
            new_pos = (self.position[0] - 1, self.position[1])

        return new_pos, new_dir

    def tryAdvance(self):
        new_pos, new_dir = self.move("F")
        return new_pos in self.image

    def tryRotateLeft(self):
        new_pos, new_dir = self.move("L")
        return new_pos in self.image

    def tryRotateRight(self):
        new_pos, new_dir = self.move("R")
        return new_pos in self.image

    def traverse(self):
        steps = []
        counter = 0
        while len(self.visited) < len(self.image):
            if self.tryAdvance():
                self.position = self.move("F")[0]
                counter += 1
                self.visited.add(self.position)
                #drawDict[self.position] = str(counter%10)
            elif self.tryRotateLeft():
                if counter != 0:
                    steps.append(str(counter))
                steps.append("L")
                #drawDict[self.position] = str("L")
                counter = 0
                self.direction = self.move("L")[1]
            elif self.tryRotateRight():
                if counter != 0:
                    steps.append(str(counter))
                steps.append("R")
                #drawDict[self.position] = str("R")
                counter = 0
                self.direction = self.move("R")[1]
        steps.append(str(counter))
        #print(drawDictScreenSimple(drawDict))
        #print(steps)
        return steps

#process.start()
#new_image = []
#for k, v in image.items():
#    if v not= ".":
#        new_image.append(k)
#current_position, direction = findBot(image)
#r = Robot(current_position, direction, new_image)
#path = r.traverse()

def stepsToPattern(stepArray):
    stringSteps = ",".join(stepArray)
    for x in range(20):
        for y in range(20):
            for z in range(20):
                patterns, success = dumbMatcher(stringSteps, [x,y,z])
                if success:
                    letters = ["A", "B", "C"]
                    for x in range(len(letters)):
                        if patterns[x][0] == ",":
                            patterns[x] = patterns[x][1:]
                        stringSteps = stringSteps.replace(patterns[x],letters[x])
                    result = [stringSteps]
                    result.extend(patterns)
                    return result

def dumbMatcher(stringSteps, sizes):
    patterns = []
    for x in range(len(sizes)):
        p = stringSteps[0:sizes[x]]
        patterns.append(p)
        stringSteps = stringSteps.replace(p, "")
    stringSteps = stringSteps.replace(",", "")
    return patterns, stringSteps==""


#patterns = stepsToPattern(path)
patterns = ['ABABAC,BC,AC', 'L,10,L,12,R,6', 'R,10,L,4,L,4,L,12', 'L,10,R,10,R,6,L,4']
patterns.append("n")

# c = (20, 24)
# patterns = ['A','B','A','B','A','C','B','C','A','C']
# vals = {"A":['L','10','L','12','R','6'], "B":['R','10','L','4','L','4','L','12'], "C":['L','10','R','10','R','6','L','4']}
#
# dir = 0
#
# def turn(dir, d):
#     if d == "L":
#         dir -= 1
#     elif d == "R":
#         dir += 1
#     dir = dir % 4
#     return dir
#
# def move(c, dir):
#     if dir == 0:
#         c = (c[0], c[1] - 1)
#     elif dir == 1:
#         c = (c[0]+1, c[1])
#     elif dir == 2:
#         c = (c[0], c[1] + 1)
#     elif dir == 3:
#         c = (c[0]-1, c[1])
#     return c
#
# xmax = max(list(image.keys()), key=lambda x: x[0])[0]
# ymax = max(list(image.keys()), key=lambda x: x[1])[1]
#
# for p in patterns:
#     for char in vals[p]:
#         if char == "L" or char == "R":
#             dir = turn(dir, char)
#         else:
#             for i in range(int(char)):
#                 c = move(c, dir)
#                 image[c] = "X"
#
# for y in range(ymax):
#     for x in range(xmax):
#         print(image[(x, y)], end='')
#     print("")
#
# import sys
# sys.exit()

q_in = Queue()
q_out = Queue()
c = Computer("A", code, q_in, q_out)
process = Thread(target=c.run, args=[])
process.start()

ninput = 0
char = 0
#for n in range(len(patterns)):
#    for p in patterns:
#        for c in p:
#            q_in.put(ord(c))
#        q_in.put(10)

while True:
    question = q_out.get()
    if question == "MOVE":
        if ninput == 0:
            for c in patterns[0]:
                q_in.put(ord(c))
            q_in.put(10)
            ninput += 1
        else:
            for i in range(1, 5):
                for c in patterns[i]:
                    q_in.put(ord(c))
                q_in.put(10)
            ninput += 1
        # if char == len(patterns[ninput]):
        #     q_in.put(10)
        #     char = 0
        #     ninput += 1
        # else:
        #     print(ord(patterns[ninput][char]))
        #     q_in.put(ord(patterns[ninput][char]))
        #     char += 1

    if question == "END":
       break
process.join()
    #    for c in patterns[i]:
    #        q_in.put(ord(c))
    #    q_in.put(10)



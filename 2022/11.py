from utils import readInput, printArray, bcolors
import numpy as np

class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashed = False
        
    def gain(self):
        self.energy += 1

    def reset(self):
        if self.energy > 9:
            self.energy = 0
            if not self.flashed:
                print ("Problema")
            self.flashed = False
        
    def flash(self):
        self.flashed = True

class Map:
    def __init__(self, filename):
        lines = readInput(filename)
        self.m = {}
        self.xlim = len(lines[0])
        self.ylim = len(lines)
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                self.m[x, y] = Octopus(int(lines[y][x]))
        self.flashes = 0

    def step(self):
        for y in range(self.ylim):
            for x in range(self.xlim):
                self.m[x, y].gain()

        for y in range(self.ylim):
            for x in range(self.xlim):
                if self.m[x, y].energy > 9 and not self.m[x, y].flashed:
                    self.m[x, y].flash()
                    self.flashes += 1
                    self.flash(x, y)

        for y in range(self.ylim):
            for x in range(self.xlim):
                self.m[x, y].reset()
                
    def flash(self, x, y):
        #print ("flash: ", x, y)
        neigh = self.neighbours(x, y)
        #print (neigh)
        for n in neigh:            
            self.m[n[0], n[1]].gain()
            #print (n[0], n[1], self.m[n[0], n[1]].energy)
            if self.m[n[0], n[1]].energy > 9 and not self.m[n[0], n[1]].flashed:
                #print ("flash: ", n[0], n[1])
                self.m[n[0], n[1]].flash()
                self.flash(n[0], n[1])
                self.flashes += 1

    def theMap(self):
        cm = np.zeros(shape=(self.xlim, self.ylim))
        flashed = []
        for y in range(self.ylim):
            for x in range(self.xlim):
                cm[x, y] = self.m[x, y].energy
                if self.m[x, y].energy == 0:
                    flashed.append([x, y])

        return cm, flashed

    def syncro(self):
        m, dummy = self.theMap()
        if m.sum() == 0:
            return True
        else:
            return False

                
    def neighbours(self, x, y):
        n = []
        n.append([x-1, y-1])
        n.append([x-1, y])
        n.append([x-1, y+1])
        n.append([x, y-1])
        n.append([x, y+1])
        n.append([x+1, y-1])
        n.append([x+1, y])
        n.append([x+1, y+1])

        real_n = []
        for i in n:
            if 0 <= i[0] < self.xlim and 0 <= i[1] < self.ylim:
                real_n.append(i)
        return real_n
        
        
steps = 200
m = Map("input_11.txt")
for s in range(steps):
    m.step()
    #cm, p = m.theMap()
    #printArray(cm, p, bcolors.YELLOW)
    #print("")

print ("🎄 Part 1: {}".format(m.flashes))


m = Map("input_11.txt")
s = 0
while (not m.syncro()):
    m.step()
    s += 1
    if m.syncro():
        cm, p = m.theMap()
        printArray(cm, p, bcolors.YELLOW)
        print("")
        print ("🎄🎅 Part 2: {}".format(s))
        break



from utils import readInput
import numpy as np

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, c1, c2):
        if (c1.x > c2.x):
            c1, c2 = c2, c1
        self.c1 = c1
        self.c2 = c2
        if (c2.x-c1.x) == 0:
            self.m = 1e10
        else:
            self.m = (c2.y - c1.y)/(c2.x - c1.x)
        self.q = c1.y - self.m*c1.x

    def maxX(self):
        return max(self.c1.x, self.c2.x)

    def maxY(self):
        return max(self.c1.y, self.c2.y)

    def points(self):
        ps = []
        if self.m != 1e10:
            for x in range(self.c1.x, self.c2.x+1):
                y = int(self.m*x + self.q)
                ps.append([y, x])
        else:
            for y in range(min(self.c1.y, self.c2.y),
                           max(self.c1.y, self.c2.y)+1):
                ps.append([y, self.c1.x])
        return ps

class Field:
    def __init__(self, filename):
        vents = readInput(filename)
        
        self.segs = []
        for v in vents:
            v = v.split(" -> ")
            self.segs.append(Line(Coord(*map(int, v[0].split(","))),
                                  Coord(*map(int, v[1].split(",")))))
                             
        lim = self.findMax()
        self.field = np.zeros(shape=(lim+1, lim+1))

    def findMax(self):
        xmax = max([s.maxX() for s in self.segs])
        ymax = max([s.maxY() for s in self.segs])

        return max(xmax, ymax)

    def solve(self):
        for s in self.segs:
            for p in s.points():
                self.field[p[0], p[1]] += 1
        print (self.field)
        return (self.field >= 2).sum()


filename = "input_5.txt"
f = Field(filename)

print ("🎄🎅 Part 2: ", f.solve())


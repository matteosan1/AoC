import time
import numpy as np

from utils import readInput, Point

class Grid:
    def __init__(self, filename):
        self.grid = {}
        self.start = None
        self.positions = set()
        self.load(filename)
        self.dirs = {0: lambda p: p + Point(0, -1),
                     1: lambda p: p + Point(1, 0),
                     2: lambda p: p + Point(0, 1),
                     3: lambda p: p + Point(-1, 0)}

    def load(self, filename):
        lines = readInput(filename)
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                if c == '#':
                    self.grid[Point(x, y)] = 0
                elif c == 'S':
                    self.positions.add(Point(x, y))
        self.size = (x+1, y+1)
    
    def step(self):
        newPos = set()
        for p in self.positions:
            for d in self.dirs.values():
                if self.wrap(d(p)) not in self.grid:
                    newPos.add(d(p))
                self.positions = newPos
        
    def wrap(self, p):
        return Point(p.x%self.size[0], p.y%self.size[1])


def loadInput():
    pass
        
def part1():
    garden = Grid("input_21.txt")
    for step in range(64):
        garden.step()
    return len(garden.positions)

def part2():
    garden = Grid("input_21.txt")
    # f(x) = how many squares are visited at time 65 + 131*x
    X,Y = [0,1,2], []
    target = (26501365 - 65)//131
    for s in range(65 + 131*2 + 1):
        if s%131 == 65:
            print (len(garden.positions))
            Y.append(len(garden.positions))
        garden.step()
    poly = np.rint(np.polynomial.polynomial.polyfit(X,Y,2)).astype(int).tolist()
    return sum(poly[i]*target**i for i in range(3))

if __name__ == '__main__':
    title = "Day 21: Step Counter"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    #garden = loadInput()

    t0 = time.time()
    res1 = part1()
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2()
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

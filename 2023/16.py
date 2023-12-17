import time
from copy import deepcopy

from utils import readInput, Point

class Cave:
    def __init__(self):
        self.cave = {}
        self.xlims = (0, 0)
        self.ylims = (0, 0)

    def load(self, lines):
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                p = Point(x, y)
                if c == "-" or c == "\\" or c == "/" or c == "|":
                    self.cave[p] = c
                    
        xs = [p.x for p in self.cave.keys()]
        ys = [p.y for p in self.cave.keys()]
        self.xlims = (0, max(xs))
        self.ylims = (0, max(ys))
                    
class Beam:
    def __init__(self, pos, dir, path):
        self.pos = pos
        self.dir = dir
        self.path = path
        
    def move(self, cave, beams):
        if self.dir == 0:
            self.pos.y -= 1
        elif self.dir == 1:
            self.pos.x += 1
        elif self.dir == 2:
            self.pos.y += 1
        elif self.dir == 3:
            self.pos.x -= 1

        if self.pos.x < cave.xlims[0] or self.pos.x > cave.xlims[1] or self.pos.y < cave.ylims[0] or self.pos.y > cave.ylims[1]:
            self.dir += 2
            self.dir %= 4
            return True

        if self.pos not in self.path:
            self.path[deepcopy(self.pos)] = [deepcopy(self.dir)]
        else:
            if self.dir not in self.path[self.pos]:
                self.path[self.pos].append(deepcopy(self.dir))
            else:
                return False

        if self.pos in cave.cave:
            c = cave.cave[self.pos]
            if c == "-" and (self.dir == 0 or self.dir == 2):
                beams.append(Beam(deepcopy(self.pos), 3, self.path))
                self.dir = 1
            elif c == "|" and (self.dir == 1 or self.dir == 3):
                beams.append(Beam(deepcopy(self.pos), 0, self.path))
                self.dir = 2
            elif c == "\\":
                if self.dir == 0:
                    self.dir = 3
                elif self.dir == 1:
                    self.dir = 2
                elif self.dir == 2:
                    self.dir = 1
                elif self.dir == 3:
                    self.dir = 0
            elif c == "/":
                if self.dir == 0:
                    self.dir = 1
                elif self.dir == 1:
                    self.dir = 0
                elif self.dir == 2:
                    self.dir = 3
                elif self.dir == 3:
                    self.dir = 2
        return True

def loadInput():
    lines = readInput("input_16.txt")
    cave = Cave()
    cave.load(lines)
    return cave

def printMap(cave, path):
    for y in range(cave.ylims[0], cave.ylims[1]+1):
        for x in range(cave.xlims[0], cave.xlims[1]+1):
            p = Point(x, y)
            if p in path:
                print ("#", end='')
            else:
                print (".", end='')
        print()

def part1(cave):
    path = {}
    beams = [Beam(Point(-1, 0), 1, path)]
    while len(beams) > 0:
        b = beams.pop()
        while b.move(cave, beams):
            pass
    #printMap(cave, path)
    return len(path)

def part2(cave):
    energy = 0
    for x in range(cave.xlims[0], cave.xlims[1]+1):
        for y in range(2):
            if y == 0:
                dir = 2
                p = Point(x, -1)
            else:
                dir = 0
                p = Point(x, cave.ylims[1]+1)
                
            path = {}
            beams = [Beam(p, dir, path)]
            while len(beams) > 0:
                b = beams.pop()
                while b.move(cave, beams):
                    pass
            if len(path) > energy:
                energy = len(path)
    return energy

if __name__ == '__main__':
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    print("⛄ Day 16: The Floor Will Be Lava ⛄")
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

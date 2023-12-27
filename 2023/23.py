import time
from itertools import combinations

from utils import readInput #, Point

class SnowIsland:
    def __init__(self):
        self.path = {}
        #self.dirs = {0:lambda c:c + Point(0,-1),
        #             1:lambda c:c + Point(1,0),
        #             2:lambda c:c + Point(0,1),
        #             3:lambda c:c + Point(-1,0),}

    def get_neighs(self, pos, part=1):
        typ = self.path[pos].typ
        if part == 2:
            new_pos = []
            for t in self.dirs:
                temp = self.dirs[t](pos)
                if temp in self.path:
                    new_pos.append(temp)
        else:
            if typ != -1:
                new_pos = [self.dirs[typ](pos)]
            else:
                new_pos = []
                for t in self.dirs:
                    temp = self.dirs[t](pos)                    
                    if temp in self.path:
                        new_pos.append(temp)
        return new_pos

    def n_neighs(self, k):
        return n

    def load(self, lines):
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                if c == "#":
                    continue
                p = Point(x, y)
                if c == ".":
                    p.typ = -1
                elif c == ">":
                    p.typ = 1
                elif c == "v":
                    p.typ = 2
                elif c == "^":
                    p.typ = 0
                elif c == "<":
                    p.typ = 3
                self.path[(x, y)] = p

        self.xlims = (0, x+1)
        self.ylims = (0, y+1)
        self.start = (1, 0)
        self.target = (self.xlims[1]-2, self.ylims[1]-1)


def loadInput():
    lines = readInput("prova.txt")
    #lines = readInput("input_23.txt")
    path = {}
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "#":
                continue

            if c == ".":
                typ = -1
            elif c == ">":
                typ = 1
            elif c == "v":
                typ = 2
            elif c == "^":
                typ = 0
            elif c == "<":
                typ = 3
            path[(x, y)] = [typ, {}]

    xlims = (0, x+1)
    ylims = (0, y+1)
    start = (1, 0)
    target = (xlims[1]-2, ylims[1]-1)
    
    prune_graph(path, start, target)
    import sys
    sys.exit()
    return si

dirs = {0:lambda c: (c[0], c[1]-1),
        1:lambda c: (c[0]+1, c[1]),
        2:lambda c: (c[0], c[1]+1),
        3:lambda c: (c[0]-1, c[1]),}

def prune_graph(path, start, target):
    crosses = []
    for k in path:
        n = 0
        for d in dirs.values():
            new_pos = d(k)
            if new_pos in path:
                n += 1
        if n > 2:
            crosses.append(k)            
    crosses.append(start)
    crosses.append(target)

    new_path = {}
    for c in combinations(crosses, 2):
        #print (c[0], c[1])
        p = dfs2(path, c[0], c[1], crosses)
        if p != []:
            new_path.setdefault(c[0], {})
            new_path[c[0]].setdefault(c[1], len(p)-1)
                                  
    print (new_path)
    
def dfs2(m, start, target, crosses):
    stack = [[start]]

    while len(stack) != 0:
        path = stack.pop()
        #print (path)
        pos = path[-1]
        if pos == target:
            return path

        if pos != start and pos in crosses:
            return []

        for d in dirs.values():
            new_pos = d(pos)
            if new_pos in m and new_pos not in path:
                stack.append(path[:]+[new_pos])
    return []

















    
def dfs(m, start, target, part=1):
    paths = []
    stack = [[start]]

    while len(stack) != 0:
        path = stack.pop()
        #print (path)
        pos = path[-1]
        if pos == target:
            paths.append(path)
            continue

        neighs = m.get_neighs(pos, part)
        #print (neighs)
        for new_pos in neighs:
            if new_pos not in path:
                stack.append(path[:]+[new_pos])
    return paths

def part1(si):
    return 0
    paths = dfs(si, si.start, si.target)
    lengths = [len(p)-1 for p in paths]
    return max(lengths)

def part2(si):
    paths = dfs(si, si.start, si.target, part=2)
    lengths = [len(p)-1 for p in paths]
    return max(lengths)
    return 0

if __name__ == '__main__':
    title = "Day 23: Long Walk"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

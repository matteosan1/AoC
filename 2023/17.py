import time
from queue import PriorityQueue
from copy import deepcopy
import heapq

from utils import readInput

class Lavatube:
    def __init__(self):
        self.map = {}
        self.xlims = (0, 0)
        self.ylims = (0, 0)

    def load(self, lines):
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                self.map[(x, y)] = int(c) 
                    
        xs = [p[0] for p in self.map.keys()]
        ys = [p[1] for p in self.map.keys()]
        self.xlims = (0, max(xs))
        self.ylims = (0, max(ys))

def loadInput():
    lines = readInput("input_17.txt")
    lavatube = Lavatube()
    lavatube.load(lines)
    return lavatube

Right = (1, 0)
Down = (0, 1)
Left = (-1, 0)
Up = (0, -1)

def dijkstra_bis(m, start, target, min_conse, max_conse):
    visited = set()
    worklist = [(0, start[0], start[1], Right, 1),
                (0, start[0], start[1], Down, 1)]
    i = 0
    while len(worklist) > 0:
        cost, x, y, dir, dir_count = heapq.heappop(worklist)
        if (x, y, dir, dir_count) in visited:
            continue
        else:
            visited.add((x, y, dir, dir_count))
            
        new_pos = (x + dir[0], y + dir[1])
        if new_pos not in m.map:
            continue
        new_cost = cost + m.map[new_pos]
        if dir_count >= min_conse and dir_count <= max_conse:
            if new_pos == target:
                return new_cost
        for d in [Right, Down, Left, Up]:
            if (d[0] + dir[0], d[1]+dir[1]) == (0, 0):
                continue

            new_d_count = dir_count + 1 if d == dir else 1
            if (d != dir and dir_count < min_conse) or new_d_count > max_conse:
                continue
            heapq.heappush(worklist, (new_cost, new_pos[0], new_pos[1], d, new_d_count))

def part1(lavatube):
    start = (0, 0)
    target = (lavatube.xlims[1], lavatube.ylims[1])
    cost = dijkstra_bis(lavatube, start, target, 0, 3)
    return cost

def part2(lavatube):
    return 0
    start = (0, 0)
    target = (lavatube.xlims[1], lavatube.ylims[1])
    cost = dijkstra_bis(lavatube, start, target, 4, 10)
    return cost

if __name__ == '__main__':
    print(" Day 17:  Clumsy Crucible ")
    print("--------------------------")
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

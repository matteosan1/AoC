import time
from queue import PriorityQueue
from copy import deepcopy
from collections import namedtuple
import heapq

from utils import readInput, Point

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
    lines = readInput("prova.txt")
    lines = readInput("input_17.txt")
    lavatube = Lavatube()
    lavatube.load(lines)
    return lavatube

dirs = {0:lambda c:(c[0], c[1]+1),
        1:lambda c:(c[0]+1, c[1]),
        2:lambda c:(c[0],  c[1]-1),
        3:lambda c:(c[0]-1, c[1])}

State = namedtuple("State", ['cost', 'pos', 'dir', 'dir_count'])
    
def get_neighs(state, m):
    new_dir = [state.dir-1, state.dir, state.dir+1]
    new_states = []
    for i, d in enumerate(new_dir):
        if i == 1 and state.forward == 3:
            continue
        new_state = deepcopy(state)
        new_state.dir = d%4
        new_state.pos = dirs[new_state.dir](new_state.pos)
        if new_state.pos in m.map:
            if i == 1:
                new_state.forward += 1
            else:
                new_state.forward = 1
            new_states.append(new_state)
    return new_states

def termination_end(new_cost, new_pos, target, state, min_conse, max_conse):
    if state.dir_count >= min_conse and state.dir_count <= max_conse:
        if new_pos == target:
            return new_cost

def dijkstra_bis(m, init, target, termination, kwargs):
    visited = set()
    worklist = init
    while len(worklist) > 0:
        current = heapq.heappop(worklist)
        if current[1:] in visited:
            continue
        else:
            visited.add(current[1:])
            
        new_pos = dirs[current.dir](current.pos)
        if new_pos not in m.map:
            continue
        new_cost = current.cost + m.map[new_pos]
        if termination(new_cost, new_pos, target, current, **kwargs):
            return new_cost
            
        for k,v in dirs.items():
            if abs(k - current.dir) == 2:
                continue
            new_d_count = current.dir_count + 1 if k == current.dir else 1
            if (k != current.dir and current.dir_count < kwargs['min_conse']) or new_d_count > kwargs['max_conse']:
                continue
            new_state = State(new_cost, new_pos, k, new_d_count)
            heapq.heappush(worklist, new_state)
    
def part1(lavatube):
    start = (0, 0)
    init = [State(0, start, 1, 1), State(0, start, 2, 1)]
    target = (lavatube.xlims[1], lavatube.ylims[1])
    cost = dijkstra_bis(lavatube, init, target, termination_end, kwargs={"min_conse":0, "max_conse":3})
    return cost

def part2(lavatube):
    start = (0, 0)
    init = [State(0, start, 1, 1), State(0, start, 2, 1)]
    target = (lavatube.xlims[1], lavatube.ylims[1])
    cost = dijkstra_bis(lavatube, init, target, termination_end, kwargs={"min_conse":4, "max_conse":10})
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

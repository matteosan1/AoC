import time
from collections import deque

from utils import readInput, Point, manhattan_dist, shoelace, perimeter

def loadInput():
    lines = readInput("prova.txt")
    lines = readInput("input_18.txt")
    return lines
    
def printMap(world):
    xs = [int(p.real) for p in world]
    ys = [int(p.imag) for p in world]
    xlims = (min(xs), max(xs)+1)
    ylims = (min(ys), max(ys)+1)

    for x in range(*xlims):
        for y in range(*ylims):
            c = complex(x, y)
            if c in world:
                print ("#", end='')
            else:
                print (" ", end='')
        print()
        
dirs = {"U": lambda c: c+complex(0, -1),
        "R": lambda c: c+complex(1, 0),
        "D": lambda c: c+complex(0, 1),
        "L": lambda c: c+complex(-1, 0)}

def span_filling(world, seed):
    if seed not in world:
        world.update({seed:1})
        for k, v in dirs.items():
            span_filling(world, v(seed))   
        
def flood_fill(world, start):
    visited = []
    q = deque()
    q.append(start)
    while len(q) != 0:
        pos = q.popleft()
        visited.append(pos)
                
        for d in dirs.values():
            new_pos = d(pos)
            if new_pos in visited or new_pos in q: 
                continue
            if new_pos not in world:
                q.append(new_pos)
    for v in visited:
        world.update({v:1})
    return world
            
def part1_old(instructions):
    pos = complex(0,0)
    world = {pos:0}
    
    for instr in instructions:
        for i in range(instr[1]):
            pos = dirs[instr[0]](pos)
            world.update({pos:instr[2]})
    printMap(world)
    print()
    #span_filling(world, seed)
    seed = complex(1, 1)
    #world = flood_fill(world, seed) 
    world = flood_fill_v2(world) 
    printMap(world)
    print (len(world))
    return 0
    
def part1(lines):
    p = Point(0, 0)
    vertices = []
    for l in lines:
        parts = l.split()
        if parts[0] == "R":
            p += Point(int(parts[1]), 0)
        elif parts[0] == "D":
            p += Point(0, int(parts[1]))
        elif parts[0] == "L":
            p += Point(-int(parts[1]), 0)
        elif parts[0] == "U":
            p += Point(0, -int(parts[1]))
        vertices.append(p)

    p = perimeter(vertices)
    A = shoelace(vertices)
    i = A + 1 - p/2
    return int(i + p)
    
def part2(lines):    
    p = Point(0, 0)
    vertices = []
    for l in lines:
        code = l.split()[-1][2:-1]
        size, code = int(code[:5], 16), code[-1]
        if code == "0":
            p += Point(size, 0)
        elif code == "1":
            p += Point(0, size)
        elif code == "2":
            p += Point(-size, 0)
        elif code == "3":
            p += Point(0, -size)
        vertices.append(p)
    p = perimeter(vertices)
    A = shoelace(vertices)
    i = A + 1 - p/2
    return int(i + p)

if __name__ == '__main__':
    title = "Day 18: Lavaduct Lagoon"
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

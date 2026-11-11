import time
from math import lcm

from utils import readInput

def loadInput():
    lines = readInput("input_8.txt")
    dirs = [0 if d =="L" else 1 for d in lines[0]]
    nodes = {}
    for l in lines[1:]:
        parts = l.split(" = ")
        nodes[parts[0]] = parts[1][1:-1].split(", ")
    return dirs, nodes

def part1(dirs, nodes):
    steps = 0
    pos = "AAA"
    while pos != "ZZZ":
        dir = dirs[steps%(len(dirs))]
        pos = nodes[pos][dir]
        steps += 1
        
    print (f"🎄 Part 1: {steps}")

def part2(dirs, nodes):
    pos = []
    for n in nodes:
        if n.endswith("A"):
            pos.append(n)
    steps = [0 for i in range(len(pos))]

    for i in range(len(pos)):            
        while True:
            dir = dirs[steps[i]%(len(dirs))]
            pos[i] = nodes[pos[i]][dir]
            steps[i] += 1
            if pos[i].endswith("Z"):
                break
    print (f"🎄🎅 Part 2: {lcm(*steps)}")

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 8         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

t0 = time.time()

dirs, nodes = loadInput()
part1(dirs, nodes)
print (f"Time: {time.time()-t0:.5f}")

t0 = time.time()
part2(dirs, nodes)
print (f"Time: {time.time()-t0:.5f}")

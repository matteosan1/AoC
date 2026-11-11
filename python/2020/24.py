import time
from utils import readInput
start_time = time.time()

def loadInput():
    lines = readInput("input_24.txt")

    return lines

dirs = {"ne":complex(1, -1), "nw":complex(-1, -1),
        "se":complex(1, 1), "sw":complex(-1, 1),
        "e":complex(2, 0), "w":complex(-2, 0)}
grid = {} 

def part1(lines):
    tiles = 0
    for l in lines:
        i = 0
        pos = complex(0, 0)
        while i < len(l):
            if l[i] == 'e' or l[i] == 'w':
                pos += dirs[l[i]]
                i += 1
            else:
                pos += dirs[l[i:i+2]]
                i += 2

        if pos in grid:
            grid[pos] = 1 - grid[pos]
        else:
            grid[pos] = 1

    print ("🎄 Part 1: {}".format(sum(grid.values())))

def addGrid(grid):
    to_add = {}
    for k in grid.keys():
        neighs = [k + d for d in dirs.values()]
        for n in neighs:
            if n not in grid:
                to_add[n] = 0
    grid.update(to_add)

def part2():
    addGrid(grid)
    for day in range(100):
        to_flip = {}
        for k, v in grid.items():
            val = 0
            for d in dirs.values():
                if k + d in grid:
                    val += grid[k+d]
            if (v == 1 and (val == 0 or val > 2)) or (v == 0 and val == 2):
                to_flip[k] = 1-grid[k]
        grid.update(to_flip)
        addGrid(grid)
    
    print ("🎄🎅 Part 2: {}".format(sum(grid.values())))

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 24        ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2()
print ("Time: {:.5f}".format(time.time()-t0))

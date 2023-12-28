import time, numpy as np

from utils import readInput

def printGrid(cm):
    for y in range(cm.shape[1]):
        for x in range(cm.shape[0]):
            if cm[x, y] == 1:
                print ("#", end='')
            else:
                print (".", end='')
        print ("")
    print ("")

def step(grid, part=1):
    xmax = grid.shape[0]
    ymax = grid.shape[1]

    cm = grid.copy()
    for y in range(cm.shape[1]):
        for x in range(cm.shape[0]):
            if part == 2:
                if (x==0 and y==0) or (x==0 and y==ymax-1) or (x==xmax-1 and y==0) or (x==xmax-1 and y==ymax-1):
                    continue

            if cm[x, y] == 1:
                if not 3 <= grid[max(0, x-1):min(x+2, cm.shape[0]),
                                max(0, y-1):min(y+2, cm.shape[1])].sum() <=4:
                    cm[x, y] = 0
            if cm[x, y] == 0:
                if grid[max(0, x-1):min(x+2, cm.shape[0]),
                        max(0, y-1):min(y+2, cm.shape[1])].sum() == 3:
                    cm[x, y] = 1
    return cm

def loadInput():
    lines = readInput("instructions18a.txt")
    xmax = len(lines[0])
    ymax = len(lines)
    grid = np.zeros(shape=(xmax, ymax))

    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if l[x] == "#":
                grid[x, y] = 1
        
    #printGrid(grid)
    return grid

def part1(grid):
    for _ in range(100):
        grid = step(grid)
    printGrid(grid)
    print (f"🎄 Part 1: {(grid==1).sum()}")

def part2(grid):
    xmax = grid.shape[0]
    ymax = grid.shape[1]
    grid[0, 0] = 1
    grid[0, ymax-1] = 1
    grid[xmax-1, 0] = 1
    grid[xmax-1, ymax-1] = 1

    for _ in range(100):
        grid = step(grid, part=2)
    printGrid(grid)
    print (f"🎄🎅 Part 2: {(grid==1).sum()}")
    
if __name__ == "__main__":
    title = "Day 18: Like a GIF For Your Yard"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))

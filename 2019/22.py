import time, numpy as np, copy

from numpy import array_equal

from utils import readInput

def loadInput():
    lines = readInput("input_24.txt")
    #lines = readInput("prova.txt")
    bugs = np.zeros(shape=(len(lines[0]), len(lines)))
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == '#':
                bugs[y, x] = 1
    return bugs
    
def arreq_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if array_equal(elem, myarr)), False)

def biodiversity(bugs, part=1):
    tot = 0
    for y in range(bugs.shape[1]):
        for x in range(bugs.shape[0]):
            if part == 2 and x == y == 2:
                continue
            val = bugs[y, x]
            tot += 2**(x+y*bugs.shape[1]) if val == 1 else 0 
    return tot
    
def part1(bugs):
    old_times = []
    update = np.zeros_like(bugs)
    dirs = ((0,1), (1,0), (-1,0), (0,-1))
    while True:
        for y in range(bugs.shape[1]):
            for x in range(bugs.shape[0]):
                neighs = 0
                for d in dirs:
                    nx, ny = x+d[0], y+d[1]
                    if 0 <= nx < bugs.shape[0] and 0 <= ny < bugs.shape[1]:
                        neighs += bugs[nx, ny]
                if bugs[x, y] == 0:
                    if neighs in (1, 2):
                        update[x, y] = 1
                    else:
                        update[x, y] = 0
                else:
                    if neighs == 1:
                        update[x, y] = 1
                    else:
                        update[x, y] = 0
        bugs = update.copy()
        if arreq_in_list(bugs, old_times):
            break
        old_times.append(bugs)

    print (f"ðŸŽ… Part 1: {biodiversity(bugs)}")
        
def neighbours(levels, update, level):
    dirs = ((0,1), (1,0), (-1,0), (0,-1))
    xmax = levels[level].shape[0]-1
    ymax = levels[level].shape[1]-1
    for y in range(levels[level].shape[1]):
        for x in range(levels[level].shape[0]):
            if x == y == 2:
                continue
            neighs = 0
            for d in dirs:
                if d == (0,-1) and y == 0:
                    neighs += levels[level+1][2, 1]
                elif d == (-1,0) and x == 0:
                    neighs += levels[level+1][1, 2]
                elif d == (0, 1) and y == ymax:
                    neighs += levels[level+1][2, 3]
                elif d == (1, 0) and x == xmax:
                    neighs += levels[level+1][3, 2]
                elif d == (0, 1) and x == 2 and y == 1:
                    neighs += levels[level-1][:, 0].sum()
                elif d == (0, -1) and x == 2 and y == 3:
                    neighs += levels[level-1][:, ymax].sum()                
                elif d == (1, 0) and x == 1 and y == 2:
                    neighs += levels[level-1][0, :].sum()
                elif d == (-1, 0) and x == 3 and y == 2:
                    neighs += levels[level-1][xmax, :].sum()
                else:
                    nx, ny = x+d[0], y+d[1]
                    neighs += levels[level][nx, ny]

            if levels[level][x, y] == 0:
                if neighs in (1, 2):
                    update[level][x, y] = 1
                else:
                    update[level][x, y] = 0
            else:
                if neighs == 1:
                    update[level][x, y] = 1
                else:
                    update[level][x, y] = 0

def part2(bugs):
    levels = {0:bugs}
    for i in range(1, 200):
        levels.update({i:np.zeros_like(bugs)})
        levels.update({-i:np.zeros_like(bugs)})
    min_level, max_level = min(levels.keys()), max(levels.keys())
    for minutes in range(200):
        update = copy.deepcopy(levels)
        for k in levels:
            if k == max_level or k == min_level:
                continue
            neighbours(levels, update, k)
        levels = copy.deepcopy(update)

    tot = 0
    for k in levels:
        tot += levels[k].sum()
    print (f"ðŸŽ„ Part 2: {tot}")
    
if __name__ == "__main__":
    title = "Day 24: Planet of Discord"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    part1(copy.deepcopy(inputs))
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))

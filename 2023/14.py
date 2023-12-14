import time
import numpy as np

from utils import readInput

def loadInput():
    lines = readInput("input_14.txt")
    platform = []
    for y, l in enumerate(lines):
        temp = []
        for x, c in enumerate(l):
            if c == ".":
                temp.append(0)
            elif c == "#":
                temp.append(2)
            elif c == "O":
                temp.append(1)
        platform.append(temp)
    platform = np.array(platform)
    return platform

def find_north_space(rock, column):
    i = rock-1
    for i in range(rock-1, -1, -1):
        if column[i] != 0:
            return i+1
    return 0

def count_load(platform):
    tot = 0
    for x in range(platform.shape[1]):
        tot += (platform.shape[0] - np.where(platform[:, x]==1)[0]).sum()
    return tot
    
def part1(platform):
    for x in range(platform.shape[1]):
        rocks = np.where(platform[:, x] == 1)[0]
        for r in rocks:
            space = find_north_space(r, platform[:, x])
            if space != r:
                platform[r, x] = 0
                platform[space, x] = 1
    return count_load(platform)

def arreq_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if np.array_equal(elem, myarr)), False)

def arridx_in_list(myarr, list_arrays):
    return next((i for i, elem in enumerate(list_arrays) if np.array_equal(elem, myarr)), -1)

def part2(platform):
    cycles = 1000000000
    platforms = []
    for i in range(cycles):
        for rot in range(0, 4):
            for x in range(platform.shape[1]):
                rocks = np.where(platform[:, x] == 1)[0]
                for r in rocks:
                    space = find_north_space(r, platform[:, x])
                    if space != r:
                        platform[r, x] = 0
                        platform[space, x] = 1
            platform = np.rot90(platform, -1)

        if not arreq_in_list(platform, platforms):
            platforms.append(platform.copy())
        else:
            break
    offset = arridx_in_list(platform, platforms)
    period = i - offset
    idx = (cycles - offset)%period+offset-1
    return count_load(platforms[idx])

if __name__ == '__main__':
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    print("⛄ Day 14: Parabolic Reflector Dish ⛄")
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

import time
import numpy as np

from utils import readInput

def decrypt(m, part=1):
    m = m.split(" ")
    if len(m) == 5:
        s = m[2].split(",")
        e = m[4].split(",")
        if m[1] == "off":
            if part == 1:
                v = 0
            else:
                v = -1
        else:
            v = 1
    elif len(m) == 4:
        s = m[1].split(",")
        e = m[3].split(",")
        v = 2
    return [v] + list(map(int, s)) + list(map(int, e))
    
def loadInput():
    lines = readInput("instructions6a.txt")
    return lines

def part1(lines):
    grid = np.zeros(shape=(1000, 1000))
    for l in lines:
        i = decrypt(l)
        if i[0] == 2:
            temp = np.where(grid[i[1]:i[3]+1, i[2]:i[4]+1] == 0, 1, 0)
            grid[i[1]:i[3]+1, i[2]:i[4]+1] = temp
        else:
            grid[i[1]:i[3]+1, i[2]:i[4]+1] = i[0]

    print (f"🎄 Part 1: {np.count_nonzero(grid == 1)}")

def part2(inputs):
    grid = np.zeros(shape=(1000, 1000))

    for l in inputs:
        i = decrypt(l, 2)
        grid[i[1]:i[3]+1, i[2]:i[4]+1] += i[0]
        if i[0] < 0:
            temp = np.where(grid[i[1]:i[3]+1, i[2]:i[4]+1] < 0, 0, grid[i[1]:i[3]+1, i[2]:i[4]+1])
            grid[i[1]:i[3]+1, i[2]:i[4]+1] = temp

    print (f"🎄🎅 Part 2: {int(np.sum(grid))}")

if __name__ == "__main__":
    title = "Day 6: Probably a Fire Hazard"
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

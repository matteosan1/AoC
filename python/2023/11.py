import time
import numpy as np
from itertools import combinations

from utils import readInput, Point, manhattan_dist
        
def loadInput():
    lines = readInput("input_11.txt")
    
    new_lines = []
    for l in lines:
        new_lines.append(list(l))
    grow = []
    gcol = []
    temp = np.array(new_lines)
    for x in range(temp.shape[0]):
        if (temp[x] == '.').all():
            grow.append(x)
    for y in range(temp.shape[1]):
        if (temp[:, y] == '.').all():
            gcol.append(y)

    galaxies = []
    for x in range(temp.shape[0]):
        for y in range(temp.shape[1]):
            if temp[x, y] == "#":
                galaxies.append(Point(x, y))
    return galaxies, grow, gcol
    
def count_rowcol(c1, c2, grow, gcol):
    n = 0
    if c1.x > c2.x:
        c1, c2 = c2, c1
    for x in grow:
        if c1.x < x < c2.x:
            n += 1
    
    if c1.y > c2.y:
        c1, c2 = c2, c1
    for y in gcol:
        if c1.y < y < c2.y:
            n += 1
    return n
    
def distances(inputs, expansion_factor):
    expansion_factor -= 1
    galaxies, grow, gcol = inputs
    lengths = 0
    for c in combinations(galaxies, 2):
        n = count_rowcol(*c, grow, gcol)
        d = manhattan_dist(*c) + n*expansion_factor    
        lengths += d
    return lengths

def part1(inputs): 
    return distances(inputs, 2)

def part2(inputs):
    return distances(inputs, 1000000)

if __name__ == '__main__':
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    print("⛄        Day 11        ⛄")
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

import time
import numpy as np
from utils import readInput

def loadInput():
    lines = readInput("input_3.txt")
    return lines

def part1(lines):
    y = 0
    x = 0
    trees = 0
    N = len(lines)
    Nx = len(lines[0])
    while True:
        y += 1
        if y >= N:
            break
        x += 3
        x = x % Nx
        if lines[y][x] == "#":
            trees += 1
    print ("🎄 Part 1: {}".format(trees))

def part2(lines):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = []

    N = len(lines)
    Nx = len(lines[0])

    for slope in slopes:
        y = 0
        x = 0
        tree = 0
        while True:
            y += slope[1]
            if y >= N:
                break
            x += slope[0]
            x = x % Nx

            if lines[y][x] == "#":
                tree += 1
        trees.append(tree)
    
    print ("🎄🎅 Part 2: {}".format(np.prod(trees)))

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 3         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

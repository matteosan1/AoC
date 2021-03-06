import numpy as np

lines = []
with open("input_3a.txt") as f:
    for l in f:
        lines.append(l.split("\n")[0])

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
    
print (trees)
print (np.prod(trees))

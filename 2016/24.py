from itertools import permutations, combinations
from utils import readInput
import numpy as np

def bfs(pair, points):
    start = points[pair[0]]
    end = points[pair[1]]
    visited = {}
    steps = 0
    current = {start:None}

    while True:
        new_pos = {}
        for c, prec in current.items():
            if c in visited:
                if visited[c][1] > steps:
                    visited[c] = (prec, steps)
            else:
                visited[c] = (prec, steps)
                for s in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    pos = (c[0] + s[0], c[1] + s[1])
                    if cm[pos[0], pos[1]] != 1 and pos[0]>= 0 and pos[1]>=0:
                        if pos not in new_pos:
                            new_pos[pos] = c
                
        current = new_pos
        if end in visited:
            return visited[end][1]
        steps += 1


lines = readInput("input_24.txt")
xmax = len(lines[0])
ymax = len(lines)
cm = np.zeros(shape=(xmax, ymax))
points = {}

for y in range(ymax):
    for x in range(xmax):
        if lines[y][x] == "#":
            cm[x, y] = 1
        elif lines[y][x].isdigit():
           points[int(lines[y][x])] = (x, y)

distances = {i:{} for i in range(len(points))}
for c in combinations(range(len(points)), 2):
    distance = bfs(c, points)
    distances[c[0]][c[1]] = distance
    distances[c[1]][c[0]] = distance


min_dists = [1e10, 1e10]
for p in permutations(range(1, len(points))):
    paths = [[0] + list(p), [0] + list(p) + [0]]
    for i in range(2):
        dist = sum([distances[paths[i][j]][paths[i][j+1]] for j in range(len(paths[i])-1)])
        if dist < min_dists[i]:
            min_dists[i] = dist

print ("🎄Part 1: {}".format(min_dists[0]))
print ("🎁🎄Part 2: {}".format(min_dists[1]))

from utils import readInput, printPath
import numpy as np
from heapdict import heapdict

scale = 5
lines = readInput("input_15.txt")
xmax = len(lines[0])
ymax = len(lines)

a = np.zeros(shape=(xmax, ymax))
for y in range(ymax):
    for x in range(xmax):
        a[(x, y)] = int(lines[y][x])

cavern = np.zeros(shape=(xmax*scale, ymax*scale))
s = 0
for x in range(0, scale):
    for y in range(0, scale):
        cavern[xmax*x:xmax*(1+x), ymax*y:ymax*(1+y)] = a + x + y
        s += 1

cavern[cavern>9] = cavern[cavern>9]%9 

xmax *= scale
ymax *= scale

start = (0,0)
end = (xmax-1, ymax-1)
neighs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
shortest = np.ones(shape=(xmax, ymax))*-1
shortest[0, 0] = 0
que = heapdict()
que[start] = 0
visited = set()
while que:
    node, dist = que.popitem()
    visited.add(node)
    for n in neighs:
        neigh = (node[0] + n[0], node[1] + n[1])
        if (0 <= neigh[0] < xmax and 0 <= neigh[1] < ymax and neigh not in visited):
            new_dist = shortest[node[0], node[1]] + cavern[neigh[0], neigh[1]]
            if new_dist < shortest[neigh[0], neigh[1]] or shortest[neigh[0], neigh[1]] == -1:
                shortest[neigh[0], neigh[1]] = new_dist
                que[neigh] = new_dist

#printPath(cavern, shortest, start, end)
print ("🎄🎅 Part 2: {}".format(shortest[-1, -1]))

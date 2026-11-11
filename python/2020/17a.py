import time
import numpy as np
start_time = time.time()

def printGrid(grids):
    for ig, g in enumerate(grids):
        print ("z={}".format(ig))
        print (g)

def reshape(grids):
    grids.insert(0, np.zeros(shape=grids[0].shape))
    grids.append(np.zeros(shape=grids[0].shape))

# def checkEdges(grid):
#     r = np.sum(grid[0, :, 0]) + np.sum(grid[-1, :, 0]) + np.sum(grid[-1, :, -1]) + np.sum(grid[0, :, -1]) + \
#         np.sum(grid[:, 0, 0]) + np.sum(grid[:, -1, 0]) + np.sum(grid[:, -1, -1]) + np.sum(grid[:, 0, -1]) + \
#         np.sum(grid[0, 0, :]) + np.sum(grid[-1, 0, :]) + np.sum(grid[-1, -1, :]) + np.sum(grid[0, -1, :])
#     return r > 0

def addDim(grid):
    row = np.zeros((1, len(grid[0])))
    col = np.zeros((grid.shape[1], 1))
    grid = np.insert(grid, 0, row, axis=1)
    grid = np.append(grid, col, axis=1)

    row = np.zeros((1, len(grid[0])))
    grid = np.insert(grid, 0, row, axis=0)
    grid = np.append(grid, row, axis=0)
    return grid

lines = []
with open("test_17a.txt") as f:
    for l in f:
        l = l.split("\n")[0]
        l = list(map(int, l.replace('#', '1').replace('.', '0')))
        lines.append(l)

dx = np.arange(-1, 1, 1)
dy = np.arange(-1, 1, 1)
dz = np.arange(-1, 1, 1)

grids = [np.array(lines)]
reshape(grids)
#if checkEdges(grid):
#    grid = addDim(grid)
printGrid(grids)

for ig, g in enumerate(grids):
    for r in np.arange(g.shape[0]):
        for c in np.arange(g.shape[1]):
            dz = (max(0, ig-1), min(ig+1, len(g)-1))
            xlim = (max(0, r), min(r+1, len(g.shape[0])-1))
            ylim = (max(0, c), min(c+1, len(g.shape[1])-1))
            temp = np.array(shape=(3,3,3))

            for x in dx:
            if z < 0 or x == g.shape[0]:
                continue
            for y in dy:
                if y < 0 or y == g.shape[1]:
                    continue
                if x == y == z == 0:
                    continue


#print('🎄 Part 1: {} 🎄'.format(sanity))
#print("\n--- %.7s secs ---" % (time.time() - start_time))

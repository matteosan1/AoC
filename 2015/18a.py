import numpy as np

def printGrid(cm):
    for y in range(cm.shape[1]):
        for x in range(cm.shape[0]):
            if cm[x, y] == 1:
                print ("#", end='')
            else:
                print (".", end='')
        print ("")
    print ("")

def step(grid):
    cm = grid.copy()
    for y in range(cm.shape[1]):
        for x in range(cm.shape[0]):
            if cm[x, y] == 1:
                if not 3<= grid[max(0, x-1):min(x+2, cm.shape[0]),
                                max(0, y-1):min(y+2, cm.shape[1])].sum() <=4:
                    cm[x, y] = 0
            if cm[x, y] == 0:
                if grid[max(0, x-1):min(x+2, cm.shape[0]),
                        max(0, y-1):min(y+2, cm.shape[1])].sum() == 3:
                    cm[x, y] = 1
    return cm
            
filename = "instructions18a.txt"
with open(filename) as f:
    lines = f.readlines()

xmax = len(lines[0])-1
ymax = len(lines)
grid = np.zeros(shape=(xmax, ymax))

for y in range(ymax):
    l = lines[y].split("\n")[0]
    for x in range(xmax):
        if l[x] == "#":
            grid[x, y] = 1
        else:
            l[x] == 0
    
printGrid(grid)
for _ in range(100):
    grid = step(grid)
    printGrid(grid)

print ((grid==1).sum())

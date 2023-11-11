from utils import readInput, printMap
import numpy as np
from matplotlib import pyplot as plt

filename = "input_13.txt"
points = []
foldings = []

lines = readInput(filename)
for l in lines:
    if l.strip() == "":
        continue
    if "," in l:
        points.append(list(map(int, l.split(","))))
    elif "y" in l:
        foldings.append(("y", int(l.split("=")[-1])))
    elif "x" in l:
        foldings.append(("x", int(l.split("=")[-1])))

xmax = max([x[0] for x in points])+1
ymax = max([x[1] for x in points])+1
                        
cm = np.zeros(shape=(xmax, ymax))
for p in points:
    cm[p[0], p[1]] = 1
#printMap(cm)

for i, f in enumerate(foldings):
    if f[0] == "y":
        new_cm = cm[:, :f[1]]
        temp = np.flip(cm[:, f[1]+1:], 1)
        ystart = new_cm.shape[1] - temp.shape[1]
        new_cm[:, ystart:] += temp
    else:
        new_cm = cm[0:f[1], :]
        temp = np.flip(cm[f[1]+1:, :], 0)
        xstart = new_cm.shape[0] - temp.shape[0]
        new_cm[xstart:, :] += temp

    cm = new_cm.copy()
    if i == 0:
        print ("🎄 Part 1: {}".format(int((cm>0).sum())))
        
print ("🎄🎅 Part 2: {}".format("\n"))
printMap(cm)



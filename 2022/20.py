from utils import readInput, printMap
import numpy as np

def enlarge(cm, pad_val=0):
    if pad_val == 0:
        b = np.zeros((cm.shape[0]+6, cm.shape[1]+6))
    else:
        b = np.ones((cm.shape[0]+6, cm.shape[1]+6))
    b[3:-3, 3:-3] = cm
    return b

def run(cm, enhance, steps):
    for s in range(steps):
        cm = enlarge(cm, s%2)
        new_cm = np.zeros(cm.shape)
        for y in range(cm.shape[1]-2):
            for x in range(cm.shape[0]-2):
                bits = [str(int(cm[x+i, y+j])) for j in range(3) for i in range(3)]
                new_cm[x+1, y+1] = int(enhance[int("".join(bits), 2)])

        #printMap(new_cm)
        cm = new_cm[2:-2, 2:-2]
    return cm

lines = readInput("input_20.txt")

enhance = lines[0].replace(".", "0").replace("#", "1")
cm = np.zeros(shape=(len(lines[2]), len(lines)-1))
for y in range(len(lines)-1):
    for x in range(len(lines[y+1])):
        if lines[y+1][x] == "#":
            cm[x, y] = int(1)

cm1 = run(cm, enhance, 2)
print ("🎄 Part 1: {}".format((cm1==1).sum()))

cm1 = run(cm, enhance, 50)
print ("🎄🎅 Part 2: {}".format((cm1==1).sum()))

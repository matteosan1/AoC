from utils import readInput
import numpy as np

trans_from = {2:[], 3:[]}
trans_to = {2:[], 3:[]}
lines = readInput("input_21.txt")
for l in lines:
    parts = l.split(" => ")
    idx = len(parts[0].split("/"))
    for i, p in enumerate(parts):
        subparts = p.split("/")
        ys = []
        for s in subparts:
            xs = []
            for c in s:
                if c == "#":
                    xs.append(1)
                else:
                    xs.append(0)
            ys.append(xs)
        if i == 0:
            m = np.array(ys, int)
            trans_from[idx].append(m)
        else:
            trans_to[idx].append(np.array(ys))

def transformInput(start):
    transformed = []
    for i in range(4):
        for j in range(3):
            if j == 0:
                m = np.rot90(start, i)
            elif j == 1:
                m = np.fliplr(np.rot90(start, i))
            elif j == 2:
                m = np.flipud(np.rot90(start, i))
            for t in transformed:
                if np.array_equal(t, m):
                    break
            else:
                yield m
                
start = np.array([[0,1,0],[0,0,1],[1,1,1]], int)

for r in range(5):
    size = start.shape[0]
    if size % 2 == 0:
        idx = 2
    else:
        idx = 3
    enhance = np.zeros(shape=(size+size//idx, size+size//idx))
    for x in range(0, size//idx):
        for y in range(0, size//idx):
            submatrix = start[x*idx:(x+1)*idx, y*idx:(y+1)*idx]
            val_s = (submatrix==1).sum()
            found = -1
            for itrans, t in enumerate(trans_from[idx]):
                on = (t==1).sum()
                if val_s != on:
                    continue
                generator = transformInput(submatrix)

                while True:
                    try:
                        m = next(generator)
                        if  np.array_equal(t, m):
                            found = itrans
                            break
                    except StopIteration:
                        break
                if found != -1:
                    break
            else:
                print ("PROBLEMA")
                import sys
                sys.exit()
            enhance[x*(idx+1):(x+1)*(idx+1), y*(idx+1):(y+1)*(idx+1)] = trans_to[idx][itrans]
            
    start = enhance.astype(int)
#print (start)
print ("🎄Part 1: {}".format((start==1).sum()))

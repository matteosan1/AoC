from utils import readInput
import numpy as np


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


def isin(t, a1):
    for m in t:
        if np.equal(a1, m).all():
            return True
    else:
        return False
    
trans_from = {2:[], 3:[]}
trans_to = {2:[], 3:[]}
lines = readInput("input_21.txt")
for l in lines:
    parts = l.split(" => ")
    insert = 0
    idx = len(parts[0].split("/"))
    for i, p in enumerate(parts):
        ys = []
        for y in p.split("/"):
            xs = []
            for x in y:
                if x == "#":
                    xs.append(1)
                else:
                    xs.append(0)
            ys.append(xs)
        if i == 0:
            m = np.array(ys, int)
            generator = transformInput(m)
            while True:
                try:
                    t = next(generator)
                    if not isin(trans_from[idx], t):
                         trans_from[idx].append(t)
                         insert += 1
                except StopIteration:
                    break
        else:
            for _ in range(insert):
                trans_to[idx].append(np.array(ys))

start = np.array([[0,1,0],[0,0,1],[1,1,1]], int)

for r in range(18):
    size = start.shape[0]
    if size % 2 == 0:
        idx = 2
    else:
        idx = 3
    print (r, size)
    enhance = np.zeros(shape=(size+size//idx, size+size//idx))
    for x in range(0, size//idx):
        for y in range(0, size//idx):
            submatrix = start[x*idx:(x+1)*idx, y*idx:(y+1)*idx]
            val_s = (submatrix==1).sum()
            for itrans, t in enumerate(trans_from[idx]):
                on = (t==1).sum()
                if val_s != on:
                    continue
                if  np.array_equal(t, submatrix):
                    break
            else:
                print ("PROBLEMA")
                import sys
                sys.exit()
            enhance[x*(idx+1):(x+1)*(idx+1), y*(idx+1):(y+1)*(idx+1)] = trans_to[idx][itrans]
            
    start = enhance.astype(int)
#print (start)
print ("🎁🎄Part 2: {}".format((start==1).sum()))

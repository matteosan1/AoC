import numpy as np

fabric = np.zeros(shape=(1000, 1000))

def intersect(f1, f2):
    #f1 = ids[id1]
    #f2 = ids[id2]
    l1 = (f1[0], f1[1])
    r1 = (f1[0]+f1[2], f1[1]+f1[3])
    l2 = (f2[0], f2[1])
    r2 = (f2[0]+f2[2], f2[1]+f2[3])

    if r1[0] < l2[0] or l1[0] > r2[0]:
        return False
    
    #if (l1[0] > r2[0] or l2[0] > r1[0]):
    #    return False 

    if r1[1] < l2[1] or r2[1] < l1[1]:
    #if (l1[1] < r2[1] or l2[1] < r1[1]):
        return False
  
    return True

def assign(l, t, w, h):
    for x in range(l, l+w):
        for y in range(t, t+h):
            fabric[x][y] = fabric[x][y] + 1
            

with open("squares.txt") as f:
    lines = f.readlines()

ids = {}
for l in lines:
    l = l.split("\n")[0]
    items = l.split(" ")
    l, t = items[2][:-1].split(",")
    w, h = items[3].split("x")
    ids[int(items[0][1:])] = (int(l), int(t), int(w), int(h))
    #1331 @ 308,708: 27x23


for i in ids.values():
    assign(*i)

values = fabric[fabric>=2]
print (len(values))

good = []
for i1 in sorted(ids.keys()):
    inter = 0
    for i2 in sorted(ids.keys()):
        if i1 == i2:
            continue
        if intersect(ids[i1], ids[i2]):
            inter = inter + 1

    if inter == 0:
        good.append(i1)
print good
    

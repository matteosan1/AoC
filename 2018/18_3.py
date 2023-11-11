import time, copy

xmax = 50
ymax = 50

def printAcres(acres):
    for y in range(ymax):
        for x in range(xmax):
            print acres[(x, y)],
        print

def checkAcre(acres, changes, x, y):
    o, t, l = 0, 0, 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < 0 or i >= xmax or j < 0 or j >= ymax:
                continue
            if i == x and j == y:
                continue
            if acres[(i, j)] == ".":
                o = o + 1
            elif acres[(i, j)] == "|":
                t = t + 1
            elif acres[(i, j)] == "#":
                l = l + 1

    if acres[(x, y)] == "." and t >= 3:
        changes[(x, y)] = "|"
    if acres[(x, y)] == "|" and l >= 3:
        changes[(x, y)] = "#"
    if acres[(x, y)] == "#":
        if l >= 1 and t >= 1:
            changes[(x, y)] = "#"
        else:
            changes[(x, y)] = "."
            

with open("acres.txt", "r") as f:
    lines = f.readlines()

acres = {}
for y,l in enumerate(lines):
    for x in range(len(l)):
        acres[(x, y)] = l[x]

import sys
sys.exit()
#printAcres(acres)
#print
history = [copy.deepcopy(acres)]

for it in xrange(489 + 7):
    changes = {}
    t1 = time.time()
    for y in range(ymax):
        for x in range(xmax):
            checkAcre(acres, changes, x, y)
    acres.update(changes)
    if acres not in history:
        history.append(copy.deepcopy(acres))
    else:
        index = history.index(acres)
        print it - index + 1
        break
    t2 = time.time()
    #print (t2 - t1)

#printAcres(acres)xs

t, l = 0, 0
for k, v in acres.iteritems():
    if v == "|":
        t = t + 1
    elif v == "#":
        l = l + 1

print t*l

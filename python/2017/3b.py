from itertools import product

n = 368078
curLoc = 0+0j
numSteps = 1
sz = 1
left = 1
curStep = 0
curDir = 1j

vals = {}
vals[curLoc] = 1
while vals[curLoc] <= n:
    numSteps += 1
    curStep += 1
    curLoc += curDir
    if curStep == sz:
        if left == 1:
            left -= 1
            curDir *= 1j
        else:
            left = 1
            curDir *= 1j
            sz += 1
            
        curStep = 0;
    s = 0
    for p in product([-1, 0, 1], repeat=2):
        if p == (0, 0):
            continue
        coord = curLoc+complex(*p)
        if coord in vals:
            s += vals[coord]
    vals[curLoc] = s

print ("🎁🎄Part 2: {}".format(s))

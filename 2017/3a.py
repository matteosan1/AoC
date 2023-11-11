n = 368078
curLoc = 0+0j
numSteps = 1
sz = 1
left = 1
curStep = 0
curDir = 1j
count = 1

vals = {}
vals[curLoc] = count
while vals[curLoc] < n:
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
    count += 1
    vals[curLoc] = count

print 
print ("🎄Part 1: {}".format(int(abs(curLoc.real) + abs(curLoc.imag))))

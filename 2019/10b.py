import math

def show(p):
    global amap
    
    for y in range(5):
        for x in range(17):
            if p == (x,y):
                print ("X", end='')
            else:
                if (x,y) in amap:
                    print ("#", end='')
                else:
                    print (".", end='')
        print ()
    print ()
    
def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

with open("input10a.txt", "r") as f:
    lines = f.readlines()

amap = []
y = 0
for l in lines:
    x = 0
    for c in l:
        if c == "#":
            amap.append((x,y))
        x += 1
    y += 1

slopes = {}
a = (28, 29)
#a = (11,13)
for b in amap:
    if a == b:
        continue
    slope = math.atan2(b[0]-a[0], b[1]-a[1])
    slopes.setdefault(slope, []).append((b, dist(a, b)))
    #print (a, b, slope)
#import sys
#sys.exit()
for k in slopes.keys():
    slopes[k] = sorted(slopes[k], key=lambda x:x[1])

#print (slopes)
#import sys
#sys.exit()
vaporized = []

l = sum([len(v) for v in slopes.values()])
while l > 0:
    for k in sorted(slopes.keys(), reverse=True):
        #if k <= math.pi/2:
            if slopes[k] != []:
                val = slopes[k].pop(0)
                #show(val[0])
                vaporized.append(val)
    

    #for k in sorted(slopes.keys(), reverse=True):
    #    if k > math.pi/2:
    #        if slopes[k] != []:
    #            vaporized.append(slopes[k].pop(-1))
    

    l = sum([len(v) for v in slopes.values()])
print (vaporized[199])

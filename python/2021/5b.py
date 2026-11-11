from utils import readInput
import numpy as np

vents = readInput("input_5.txt")

vent_coords = []
for v in vents:
    v = v.split(" -> ")
    c1 = list(map(int, v[0].split(",")))
    c2 = list(map(int, v[1].split(",")))

    if (c1[0] < c2[0]):
        vent_coords.append([c1, c2])
    else:
        vent_coords.append([c2, c1])
        
xmin = min(min([v[0][0] for v in vent_coords],
               [v[1][0] for v in vent_coords]))
xmax = max(max([v[0][0] for v in vent_coords],
               [v[1][0] for v in vent_coords]))

ymin = min(min([v[0][1] for v in vent_coords],
               [v[1][1] for v in vent_coords]))
ymax = max(max([v[0][1] for v in vent_coords],
               [v[1][1] for v in vent_coords]))

lim = max(xmax, ymax)
vent_map = np.zeros(shape=(lim+1, lim+1))

n = 0
for c1, c2 in vent_coords:
    if c1[0] == c2[0]:
        dx = 0
    else:
        dx = 1

    if c1[1] > c2[1]:
        dy = -1
    elif c1[1] < c2[1]:
        dy = 1
    else:
        dy = 0

    #print (c1, c2, dx, dy)

    if dx != 0 :
        p = 0
        for x in range(c1[0], c2[0]+1):    
            vent_map[c1[1]+dy*p, x] += 1
            p += 1
    else:
        #print (min(c1[1], c2[1]+1))
        for y in range(min(c1[1], c2[1]),
                       max(c1[1], c2[1])+1):
            #print (y)
            vent_map[y, c1[0]] += 1
    #if n == 3:
    #    break
    n += 1

#print (vent_map)
res = (vent_map >= 2).sum()

print ("🎄🎅 Part 2: ", res)


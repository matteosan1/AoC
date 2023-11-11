from utils import readInput
import numpy as np
#import numpy.ma as ma

vents = readInput("input_5.txt")

vent_coords = []
for v in vents:
    v = v.split(" -> ")
    c1 = list(map(int, v[0].split(",")))
    c2 = list(map(int, v[1].split(",")))
    if c1[0] == c2[0] or c1[1] == c2[1]:
        vent_coords.append([c1, c2])
        
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

for v in vent_coords:
    for x in range(min(v[0][0], v[1][0]),
                   max(v[0][0], v[1][0])+1):
        for y in range(min(v[0][1], v[1][1]),
                       max(v[0][1], v[1][1])+1):
            vent_map[y, x] += 1

print (vent_map)
res = (vent_map >= 2).sum()

print ("🎄 Part 1: ", res)



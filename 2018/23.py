from utils import readLines, manahattanDistance3d
from operator import itemgetter

lines = readLines("nanobots.txt")

bots = []

for l in lines:
    r = int(l.split("r=")[1])
    x, y, z =list(map(int, l.split("=<")[1].split(">")[0].split(",")))
    bots.append((x,y,z,r))

max_r = max(bots,key=itemgetter(3))

inRange = 0
for b in bots:
    d = manahattanDistance3d(b, max_r)
    if d <= max_r[3]:
        inRange = inRange + 1

print (inRange)

# part 2

# xmin = min(bots,key=itemgetter(0))[0]
# xmax = max(bots,key=itemgetter(0))[0]
# ymin = min(bots,key=itemgetter(1))[1]
# ymax = max(bots,key=itemgetter(1))[1]
# zmin = min(bots,key=itemgetter(2))[2]
# zmax = max(bots,key=itemgetter(2))[2]
#
# print (xmin, xmax)
# print (ymin, ymax)
# print (zmin, zmax)
#
# r = 1000000
# for _ in range(7):
#     points = {}
#     iter = 0
#     for x in range(xmin, xmax, int(r)):
#         for y in range(ymin, ymax, int(r)):
#             for z in range(zmin, zmax, int(r)):
#                 #t1 = time.time()
#                 iter = iter + 1
#                 inRange = 0
#                 for b in bots:
#                     p = (x, y, z, 0)
#                     d = manahattanDistance3d(p, b)
#                     if d <= b[3]:
#                         inRange = inRange + 1
#                     points[p] = inRange
#                 #t2 = time.time()
#                 #print (t2 - t1)
#
#     #print (iter)
#     #print (points)
#     best = (max(points.items(), key=itemgetter(1))[0])
#     print (best)
#     r = r / 10
#     xmin = int(best[0] - r)
#     xmax = int(best[0] + r)
#     ymin = int(best[1] - r)
#     ymax = int(best[1] + r)
#     zmin = int(best[2] - r)
#     zmax = int(best[2] + r)
#
# print (manahattanDistance3d(best, (0,0,0,0)))

def lenr(l):
    return range(len(l))

from z3 import *

def zabs(x):
    return If(x >= 0, x, -x)

(x, y, z) = (Int('x'), Int('y'), Int('z'))
in_ranges = [ Int('in_range_' + str(i)) for i in lenr(bots)]
range_count = Int('sum')
o = Optimize()

for i in lenr(bots):
  nx, ny, nz, nrng = bots[i]
  o.add(in_ranges[i] == If(zabs(x - nx) + zabs(y - ny) + zabs(z - nz) <= nrng, 1, 0))
o.add(range_count == sum(in_ranges))
dist_from_zero = Int('dist')
o.add(dist_from_zero == zabs(x) + zabs(y) + zabs(z))
h1 = o.maximize(range_count)
h2 = o.minimize(dist_from_zero)
print (o.check())
#print o.lower(h1)
#print o.upper(h1)
print ("b", o.lower(h2), o.upper(h2))
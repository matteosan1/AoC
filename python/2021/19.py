from utils import readInput
from numpy import cos, sin
import numpy as np
from itertools import product, combinations

def rotate(scan, alpha, beta, gamma):
    R = np.array([[cos(alpha)*cos(beta), cos(alpha)*sin(beta)*sin(gamma) - sin(alpha)*cos(gamma), cos(alpha)*sin(beta)*cos(gamma) + sin(alpha)*sin(gamma)],
                  [sin(alpha)*cos(beta), sin(alpha)*sin(beta)*sin(gamma) + cos(alpha)*cos(gamma), sin(alpha)*sin(beta)*cos(gamma) - cos(alpha)*sin(gamma)], 
                  [-sin(beta), cos(beta)*sin(gamma), cos(beta)*cos(gamma)]])
    return [[int(round(x, 1)) for x in np.array(b).dot(R)] for b in scan]
        
def diff(a, b):
    res = []
    for i in range(len(a)):
        res.append(int(a[i]-b[i]))
    return res

def drift(a, off):
    off = np.array(off)
    res = []
    for i in a:
        res.append((np.array(i)+off).tolist())
    return res

lines = readInput("test.txt")

scan = []
temp = []
for l in lines:
    if "---" in l:
        if temp != []:
            scan.append(temp)
        temp = []
    else:
        temp.append(list(map(int, l.split(","))))
scan.append(temp)

a = (0, np.pi/2, np.pi, 3/2*np.pi)
rotations = []
for p in product(a, repeat=len(scan[0][0])):
    rotations.append(p)

distances = []
for i, s in enumerate(scan):
    temp = {}
    for c in product(range(len(s)), repeat=2):
        a = np.array(s[c[0]])
        b = np.array(s[c[1]])
        temp.setdefault(c[0], []).append(np.linalg.norm(a-b))
    distances.append(temp)

#print (distances)
pairs = []
for p in combinations(list(range(len(scan))), 2):
    d1 = set([val for k, v in distances[p[0]].items() for val in v])
    d2 = set([val for k, v in distances[p[1]].items() for val in v])
    if len(d1.intersection(d2)) >= 66:
        pairs.append(p)
print (pairs)
def findBeacon(d1, d2):
    for k1, v1 in d1.items():
        for k2, v2 in d2.items():
            if len(set(v1).intersection(set(v2))) >= 12:
                print(v1, v2)
                return k1, k2

matches = {}
ref = 0
for p in pairs:
    i = p[0]
    j = p[1]
    
    b1, b2 = findBeacon(distances[i], distances[j])

    for r in rotations:
        rotated = rotate(scan[j], *r)
        offset = diff(scan[i][b1], rotated[b2])
        trans = drift(rotated, offset)
        if sum([int(t in scan[i]) for t in trans]) >= 12:           
            beacons = trans
            key = i
            while True:
                for m in matches:
                    if key == m[1]:
                        beacons = rotate(beacons, *matches[m][1])
                        beacons = drift(beacons, matches[m][0])
                        key = m[0]
                        break
                    if key == ref:
                        break                            
                    if len(matches) == 0:
                        beacons += scan[ref]
            matches[p] = (offset, r)#, beacons)                    
            break

print (matches)
#beacons = []
#for k, v in matches.items():
#    beacons += list(map(tuple, v[2]))
##print (len(beacons))
#
#beacons = sorted(list(set(beacons)), key=lambda x: x[0])
##for b in beacons:
##    print (b)
#print (len(beacons))
#
##7 donne e un mistero
##Diabolik
##No time to die
#

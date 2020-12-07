import re
from itertools import combinations

def potentialEnergy(sat):
    pE = sum(list(map(abs, sat[0])))
    return pE

def kinematicEnergy(sat):
    kE = sum(list(map(abs, sat[1])))
    return kE

def totalEnergy(sat):
    tE = 0
    for k in sat.keys():
        tE +=  kinematicEnergy(sat[k]) * potentialEnergy(sat[k])
    return tE

def show(sat):
    for k in sorted(sat.keys()):
        print ("pos=<x={:2d}, y={:2d}, z={:2d}>, vel=<x={:2d}, y={:2d}, z={:2d}>".format(sat[k][0][0], sat[k][0][1], sat[k][0][2], sat[k][1][0], sat[k][1][1], sat[k][1][2]))
    print ()


r = re.compile("\w=(-?\d+)+")
inputs = []
#filename = "example12a.txt"
filename = "input12a.txt"
with open(filename, "r") as f:
    for i, l in enumerate(f):
        inputs.append(l)

sat = {}
for i, l in enumerate(inputs):
    m = r.findall(l)
    sat[str(i)] = [list(map(int, m)), [0, 0, 0]]

show(sat)
cycles = 1000
for c in range(cycles):
    # update velo
    for comb in combinations(sat.keys(), 2):
        for i in range(3):
            if sat[comb[0]][0][i] < sat[comb[1]][0][i]:
                sat[comb[0]][1][i] += 1
                sat[comb[1]][1][i] -= 1
            elif sat[comb[0]][0][i] > sat[comb[1]][0][i]:
                sat[comb[0]][1][i] -= 1
                sat[comb[1]][1][i] += 1

    # update pos
    for k in sat.keys():
        for i in range(3):
            sat[k][0][i] += sat[k][1][i]

    show(sat)

print (totalEnergy(sat))


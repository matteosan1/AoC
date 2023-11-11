import re, copy, math
from itertools import combinations

def totalEnergy(sat, i):
    tE = 0
    for k in sat.keys():
        tE += abs(sat[k][0][i]) * abs(sat[k][1][i])
    return tE

def primi(n):
    fattori = {}
    d = 2
    while n >= d:
        if n%d==0:
            fattori[d] = fattori.setdefault(d, 0) + 1
            n /= d
        else:
            d += 1
    return fattori

def show(sat):
    for k in sorted(sat.keys()):
        print ("pos=<x={:2d}, y={:2d}, z={:2d}>, vel=<x={:2d}, y={:2d}, z={:2d}>".format(sat[k][0][0], sat[k][0][1], sat[k][0][2], sat[k][1][0], sat[k][1][1], sat[k][1][2]))
    print ()

r = re.compile("\w=(-?\d+)+")
inputs = []
#filename = "example12a.txt"
filename = "input_12.txt"
with open(filename, "r") as f:
    for i, l in enumerate(f):
        inputs.append(l)

sat = {}
for i, l in enumerate(inputs):
    m = r.findall(l)
    sat[str(i)] = [list(map(int, m)), [0, 0, 0]]

cycles = [1, 1, 1]
for coord in range(3):
    #show(sat)
    history = [totalEnergy(sat, coord)]
    first_state = copy.deepcopy(sat)
    while True:
        for comb in combinations(sat.keys(), 2):
           if sat[comb[0]][0][coord] < sat[comb[1]][0][coord]:
                sat[comb[0]][1][coord] += 1
                sat[comb[1]][1][coord] -= 1
           elif sat[comb[0]][0][coord] > sat[comb[1]][0][coord]:
                sat[comb[0]][1][coord] -= 1
                sat[comb[1]][1][coord] += 1

        for k in sat.keys():
            sat[k][0][coord] += sat[k][1][coord]

        tE = totalEnergy(sat, coord)
        if tE == 0:
            ciao = False
            if sat == first_state:
                    ciao = True
                    print (cycles[coord])
                    break
            if ciao:
                break

        cycles[coord] += 1

print (cycles)

scomp = [primi(x) for x in cycles]
keys = []
for s in scomp:
    keys.extend(s.keys())
keys = set(keys)

final_scomp = {}
for k in keys:
    final_scomp[k] = max([s[k] for s in scomp if k in s.keys()])

print (final_scomp)
tot = 1
for k, v in final_scomp.items():
    tot *= math.pow(k, v)
print (int(tot))

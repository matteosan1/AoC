from collections import Counter
import heapq

class Disk:
    def __init__(self, name, weight, disks=[]):
        self.name = name
        self.weight = weight
        if disks != []:
            self.disks = list(map(str.strip, disks.split(",")))
        else:
            self.disks = []

    def __repr__(self):
        s = "{} {}".format(self.name, self.weight) + str(self.disks)
        return s

towers = {}
with open("input_7.txt") as f:
    for l in f:
        if l.startswith("###"):
            break
        parts = l.split("\n")[0].split("->")
        name, weight = parts[0].split()
        weight = int(weight[1:-1])
        if len(parts) == 2:
            d = Disk(name, weight, parts[1])
        else:
            d = Disk(name, weight)
        towers[name] = d

def findWeight(towers, t, level=0):
    #if level != 0:
    w = towers[t].weight
    #else:
    #    w = 0
    if towers[t].disks != []:
        level += 1
        for d in towers[t].disks:
            w += findWeight(towers, d, level)[0]
    else:
        if level == 0:
            level = -1
        w = towers[t].weight
    return w, level

supported = []
for t in towers:
    supported += towers[t].disks
supported = set(supported)

start = set(towers.keys()).difference(supported).pop()
print ("🎄Part 1: {}".format(start))

weights = {}
toweight = []
heapq.heappush(toweight, start)

while len(toweight) != 0:
    t = heapq.heappop(toweight)
    if towers[t].disks != []:
        w, l = findWeight(towers, t)
        weights[t] = (towers[t].disks, w)
        for d in towers[t].disks:
            heapq.heappush(toweight, d)

diff = None
suspect = None
for k, v in weights.items():
    temp = Counter([weights[t][1] for t in v[0] if t in weights])
    if len(temp) > 1:
        wrong_weight = [k for k,v in temp.items() if v == 1][0]
        right_weight = [k for k,v in temp.items() if v != 1][0]
        diff = right_weight - wrong_weight
        suspect = [t for t in v[0] if t in weights and weights[t][1] == wrong_weight][0]
        
print ("🎁🎄Part 2: {} {}".format(suspect, towers[suspect].weight + diff))


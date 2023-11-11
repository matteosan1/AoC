depth =  10914
target = (9, 739)

xmax = target[0] + 50
ymax = target[1] + 50

geoIndex = {}
eroLevel = {}
rockType = {}

def printCave():
    for y in range(ymax):
        for x in range(xmax):
            if (x, y) == (0, 0):
                print("M", end='')
            elif (x, y) == tuple(target):
                print("T", end='')
            elif rockType[(x, y)] == 0:
                print (".", end='')
            elif rockType[(x, y)] == 1:
                print("=", end='')
            elif rockType[(x, y)] == 2:
                print("|", end='')
        print ("")

def geological_index(p):
    if p == (0, 0):
        return 0
    elif p == target:
        return 0
    elif p[1] == 0:
        return p[0] * 16807
    elif p[0] == 0:
        return p[1] * 48271
    else:
        p1 = (p[0] - 1, p[1])
        p2 = (p[0], p[1] - 1)
        if p1 in eroLevel.keys() and p2 in eroLevel.keys():
            return erosion_level(p1) * erosion_level(p2)
        else:
            return None

def erosion_level(p):
    if p in geoIndex.keys():
        return (geoIndex[p] + depth) % 20183

def rock_type(p):
    if p in eroLevel.keys():
        return eroLevel[p] % 3
    else:
        return None

def risk(p):
    #if p in eroLevel.keys():
    return eroLevel[p] % 3
    #else:
    #    return 100000000.

def risk_level():
    rl = 0
    for y in range(ymax):
        for x in range(xmax):
            if (x,y) == target or (x,y) == (0,0):
                continue
            rl = rl + rockType[(x, y)]
    return rl

while True:
    for y in range(ymax):
        for x in range(xmax):
            p = (x, y)
            if geoIndex.get(p) is None:
                geoIndex[p] = geological_index(p)
            else:
                if eroLevel.get(p) is None:
                    eroLevel[p] = erosion_level(p)
                else:
                    if rockType.get(p) is None:
                        rockType[p] = rock_type(p)

    if None not in rockType.values() and len(rockType) == (ymax) * (xmax):
        break

printCave()
print (risk_level())

import heapq

queue = [(0,0,0,1)] # (minutes, x, y, cannot)
best = dict() # (x, y, cannot) : minutes

target = (target[0], target[1], 1)
while queue:
    minutes, x, y, cannot = heapq.heappop(queue)
    best_key = (x, y, cannot)
    if best_key in best and best[best_key] <= minutes:
        continue
    best [best_key] = minutes
    if best_key == target:
        print (minutes)
        break
    for i in range(3):
        if i != cannot and i != risk((x, y)):
            heapq.heappush(queue, (minutes + 7, x, y, i))

    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        newx = x + dx
        newy = y + dy
        if newx < 0 or newx >= xmax:
            continue
        if newy < 0 or newy >= ymax:
            continue
        if newx < 0:
            continue
        if newy < 0:
            continue
        if risk((newx, newy)) == cannot:
            continue
        heapq.heappush(queue, (minutes + 1, newx, newy, cannot))

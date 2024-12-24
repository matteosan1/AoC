import re
from random import randint
from collections import defaultdict

with open("input_24.txt", "r") as f:
    init_p, conns_p = f.read().split("\n\n")
    init_p = init_p.split("\n")
    conns_p = conns_p.split("\n")

res = {}
wires = {}
initwire = set()
xws = set()
yws = set()
finwire = set()
ws = set()

for l in init_p:
    wire = l[:3]
    val = int(l[5:])
    wires[wire] = val
    ws.add(wire)
    initwire.add(wire)
    res[wire] = val
    if wire[0] == 'x':
        xws.add(wire)
    else:
        yws.add(wire)

for l in conns_p:
    #print(l)
    if (l == ""):
        continue
    ts = l.split(" ")
    w1 = ts[0]
    op = ts[1]
    w2 = ts[2]
    ow = ts[4]
    if (re.match('z[0-9][0-9]', ow)):
        finwire.add(ow)
    wires[ow] = (w1, op, w2)
    ws.add(w1)
    ws.add(w2)
    ws.add(ow)

def ev(w,sw):
    if w not in initwire:
        w2 = w
        if w in sw:
            w2 = sw[w]
        if (w in res) and res[w] != -1:
            return res[w]
        tup = wires[w2]
        w1 = tup[0]
        op = tup[1]
        w2 = tup[2]
        ret = -1
        if visited[w]:
            return -1
        visited[w] = True
        if ev(w1,sw)==-1 or ev(w2, sw)==-1:
            return -1
        if op == "AND":
            ret = res[w1] & res[w2]
        elif op == "OR":
            ret = res[w1] | res[w2]
        else:
            ret = res[w1] ^ res[w2]
        res[w] = ret
        return ret
    else:
        return res[w]

def tobinary(n):
    if n==0:
        return [0]
    digits = []
    while n:
        digits.append(n%2)
        n //= 2
    return digits


def setInput(x,y):
    xdigs = tobinary(x)
    ydigs = tobinary(y)
    for i, xi in enumerate(xws):
        res[xi] = xdigs[i] if i<len(xdigs) else 0
    for i, yi in enumerate(yws):
        res[yi] = ydigs[i] if i<len(ydigs) else 0
    for w in ws:
        if w in initwire:
            continue
        res[w] = -1;
    for key in visited.keys():
        visited[key] = False

finwire = sorted(list(finwire))
maxx = 2**len(xws)
maxy = 2**len(yws)
print(f"maxx: {maxx}, maxy: {maxy}")
xws = sorted(list(xws))
yws = sorted(list(yws))
visited = defaultdict(lambda:False)

def higheval(sw):
    randxs = [randint(0,maxx) for i in range(100)]
    randys = [randint(0,maxy) for i in range(100)]
    sc = 0
    for i in range(100):
        setInput(randxs[i],randys[i])
        ret = [ev(w,sw) for w in finwire]
        if -1 in ret:
            return 1000000000
        goal = tobinary(randxs[i]+randys[i])
        goal = goal+[0]*(len(ret)-len(goal))
        for i in range(len(ret)):
            if goal[i] != ret[i]:
                sc += 1
    return sc

def addswap(swm, w1, w2):
    h1 = w1
    h2 = w2
    if w1 in swm:
        h1 = swm[w1]
    if w2 in swm:
        h2 = swm[w2]
    swm[w1] = h2
    swm[w2] = h1

startswm = {}
swm = startswm.copy()
goodcon = defaultdict(lambda:[])
for i1, w1 in enumerate(ws):
    if w1 in initwire:
        continue
    for i2, w2 in enumerate(ws):
        if i2 <= i1:
            continue
        if w1==w2 or w2 in initwire or w2 in goodcon[w1]:
            continue
        setInput(0,0)
        swm = startswm.copy()
        addswap(swm, w1, w2)

        ret = [ev(w,swm) for w in finwire]
        if -1 not in ret:
            goodcon[w1].append(w2)

minsc = higheval(startswm)
minswm = startswm.copy()
swm = startswm.copy()
print(f"initial: {higheval({})}")
print(f"curr init: {higheval(startswm)}")
print(','.join(list(sorted(startswm.keys()))))
for i,w1 in enumerate(ws):
    if w1 in initwire:
        continue
    print(f"{i/len(ws)*100}%")
    print(f"minsc: {minsc}")
    print(minswm)
    for w2 in goodcon[w1]:
        swm = startswm.copy()
        addswap(swm, w1, w2)
        sc = higheval(swm)
        if sc < minsc:
            minsc = sc
            minswm = swm.copy()
            print(f"minsc: {minsc}")
            print(f"minswm: {minswm}")
print(f"minsc: {minsc}")
print(minswm)
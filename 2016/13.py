import numpy as np
from utils import bcolors

magic = 1362
xmax, ymax = 45, 45
cm = np.zeros(shape=(xmax, ymax))

for y in range(ymax):
    for x in range(xmax):
        binary = bin(x*x + 3*x + 2*x*y + y + y*y + magic)
        ones = binary[2:].count("1")
        if ones % 2 == 0:
            cm[x, y] = 0
        else:
            cm[x, y] = 1

part = 1
start = (1, 1)
end = (31, 39)
visited = {}
steps = 0
current = {start:None}

while True:
    new_pos = {}
    for c, prec in current.items():
        if c in visited:
            if visited[c][1] > steps:
                visited[c] = (prec, steps)
        else:
            visited[c] = (prec, steps)
            for s in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                pos = (c[0] + s[0], c[1] + s[1])
                if cm[pos[0], pos[1]] != 1 and pos[0]>= 0 and pos[1]>=0:
                    if pos not in new_pos:
                        new_pos[pos] = c
                
    current = new_pos
    if end in visited:
        print ("🎄Part 1: {}".format(visited[end][1]))
        break
    steps += 1
    if part == 2 and steps == 51:
        print ("🎁🎄Part 2: {}".format(len(visited)))
        break

path = [end]
prec = end
while True:
    if visited[prec][0] is not None:
        path.append(visited[prec][0])
        prec = visited[prec][0]
    else:
        break

for y in range(cm.shape[1]):
    for x in range(cm.shape[0]):
        if (x, y) in path:
            print(bcolors.RED+"O"+bcolors.ENDC, end='')
        elif cm[x, y] == 0:
            print (".", end='')
        else:
            print ("#", end='')
    print ()
print ()



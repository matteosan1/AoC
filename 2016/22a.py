from utils import readInput

nodes = {}
#size, used, avail

x = 0
y = 0
xmax  = 38
ymax = 28
lines = readInput("input_22.txt")
for l in lines[2:]:
    parts = l.split()
    nodes[(x, y)] = (int(parts[-4][:-1]), int(parts[-3][:-1]), int(parts[-2][:-1]))
    y += 1
    if y == 28:
        y = 0
        x += 1

pairs = []
for y in range(ymax):
    for x in range(xmax):
        m = (x, y)
        for y1 in range(ymax):
            for x1 in range(xmax):
                n = (x1, y1)
                if n == m:
                    continue
                if nodes[m][1] != 0:
                    if nodes[n][2] > nodes[m][1]:
                        pairs.append([m, n])

print ("🎄Part 1: {}".format(len(pairs)))


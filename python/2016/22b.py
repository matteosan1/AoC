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
        if m == (xmax-1, 0):
            print ("G", end='')
            continue
        if m == (0, 0):
            print ("!", end='')
            continue
        if nodes[m][1] == 0:
            print ("_", end='')
        elif nodes[m][0] < 100:
            print (".", end = '')
        else:
            print ("#", end = '')                        
    print ()

print ("🎁🎄Part 2: by hand")

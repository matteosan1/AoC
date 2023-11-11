from utils import readInput

m = {}
lines = readInput("input_22.txt")

for y, l in enumerate(lines):
    for x in range(len(lines[y])):
        if lines[y][x] == "#":
            m[(x, y)] = 1
        else:
            m[(x, y)] = 0

dirs = {0: (lambda x: (x[0], x[1]-1)),
        2: (lambda x: (x[0], x[1]+1)),
        3: (lambda x: (x[0]-1, x[1])),
        1: (lambda x: (x[0]+1, x[1]))}
        
infections = 0
dir = 0
pos = (x//2, y//2)

for burst in range(10000):
    if m[pos] == 1:
        dir = (dir+1)%4
        m[pos] = 0
    else:
        dir = (dir-1)%4
        m[pos] = 1
        infections += 1

    pos = dirs[dir](pos)
    m[pos] = m.setdefault(pos, 0)

print ("🎄Part 1: {}".format("".join(infections)))

from utils import readInput

m = {}
lines = readInput("input_22.txt")

for y, l in enumerate(lines):
    for x in range(len(lines[y])):
        if lines[y][x] == "#":
            m[(x, y)] = 2
        else:
            m[(x, y)] = 0

dirs = {0: (lambda x: (x[0], x[1]-1)),
        2: (lambda x: (x[0], x[1]+1)),
        3: (lambda x: (x[0]-1, x[1])),
        1: (lambda x: (x[0]+1, x[1]))}

# 0  clean
# 1 W
# 2 I
# 3 F

infections = 0
dir = 0
pos = (x//2, y//2)
for burst in range(10000000):
    if m[pos] == 0:
        dir = (dir-1)%4
    elif m[pos] == 1:
        pass
    elif m[pos] == 2:
        dir = (dir+1)%4
    elif m[pos] == 3:
        dir = (dir-2)%4
    else:
        import sys
        print ("PROBLEMA")
        sys.exit()
    
    m[pos] = (m[pos] + 1)%4
    if m[pos] == 2:
        infections += 1
    pos = dirs[dir](pos)
    m[pos] = m.setdefault(pos, 0)

print ("🎁🎄Part 2: {}".format("".join(infections)))
    

from utils import readInput

lines = readInput("input_20.txt")

for i in range(len(lines)):
    lines[i] = list(map(int, lines[i].split("-")))

blocked = []
for parts in sorted(lines):
    if len(blocked) == 0:
        blocked.append(parts)
    else:
        for i, b in enumerate(blocked):
            if b[0]-1 <= parts[0] <= b[1]+1:
                if parts[1] > b[1]:
                    blocked[i] = [b[0], parts[1]]
                break
            elif b[0]-1 <= parts[1] <= b[1]+1:
                if parts[0] < b[0]:
                    blocked[i] = [parts[0], b[1]]
                elif parts[0] < b[0] and parts[1] > b[1]:
                    blocked[i] = parts
                break
        else:
            blocked.append(parts)
print ("🎄Part 1: {}".format(blocked[0][1]+1))
        
allowed = 4294967296
for b in blocked:
    allowed -= b[1] - b[0] + 1

print ("🎁🎄Part 2: {}".format(allowed))

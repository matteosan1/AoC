lines = []
with open("input_1a.txt") as f:
    for l in f:
        lines.append(int(l.split("\n")[0]))

lines = sorted(lines)

for i in range(len(lines)):
    diff = 2020 - lines[i]
    for j in range(len(lines)-1, i, -1):
        if lines[j] < diff:
            diff2 = diff - lines[j]
            for y in range(j-1, i, -1):
                if lines[y] == diff2:
                    print (lines[i]*lines[j]*lines[y])
                    import sys
                    sys.exit()
                elif lines[y] < diff2:
                    break

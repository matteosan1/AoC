lines = []
with open("input_1a.txt") as f:
    for l in f:
        lines.append(int(l.split("\n")[0]))

lines = sorted(lines)

for i in range(len(lines)):
    diff = 2020 - lines[i]
    for j in range(len(lines)-1, 0, -1):
        if lines[j] == diff:
            print (lines[i]*lines[j])
            import sys
            sys.exit()
        elif lines[j] < diff:
            break

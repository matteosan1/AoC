from itertools import combinations

lines = []
with open("input_9a.txt") as f:
    for l in f:
        lines.append(int(l.split("\n")[0]))

step = 26
for i in range(len(lines)-step):
    code = lines[i:i+step]
    sums = ([code[c[0]] + code[c[1]] for c in combinations(range(step-1), 2)])
    if code[-1] not in sums:
        print (code)
        print (sums)
        print (code[-1])
        break
    #if i ==1:
    #    break

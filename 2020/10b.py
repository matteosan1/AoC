lines = []
with open("input_10a.txt") as f:
    for l in f:
        lines.append(int(l.split("\n")[0]))

comb = {2:2, 3:4, 4:7, 1:1, 0:1}
jolts = []
s = [0] + sorted(lines) + [max(lines) + 3]
for i in range(1, len(s)):
    diff = s[i] - s[i-1]
    jolts.append(diff)

print (jolts)
cons = []
c = 0
for i, j in enumerate(jolts):
    if  j == 1:
        c +=1
    else:
        cons.append(c)
        c = 0

print (cons)
tot = 1
for c in cons:
    tot *= comb[c]
print (tot)

lines = []
with open ("input_5a.txt") as f:
    for l in f:
        lines.append(l.split("\n")[0])

def rule(code, up=128):
    diff = up // 2
    for c in code:
        if c == 'F' or c == 'L':
            up -= diff
        diff //= 2
    return up - 1

ids = []
for l in lines:
    row = rule(l[:7])
    col = rule(l[7:], 8)
    ids.append(row*8+col)

seats = set(ids)
all = set(range(59, 905))
print (all-seats)

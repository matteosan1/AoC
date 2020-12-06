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
seats  = []
for l in lines:
    row = rule(l[:7])
    col = rule(l[7:], 8)
    ids.append(row*8+col)
    seats.append((col, row))

ids = set(ids)
all = set(range(59, 905))
print (all-ids)

for y in range(128):
    print ("{:3} ".format(y), end='')
    for x in range(8):
        if (x, y) in seats:
            print ("X", end="")
        else:
            print (".", end="")
        if x == 3:
            print (" ", end="")
    print ()

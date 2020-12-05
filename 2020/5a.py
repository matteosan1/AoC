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


#code = "BFFFBBFRRR" #: row 70, column 7, seat ID 567.
#code = "FFFBBBFRRR" #: row 14, column 7, seat ID 119.
#code = "BBFFBBFRLL" #:
#code = "FBFBBFFRLR"

maxID = 0
for l in lines:
    row = rule(l[:7])
    col = rule(l[7:], 8)
    id  = row*8+col
    if id > maxID:
        maxID = id

print (maxID)

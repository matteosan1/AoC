steps = []
with open("input_1.txt") as f:
    lines = f.readlines()
    for l in lines:
        ins = l.split("\n")[0].split(", ")

position = 0 + 0j
pos = [position]
direction = 0 + 1j
for i in ins:
    if i[0] == 'L':
        direction *= 1j
    else:
        direction *= -1j

    steps = int(i[1:])
    for _ in range(steps):
        position += direction
        if position not in pos:
            pos.append(position)
        else:
            res = (int(abs(position.real) + abs(position.imag)))
            print ("🎄Part 2: {}".format(res))
            import sys
            sys.exit()
res = (int(abs(position.real) + abs(position.imag)))
print ("🎄Part 1: {}".format(res))



mems = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"

part = 2
banks = list(map(int, mems.split()))
old = [banks]
cycles = [0]
size = len(banks)
steps = 0
while True:
    start = banks.index(max(banks))
    new_bank = list(banks)
    offset = start
    for i in range(banks[start]):
        new_bank[start] -= 1
        offset += 1
        offset %= size
        new_bank[offset] += 1

    steps += 1
    if new_bank not in old:
        old.append(new_bank)
        cycles.append(steps)
    else:
        break
    banks = new_bank

if part == 1:
    print ("🎄Part 1: {}".format(steps))
else:
    idx = old.index(new_bank)
    print ("🎁🎄Part 2: {}".format(steps-cycles[idx]))

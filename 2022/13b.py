from sympy.ntheory.modular import crt
import time
start_time = time.time()

busses = []
mods = []
with open("input_13a.txt") as f:
    i = 0
    for line in f:
        line = line.strip('\n').split(',')
        if i == 0:
            target = int(line[0])
            i += 1
            continue
        for j in range(0, len(line)):
            try:
                busses.append(int(line[j]))
                mods.append(j)
            except:
                pass

p2, mult = crt(busses, mods)
while p2 > 0:
    p2 -= mult
p2 *= -1

print('🎄 Part 2: {} 🎄'.format(p2))

print("\n--- %.7s secs ---" % (time.time() - start_time))
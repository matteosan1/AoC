import time
from utils import readInput

def loadInput():
    lines = [int(l) for l in readInput("input_10.txt")]
    jolts = []
    s = [0] + sorted(lines) + [max(lines) + 3]
    for i in range(1, len(s)):
        diff = s[i] - s[i-1]
        jolts.append(diff)
    return jolts

def part1(jolts):
    print ("🎄 Part 1: {}".format(jolts.count(1)*jolts.count(3)))

def part2(jolts):
    comb = {2:2, 3:4, 4:7, 1:1, 0:1}
    cons = []
    c = 0
    for i, j in enumerate(jolts):
        if  j == 1:
            c +=1
        else:
            cons.append(c)
            c = 0

    tot = 1
    for c in cons:
        tot *= comb[c]
    print ("🎄🎅 Part 2: {}".format(tot))

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 10        ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

from utils import readInput

timers = readInput("input_7.txt")
pos = list(map(int, timers[0].split(",")))

deltas = [sum([abs(p-i) for p in pos]) for i in range(min(pos), max(pos)+1)]
print ("🎄 Part 1: {}".format(min(deltas)))


from utils import readInput

def sumInt(n):
    return n*(n+1)//2

timers = readInput("input_7.txt")
pos = list(map(int, timers[0].split(",")))

deltas = [sum([sumInt(abs(p-i)) for p in pos]) for i in range(min(pos), max(pos)+1)]                                
print ("🎄🎅 Part 2: {}".format(min(deltas)))

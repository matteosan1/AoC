import time, math

from itertools import combinations
from functools import reduce

from utils import readInput

def loadInput():
    lines = readInput("instructions24a.txt")
    return list(map(int, lines))

def solve(inputs, parts):
    tot = sum(inputs)/parts
    def hasSum(lst, sub):
        for y in range(1, len(lst)):
            for x in (z for z in combinations(lst, y) if sum(z) == tot):
                if sub == 2:
                    return True
                elif sub < parts:
                    return hasSum(list(set(lst) - set(x)), sub - 1)
                elif hasSum(list(set(lst) - set(x)), sub - 1):
                    return math.prod(x)
    return hasSum(inputs, parts)

def part1(inputs):
    print (f"🎄 Part 1: {solve(inputs, 3)}")

def part2(inputs):
    print (f"🎄🎅 Part 2: {solve(inputs, 4)}")
    
if __name__ == "__main__":
    title = "Day 24: It Hangs in the Balance"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))

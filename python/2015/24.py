import time, math

from itertools import combinations
from functools import reduce

from utils import readInput

def loadInput():
    lines = readInput("instructions24a.txt")
    return list(map(int, lines))

def get_groups(lst, parts, tot, ng, g1=None):
    if g1 is None:
        y = 1
    else:
        y = len(g1[0])+1
    while y < len(lst)+1:
        for z in combinations(lst, y):
            if sum(z) == tot:
                if ng == parts:
                    entanglement = math.prod(z)
                    if g1 is not None:
                        if entanglement < g1[1]:
                            g1 = [z, entanglement, False]
                        else:
                            continue
                    else:
                        g1 = [z, entanglement, False]
                elif ng == 1:
                    g1[2] = True
                get_groups(list(set(lst) - set(z)), parts, tot, ng - 1, g1)                     
        if g1 is not None and g1[2]:
            break
        y += 1
    return g1
    
def solve(inputs, parts):
    tot = sum(inputs)/parts
    return get_groups(inputs, parts, tot, parts)
    
def part1(inputs):
    print (f"🎄 Part 1: {solve(inputs, 3)[1]}")

def part2(inputs):
    print (f"🎄🎅 Part 2: {solve(inputs, 4)[1]}")
    
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

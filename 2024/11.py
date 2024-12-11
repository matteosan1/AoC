import time

from functools import cache
from math import log10

from utils import readInput
                      
def loadInput():
    lines = readInput("input_11_prova.txt")
    #lines = readInput("input_11.txt")

    stones = list(map(int, lines[0].split()))
    return stones

@cache
def rules(s):
    if s == 0:
        return [1]
    oom = int(log10(s)+1)
    if oom != 0 and oom%2 == 0:
        s1 = s//10**(oom/2)
        s2 = s - s1*10**(oom/2)
        return  [int(s1), int(s2)]
    else:
        return  [int(s*2024)]

def blinking(vect, blinks):
    for _ in range(blinks):
        new_vect = {}
        for stone, i in vect.items():
            s = rules(stone)
            for item in s:
                new_vect[item] = new_vect.get(item, 0) + i
        vect = new_vect
    return sum(vect.values())

def part1(stones):
    length = 0
    for stone in stones:
        init = {stone: 1}
        length += blinking(init, 1000)        
    return length

def part2(stones):
    length = 0
    for stone in stones:
        init = {stone: 1}
        length += blinking(init, 75)
    return length
    
if __name__ == '__main__':
    title = "Day 11: Plutonian Pebbles"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

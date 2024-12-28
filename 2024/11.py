import time

from functools import cache
from math import log10

from utils import readInput
                      
def loadInput(filename: str) -> list[int]:
    lines = readInput("input_11.txt")

    stones = list(map(int, lines[0].split()))
    return stones

@cache
def rules(s: int):
    if s == 0:
        return [1]
    oom = int(log10(s)+1)
    if oom != 0 and oom%2 == 0:
        s1 = s//10**(oom/2)
        s2 = s - s1*10**(oom/2)
        return  [int(s1), int(s2)]
    else:
        return  [int(s*2024)]

def blinking(vect: dict[int, int], blinks: int):
    for _ in range(blinks):
        new_vect: dict[int, int] = {}
        for stone, i in vect.items():
            s = rules(stone)
            for item in s:
                new_vect[item] = new_vect.get(item, 0) + i
        vect = new_vect
    return sum(vect.values())

def part1(stones: list[int]):
    length = 0
    for stone in stones:
        length += blinking({stone: 1}, 25)
    print (f"🎄 Part 1: {length}", end="")
     
def part2(stones: list[int]):
    length = 0
    for stone in stones:
        length += blinking({stone: 1}, 75)
    print (f"🎄🎅 Part 2: {length}", end="")
    
if __name__ == '__main__':
    title = "Day 11: Plutonian Pebbles"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_11.txt")

    t0 = time.time()
    res1 = part1(inputs)
    print (f" - {time.time()-t0:.5f}")
    
    t0 = time.time()
    res2 = part2(inputs)
    print (f" - {time.time()-t0:.5f}")

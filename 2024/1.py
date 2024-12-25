import time

from collections import Counter

from utils import readInput

def loadInput(filename: str) -> tuple[list[int], list[int]]:
    lines = readInput(filename)
    ids: list[tuple[int, ...]] = []
    for l in lines:
        ids.append(tuple(map(int, l.split())))
    return tuple(zip(*ids))

def part1(id1: list[int], id2: list[int]) -> None:
    print (f"🎄 Part 1: {sum([abs(x-y)for x, y in zip(sorted(id1), sorted(id2))])}")

def part2(id1: list[int], id2: list[int]) -> None:
    tot = 0
    counts = Counter(id2)
    for n in id1:
        tot += n*counts[n]
    print (f"🎄🎅 Part 2: {tot}")

if __name__ == "__main__":
    title = "Day 1: Historian Hysteria"
    sub = "⛄"*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs1, inputs2 = loadInput("input_1.txt")
    
    t0 = time.time()
    part1(inputs1, inputs2)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs1, inputs2)
    print ("Time: {:.5f}".format(time.time()-t0))

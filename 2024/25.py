import time

from utils import readInputWithBlank

def loadInput(filename: str) -> tuple[list[list[int]], list[list[int]]]:
    lines = readInputWithBlank(filename)

    locks: list[list[int]] = []
    keys: list[list[int]] = []
    l = 0
    while l < len(lines):
        if lines[l] == "":
            l += 1
        else:
            if lines[l][0] == "#":
                temp = [0 for _ in range(len(lines[l]))]
                for i in range(l+1, l+7):
                    for j in range(len(lines[i])):
                        temp[j] += 1 if lines[i][j] == "#" else 0
                locks.append(temp)
            else:
                temp = [0 for _ in range(len(lines[l]))]
                for i in range(l, l+6):
                    for j in range(len(lines[i])):
                        temp[j] += 1 if lines[i][j] == "#" else 0
                keys.append(temp)
            l += 7
    return locks, keys

def part1(locks: list[list[int]], keys: list[list[int]]) -> None:
    matches = 0
    for lock in locks:
        for key in keys:
            if all([key[i]+lock[i] <= 5 for i in range(len(lock))]):
                matches += 1
    print (f"🎄 Part 1: {matches}", end='')
    
if __name__ == '__main__':
    title = "Day 25: Code Chronicle"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_25.txt")
    
    t0 = time.time()
    part1(*inputs)
    print (" - {:.5f}".format(time.time()-t0))

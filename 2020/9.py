import time
from utils import readInput
from itertools import combinations

def loadInput():
    lines = readInput("input_9.txt")    
    return [int(n) for n in lines]

def part1(numbers):
    
    step = 26
    for i in range(len(numbers)-step):
        code = numbers[i:i+step]
        sums = ([code[c[0]] + code[c[1]] for c in combinations(range(step-1), 2)])
        if code[-1] not in sums:
            print ("🎄 Part 1: {}".format(code[-1]))
            break
            

def part2(numbers):
    target = 10884537
    start = 0
    end = 1
    sums = sum(numbers[start:end])
    while sums != target:
        if sums < target:
            end += 1
        elif sums > target:
            start += 1
        sums = sum(numbers[start:end])
    print ("🎄🎅 Part 2: {}".format(min(numbers[start:end]) + max(numbers[start:end])))

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 9         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

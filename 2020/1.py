import time
from utils import readInput
from itertools import combinations
from math import prod

def loadInput():
    lines = readInput("input_1.txt")
    expenses = [int(e) for e in lines]
    return expenses

def part1(expenses):
    for c in combinations(expenses, 2):
        if sum(c) == 2020:
            print ("🎄 Part 1: {}".format(prod(c)))
            break

def part2(expenses):
    for c in combinations(expenses, 3):
        if sum(c) == 2020:
            print ("🎄🎅 Part 2: {}".format(prod(c)))
            break


print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 1         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

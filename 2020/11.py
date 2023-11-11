import time
from utils import readInput

def loadInput():
    lines = readInput("prova.txt")
    #lines = readInput("input_11.txt")

    return

def part1():
    pass
    #print ("🎄 Part 1: {}".format())

def part2():
    pass
    #print ("🎄🎅 Part 2: {}".format())

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 11         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

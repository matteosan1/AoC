import time
from utils import readInput

def loadInput():
    lines = readInput("prova.txt")
    #lines = readInput("input_DAY.txt")

    return lines

def part1(inputs):
    pass
    #print (f"🎄 Part 1: {}")

def part2(inputs):
    pass
    #print (f"🎄🎅 Part 2: {}")

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day DAY         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print (f"Time: {time.time()-t0:.5f}")

t0 = time.time()
part2(inputs)
print (f"Time: {time.time()-t0:.5f}")
import time
from utils import readInput

def loadInput():
    lines = readInput("prova.txt")
    #lines = readInput("input_12.txt")
    return lines

def part1(inputs):
    pass
    #return res1

def part2(inputs):
    pass
    #return res2

if __name__ == '__main__':
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    print("⛄        Day 12         ⛄")
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

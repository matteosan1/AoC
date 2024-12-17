import timeit, copy

from utils import readInput

def loadInput():
    lines = readInput("input_18_prova.txt")
    #lines = readInput("input_18.txt")
    return intcode

def part1(intcode):
    print (f"🎄 Part 1: {0}")

def part2(intcode):
    print (f"🎄🎅 Part 2: {0}")

if __name__ == '__main__':
    title = "Day 18: "
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    t2 = timeit.timeit(lambda: part2(inputs), number=1)
    print (f"{t2*1000:.3f} ms")


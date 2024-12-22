import timeit

from math import floor

from utils import readInput

def loadInput():
    lines = readInput("input_23_prova.txt")
    #lines = readInput("input_23.txt")
    return list(map(int, lines))

def part1(secret_numbers):
    secret_sum = 0
    print (f"🎄 Part 1: {secret_sum}")
    
def part2(secret_numbers):
    x = max(totals.values())
    print (f"🎄🎅 Part 2: {x}")

if __name__ == '__main__':
    title = "Day 23: "
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    # t2 = timeit.timeit(lambda: part2(inputs), number=1)
    # print (f"{t2*1000:.3f} ms")

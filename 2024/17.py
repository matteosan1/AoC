import timeit, heapq

from utils import readInput

def loadInput():
    lines = readInput("input_17_prova.txt")
    #lines = readInput("input_17.txt")
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            c = (x, y)
            if lines[y][x] == "#":
                pitch[c] = 1
            elif lines[y][x] == "S":
                pitch[c] = 0
                start = c
            elif lines[y][x] == "E":
                target = c
                pitch[c] = 0
            elif lines[y][x] == ".":
                pitch[c] = 0
    return 

def part1(pitch, start, target):
    print (f"🎄 Part 1: {0}")
    
def part2():
    print (f"🎄🎅 Part 2: {0}")

if __name__ == '__main__':
    title = "Day 17: "
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(*inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    t2 = timeit.timeit(lambda: part2(*inputs), number=1)
    print (f"{t2*1000:.3f} ms")


import time
from utils import readInput

def loadInput():
    lines = readInput("instructions1a.txt")
    return lines

def part1(lines):
    char = 0
    floor = 0
    for c in lines[0]:
        if c == "(":
            char += 1
            floor += 1
        elif c == ")":
            char += 1
            floor -= 1

    print (f"🎄 Part 1: {floor}")

def part2(lines):
    char = 0
    floor = 0
    for c in lines[0]:
        if c == "(":
            char += 1
            floor += 1
        elif c == ")":
            char += 1
            floor -= 1
        if floor == -1:
            print (f"🎄🎅 Part 2: {char}")
            return

if __name__ == "__main__":
    title = "Day 1: Not Quite Lisp"
    sub = "-"*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))

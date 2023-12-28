import time
from utils import readInput

def loadInput():
    lines = readInput("instructions3a.txt")
    return lines

def part1(lines):
    presents = {(0,0): 1}
    pos = (0,0)
    for c in lines[0]:
        if c == "^":
            pos = (pos[0], pos[1]+1)
        elif c == "v":
            pos = (pos[0], pos[1]-1)
        elif c == "<":
            pos = (pos[0]-1, pos[1])
        elif c == ">":
            pos = (pos[0]+1, pos[1])
        presents[pos] = presents.setdefault(pos, 0) + 1

    print (f"🎄 Part 1: {len(presents)}")

def part2(lines):
    presents = {(0,0): 2}
    pos = [(0,0), (0,0)]
    isSanta = 0
    for c in lines[0]:
        if c == "^":
            pos[isSanta] = (pos[isSanta][0], pos[isSanta][1]+1)
        elif c == "v":
            pos[isSanta] = (pos[isSanta][0], pos[isSanta][1]-1)
        elif c == "<":
            pos[isSanta] = (pos[isSanta][0]-1, pos[isSanta][1])
        elif c == ">":
            pos[isSanta] = (pos[isSanta][0]+1, pos[isSanta][1])
        presents[pos[isSanta]] = presents.setdefault(pos[isSanta], 0) + 1
        isSanta = 1 - isSanta

    print (f"🎄🎅 Part 2: {len(presents)}")
    
if __name__ == "__main__":
    title = "Day 3: Perfectly Spherical Houses in a Vacuum"
    sub = "-"*(len(title)+2)

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

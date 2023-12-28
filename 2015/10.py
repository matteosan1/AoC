import time

from itertools import groupby

def loadInput():
    return "1321131112"

def look_and_say(inp):
    return ''.join(str(len(list(v))) + k for k, v in groupby(inp))

def part1(p1):
    for steps in range(50):
        p1 = look_and_say(p1)
        if steps == 39:
            break
    print (f"🎄 Part 1: {len(p1)}")

def part2(p1):
    for steps in range(50):
        p1 = look_and_say(p1)
    print (f"🎄🎅 Part 2: {len(p1)}")
    
if __name__ == "__main__":
    title = "Day 10: Elves Look, Elves Say"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    inputs = loadInput()
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))


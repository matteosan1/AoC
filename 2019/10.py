import time, numpy as np

from utils import readInput

def loadInput():
    lines = readInput("prova.txt")
    asteroids = {}
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c  == "#":
                asteroids[(x, y)] = 1
    return asteroids

def part1(asteroids):
    for k1 in asteroids:
        for k2 in asteroids:
            if k1 == k2:
                continue
            
    print (f"ðŸŽ„ Part 1: {0}")

def part2(image):
    print (f"ðŸŽ„ðŸŽ… Part 2:")

if __name__ == "__main__":
    title = "Day 10: Monitoring Station"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    #t0 = time.time()
    #part2(inputs)
    #print ("Time: {:.5f}".format(time.time()-t0))

import time

from utils import readInput

def loadInput():
    dimensions = []
    lines = readInput("instructions17a.txt")
    for l in lines:
        dimensions.append(int(l))
    return dimensions

def part1(dimensions):
    dist = dict()
    for mask in range(1, 1<<len(dimensions)):
        p = [d for i,d in enumerate(dimensions) if (mask & (1 << i)) > 0]
        if sum(p) == 150:
            dist[len(p)] = dist.setdefault(len(p), 0) + 1

    print (f"🎄 Part 1: {sum(dist.values())}")
    return dist

def part2(dist):
    print (f"🎄🎅 Part 2: {dist[min(dist.keys())]}")
    
if __name__ == "__main__":
    title = "Day 17: No Such Thing as Too Much"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    dist = part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(dist)
    print ("Time: {:.5f}".format(time.time()-t0))


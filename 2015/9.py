import time, math

from itertools import permutations

from utils import readInput

def loadInput():
    lines = readInput("instructions9a.txt")
    distances = {}

    for d in lines:
        items = d.split(" ")
        distances.setdefault(items[0], {}).update({items[2]:int(items[4])})
        distances.setdefault(items[2], {}).update({items[0]:int(items[4])})
    return distances

def part1(distances):
    min_dist = math.inf
    for p in permutations(distances.keys()):
        dist = 0
        for i in range(len(p)-1):
            dist += distances[p[i]][p[i+1]]

        if dist < min_dist:
            min_dist = dist
            
    print (f"🎄 Part 1: {min_dist}")


def part2(distances):
    max_dist = 0
    for p in permutations(distances.keys()):
        dist = 0
        for i in range(len(p)-1):
            dist += distances[p[i]][p[i+1]]

        if dist > max_dist:
            max_dist = dist
            
    print (f"🎄🎅 Part 2: {max_dist}")

if __name__ == "__main__":
    title = "Day 9: All in a Single Night"
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

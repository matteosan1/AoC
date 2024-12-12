import time

#from functools import cache
from math import log10

from utils import readInput
                      
def loadInput():
    lines = readInput("input_12_prova.txt")
    #lines = readInput("input_12.txt")

    garden = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            garden[complex(x, y)] = lines[y][x]
    return garden

dirs = {0:complex(0, -1), 1:complex(1, 0), 2:complex(0, 1), 3:complex(-1, 0)}

def get_regions(garden):
    gardens = {}
    for pos, gtype in garden.items():
        gardens.setdefault(gtype, []).append(pos)

    regions = {}
    for gtype in gardens.keys():
        regions[gtype] = []
        visited = []
        for pos in gardens[gtype]:
            group = []
            if pos in visited:
                continue
            neighs = [pos]
            visited.append(pos)
            while len(neighs) != 0:
                spot = neighs.pop()
                group.append(spot)
                for d in dirs.values():
                    new_spot = spot + d
                    if new_spot in garden:
                        if new_spot not in visited:
                            if garden[new_spot] == gtype:
                                visited.append(new_spot)
                                neighs.append(new_spot)
            regions[gtype].append(group)                        
            group = []
    return regions

def part1(garden):
    regions = get_regions(garden)
    cost = 0
    for k, v in regions.items():
        for subregion in v:
            area = len(subregion)
            perimeter = 0
            for spot in subregion:
                perimeter += sum([spot+d not in subregion for d in dirs.values()])
            cost += area*perimeter
    return cost

def complex_lex_key(z):
  return (z.real, z.imag)

def cheap_perimeter(region):
    sorted_region = sorted(region, key=complex_lex_key)
    print (sorted_region)
    sides = []
    #current_side = [sorted_region[0]]
    start = sorted_region[0]
    dir = sorted_region[1] - sorted_region[0]
    for i in range(1, len(sorted_region)):
        print (sorted_region[i] - sorted_region[i-1])
        if sorted_region[i].real == sorted_region[i-1].real or sorted_region[i].imag == sorted_region[i-1].imag:
            current_side.append(sorted_region[i])
        else:
            sides.append(current_side)
            current_side = [sorted_region[i]]
    sides.append(current_side)  # Add the last side
    print (len(sides), sides)
    return 0

def part2(garden):
    regions = get_regions(garden)
    cost = 0
    for k, v in regions.items():
        for subregion in v:
            area = len(subregion)
            perimeter = cheap_perimeter(subregion)
            cost += area*perimeter
    return cost

if __name__ == '__main__':
    title = "Day 12: Garden Groups"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

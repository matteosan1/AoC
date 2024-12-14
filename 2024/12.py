import time

from math import log10

from utils import readInput

# PROVARE PART1 CON FLOODFILL RICORSIVO  
# SPEED UP parte 2
def loadInput():
    #lines = readInput("input_12_prova.txt")
    lines = readInput("input_12.txt")

    garden = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            garden[complex(x, y)] = lines[y][x]
    return garden

dirs = {0: complex(0, -1), 1: complex(1, 0), 2: complex(0, 1), 3: complex(-1, 0)}

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
                    if new_spot in garden and new_spot not in visited and garden[new_spot] == gtype:
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
    return cost, regions

full_dirs = { 0: complex(0,-1), 2: complex(1,0), 4: complex(0,1), 6: complex(-1,0),
              1: complex(1,-1), # NE
              3: complex(1,1), # SE
              5: complex(-1,1), # SW
              7: complex(-1,-1) # NW
            }

def count_corners(pos, region):
    corners = 0
    adjacent = [False for _ in range(8)]
    for i, d in full_dirs.items():
        if pos+d in region:
            adjacent[i] = True

    if (not adjacent[0] and not adjacent[2] and not adjacent[4] and not adjacent[6]): 
        corners += 4
        
    # pokey nodes (touches zone on just 1 side)
    if (adjacent[0] and not adjacent[2] and not adjacent[4] and not adjacent[6]):
        corners += 2
    if (adjacent[2] and not adjacent[0] and not adjacent[4] and not adjacent[6]):
        corners += 2
    if (adjacent[4] and not adjacent[2] and not adjacent[0] and not adjacent[6]):
        corners += 2
    if (adjacent[6] and not adjacent[2] and not adjacent[4] and not adjacent[0]):
        corners += 2

    # convex corners
    if (adjacent[4] and adjacent[2] and not adjacent[0] and not adjacent[6]):
       corners += 1
    if (adjacent[4] and adjacent[6] and not adjacent[0] and not adjacent[2]):
       corners += 1
    if (adjacent[0] and adjacent[2] and not adjacent[4] and not adjacent[6]):
       corners += 1
    if (adjacent[0] and adjacent[6] and not adjacent[4] and not adjacent[2]):
       corners += 1

    # concave corners
    if (adjacent[2] and adjacent[0]  and not adjacent[1]):
       corners += 1
    if (adjacent[2] and adjacent[4]  and not adjacent[3]):
       corners += 1
    if (adjacent[6] and adjacent[0]  and not adjacent[7]):
       corners += 1
    if (adjacent[6] and adjacent[4] and not adjacent[5]): 
       corners+=1
    return corners

def part2(regions):
    #regions = get_regions(garden)
    cost = 0
    for k, v in regions.items():
        for subregion in v:
            area = len(subregion)
            perimeter = 0 
            for pos in subregion:
                perimeter += count_corners(pos, subregion)
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
    res1, regions = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(regions)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

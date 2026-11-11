import time

from utils import readInput, DIRECTIONS

dirs = {i:d for i, d in enumerate(DIRECTIONS)}

def loadInput(filename: str) -> list[set[complex]]:
    lines = readInput(filename)
    gardens: dict[complex, str] = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            gardens[complex(x, y)] = lines[y][x]
    regions = get_regions(gardens)
    return regions

def floodfill(gardens:dict[complex, str], pos: complex, 
              region: set[complex], visited: set[complex]) -> set[complex]:
    if pos not in visited:
        visited.add(pos)
        region.add(pos)
        for d in dirs.values():
            new_pos = pos + d
            if gardens.get(new_pos, "") == gardens[pos]:
                floodfill(gardens, new_pos, region, visited)
    return region

def get_regions(gardens: dict[complex, str]) -> list[set[complex]]:
    visited: set[complex] = set([])
    return [floodfill(gardens, pos, set(), visited) for pos in gardens if pos not in visited]

def part1(regions: list[set[complex]]):
    cost = 0
    for region in regions:
        area = len(region)
        perimeter = 0
        for spot in region:
            perimeter += sum([spot+d not in region for d in dirs.values()])
        cost += area*perimeter
    print (f"🎄 Part 1: {cost}", end='')

full_dirs = { 0: complex(0,-1), 2: complex(1,0), 4: complex(0,1), 6: complex(-1,0),
              1: complex(1,-1), # NE
              3: complex(1,1), # SE
              5: complex(-1,1), # SW
              7: complex(-1,-1) # NW
            }

def count_corners(pos: complex, region: set[complex]) -> int:
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

def part2(regions: list[set[complex]]):
    cost = 0
    for region in regions:
        area = len(region)
        perimeter = 0 
        for pos in region:
            perimeter += count_corners(pos, region)
        cost += area*perimeter
    print (f"🎄🎅 Part 2: {cost}", end='')

if __name__ == '__main__':
    title = "Day 12: Garden Groups"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_12.txt")
    
    t0 = time.time()
    part1(inputs)
    print (f" - {time.time()-t0:.5f}")
    
    t0 = time.time()
    part2(inputs)
    print (f" - {time.time()-t0:.5f}")

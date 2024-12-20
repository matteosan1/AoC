import timeit, heapq

from utils import readInput, bcolors

DIRECTIONS = [complex(0, 1), complex(1, 0), complex(0, -1), complex(-1, 0)]

def loadInput():
    lines = readInput("input_20_prova.txt")
    #lines = readInput("input_20.txt")

    racetrack = {}
    for l in lines:
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                c = complex(x, y)
                if lines[y][x] == "#":
                    racetrack[c] = 1
                elif lines[y][x] == "S":
                    start = c
                    racetrack[c] = 0
                elif lines[y][x] == "E":
                    end = c
                    racetrack[c] = 0
                else:
                    racetrack[c] = 0
    return racetrack, start, end

def is_valid(grid, c):
    return grid.get(c, 1) != 1

def get_neighbors(grid, c, cheated, cheat):
    neighbors = []
    for dc in DIRECTIONS:
        nc = c + dc
        if is_valid(grid, nc):
            neighbors.append((nc, cheated))
        if cheat and not cheated:
            nc2 = c + 2*dc
            if is_valid(grid, nc2):
                neighbors.append((nc2, True))
    return neighbors

def solve(grid, start, target, cheat=False, get_path=False):
    q = [(0, i:=0, start, False)]
    visited = set()
    #predecessors = {}
    costs = []
    while q:
        cost, _, c, cheated = heapq.heappop(q)
        if (c, cheated) in visited:
            continue
        visited.add((c, cheated))

        if c == target:
            if not get_path:
                costs.append(cost)
                continue
                #return cost, None
            # else:
            #     path = []
            #     current = c
            #     while current:
            #         path.append(current)
            #         current = predecessors.get(current)
            #     return cost, path[::-1]

        for nc in get_neighbors(grid, c, cheated, cheat):
            if nc not in visited:
                new_cost = cost + 1 + int(nc[1])*1
                heapq.heappush(q, (new_cost, i:=i+1, nc[0], nc[1]))
                #predecessors[(nc, cheated)] = c
    return costs
    #return -1, None

def part1(racetrack, start, end):
    #cost, path = solve(racetrack, start, end, get_path=True)
    #draw(racetrack, path)
    benchmark = min(solve(racetrack, start, end, get_path=False))
    print (benchmark)
    costs = solve(racetrack, start, end, cheat=True, get_path=False)
    print (costs)
    print (f"🎄 Part 1: {0}")

def part2(bytes):
    print (f"🎄🎅 Part 2: {0}")

def draw(memory, sits=None, width=None):
    print("")
    if width is None:
        xmax = int(max([c.real for c in memory]))+1
        ymax = int(max([c.imag for c in memory]))+1
    else:
        xmax = ymax = width
    for y in range(ymax):
        for x in range(xmax):
            c = complex(x, y)
            if sits is not None and c in sits:
                print (bcolors.RED + "O" + bcolors.ENDC, end="")
            elif memory[c] == 1:
                print ("#", end='')
            elif memory[c] == 0:
                print (".", end='')
        print ("")

if __name__ == '__main__':
    title = "Day 20: Race Condition"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(*inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    t2 = timeit.timeit(lambda: part2(inputs), number=1)
    print (f"{t2*1000:.3f} ms")

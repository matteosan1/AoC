import timeit, heapq

from utils import readInput, bcolors

DIRECTIONS = [complex(0, 1), complex(1, 0), complex(0, -1), complex(-1, 0)]

def loadInput():
    #lines = readInput("input_18_prova.txt")
    lines = readInput("input_18.txt")
    bytes = []
    for l in lines:
        bytes.append(complex(*(map(int, l.split(",")))))
    return bytes

def simulate_falling(bytes, nbytes, width):
    memory = {}

    for y in range(width):
        for x in range(width):
            c = complex(x, y)
            if c in bytes[:nbytes]:
                memory[c] = 1
            else:
                memory[c] = 0
    return memory                       

def is_valid(grid, c):
    return grid.get(c, 1) != 1

def get_neighbors(grid, c, new_walls):
    neighbors = []
    for dc in DIRECTIONS:
        nc = c + dc
        if new_walls is None:
            if is_valid(grid, nc):
                neighbors.append(nc)
        else:
            if is_valid(grid, nc) and not nc in new_walls:
                neighbors.append(nc)
    return neighbors

def solve(grid, width, new_walls=None, get_path=False):
    start = 0
    target = complex(width-1, width-1)
    q = [(0, i:=0, start)]
    visited = set()
    predecessors = {}

    while q:
        cost, _, c = heapq.heappop(q)
        if c in visited:
            continue
        visited.add(c)

        if c == target:
            if not get_path:
                return cost, None
            else:
                path = []
                current = c
                while current:
                    path.append(current)
                    current = predecessors.get(current)
                return cost, path[::-1]

        for nc in get_neighbors(grid, c, new_walls):
            if nc not in visited:
                new_cost = cost + 1
                heapq.heappush(q, (new_cost, i:=i+1, nc))
                predecessors[nc] = c
    return -1, None

def part1(bytes):
    nbytes = 1024
    width = 71
    memory = simulate_falling(bytes, nbytes, width)
    cost, path = solve(memory, width, get_path=True)
    draw(memory, path, width)
    print (f"🎄 Part 1: {cost}")

def part2(bytes):
    width = 71
    memory = simulate_falling(bytes, 1024, width)
    low = 1024
    high = len(bytes) - 1

    path = None
    while low <= high:
        mid = (low + high) // 2
        if path is not None and bytes[mid-1] not in path:
            low += 1
            continue

        cost, path = solve(memory, width, new_walls=bytes[1024:mid], get_path=True)

        if cost != -1:
            low = mid + 1
        else:
            if mid == low or solve(memory, width, new_walls=bytes[1024:mid-1])[0] != -1:
                break
            else:
                high = mid - 1
    #draw(memory, path)
    print (f"🎄🎅 Part 2: {bytes[mid-1]}")

def draw(memory, sits=None, width=None):
    print("")
    if width is None:
        xmax = int(max([c[0] for c in memory]))+1
        ymax = int(max([c[1] for c in memory]))+1
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
    title = "Day 18: RAM Run"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    t2 = timeit.timeit(lambda: part2(inputs), number=1)
    print (f"{t2*1000:.3f} ms")

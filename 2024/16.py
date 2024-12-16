import timeit, heapq, copy

from utils import readInput

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def loadInput():
    #lines = readInput("input_16_prova.txt")
    lines = readInput("input_16.txt")
    pitch = {}
    start = None
    target = None
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            c = (x, y)
            if lines[y][x] == "#":
                pitch[c] = 1
            elif lines[y][x] == "S":
                pitch[c] = 0
                start = c
            elif lines[y][x] == "E":
                target = c
                pitch[c] = 0
            elif lines[y][x] == ".":
                pitch[c] = 0
    #draw(pitch, start, target)                       
    return pitch, start, target

def is_valid(grid, c):
    return c in grid and grid[c] != 1

def get_neighbors(grid, c, direction):
    neighbors = []
    for idc, dc in enumerate(DIRECTIONS):
        if dc == (-DIRECTIONS[direction][0], -DIRECTIONS[direction][1]):
            continue
        nc = (c[0] + dc[0], c[1] + dc[1])
        if is_valid(grid, nc):
            if dc == DIRECTIONS[direction]: 
                neighbors.append((nc, direction, 1))
            else:
                neighbors.append((nc, idc, 1001))
    return neighbors

def solve(grid, start, target):
    q = [(0, start, 1)]
    visited = set()
    predecessors = {}

    while q:
        cost, c, direction = heapq.heappop(q)
        if (c, direction) in visited:
            continue
        visited.add((c, direction))

        if c == target:
            path = []
            current = (c, direction)
            while current:
                path.append((current[0],current[1]))
                current = predecessors.get(current)
            return cost, path[::-1]

        for nc, nd, move_cost in get_neighbors(grid, c, direction):
            neighbor = (nc, nd)
            if neighbor not in visited:
                new_cost = cost + move_cost
                heapq.heappush(q, (new_cost, nc, nd))
                predecessors[neighbor] = (c, direction)
    return -1, None

def part1(pitch, start, target):
    cost, path = solve(pitch, start, target)
    #draw(pitch, path)
    print (f"🎄 Part 1: {cost}")

def solve2(grid, start, target):
    DIRECTIONS = set([(0, 1), (1, 0), (0, -1), (-1, 0)])
    q = [(0, start, (1, 0), set())]  # score, position, direction, visited tiles
    seen_states = {
        pos: {direction: {"score": float("inf"), "tiles": set()} for direction in DIRECTIONS}
        for pos in grid.keys()
    }
    while q:
        score, coord, direction, tiles = heapq.heappop(q)
        allowed = DIRECTIONS - {(-direction[0], -direction[1])}  # avoid reversing direction
        for dc in allowed:
            new_coord = (coord[0] + dc[0], coord[1] + dc[1])
            if not is_valid(grid, new_coord):
                continue
            new_score = score + 1 + (1000 if dc != direction else 0)
            state = seen_states[new_coord][dc]
            if new_score > state["score"]:
                continue
            new_tiles = tiles | {new_coord}
            state["score"] = new_score
            if new_score < state["score"]:
                state["tiles"] = new_tiles
            elif new_score == state["score"]:
                state["tiles"] |= new_tiles        
            heapq.heappush(q, (new_score, new_coord, dc, state["tiles"]))
    return seen_states
    
def part2(pitch, start, target):
    visited = solve2(pitch, start, target)
    min_direction = min(visited[target].values(), key=lambda d: d["score"])
    #draw(pitch, min_direction['tiles'])
    print (f"🎄🎅 Part 2: {len(min_direction["tiles"]) + 1}")

def draw(pitch, sits):
    xmax = int(max([c[0] for c in pitch]))+1
    ymax = int(max([c[1] for c in pitch]))+1
    print ( xmax, ymax)
    #points = {c[0]:c[1] for c in sits}
    dirs = ['v','>','^','<']
    for y in range(ymax):
        for x in range(xmax):
            c = (x, y)
            if c in sits:
                #print (dirs[points[c]], end='')
                print ("O", end='')
            elif pitch[c] == 1:
                print ("#", end='')
            elif pitch[c] == 0:
                print (".", end='')
        print ("")

if __name__ == '__main__':
    title = "Day 16: Reindeer Maze"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(*inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    t2 = timeit.timeit(lambda: part2(*inputs), number=1)
    print (f"{t2*1000:.3f} ms")


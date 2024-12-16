import timeit, heapq, copy

from utils import readInput

def loadInput():
    lines = readInput("input_16_prova.txt")
    #lines = readInput("input_16.txt")
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

def draw(pitch, start=None, target=None):
    xmax = int(max([c[0] for c in pitch]))+1
    ymax = int(max([c[1] for c in pitch]))+1
    for y in range(ymax):
        for x in range(xmax):
            c = (x, y)
            if pitch[c] == 1:
                print ("#", end='')
            elif c == start:
                print ("S", end='')
            elif c == target:
                print ("E", end='')    
            elif pitch[c] == 0:
                print (".", end='')
        print ("")

def is_valid(grid, c):
    return c in grid and grid[c] != 1

def get_neighbors(grid, c, direction):
    neighbors = []
    # row, column
    dc = [(0, 1), (1, 0), (0, -1), (-1, 0)][direction]
    nc = (c[0] + dc[0], c[1] + dc[1])
    if is_valid(grid, nc):
        neighbors.append((nc, direction, 1))
    neighbors.append((c, (direction + 1) % 4, 1000))
    neighbors.append((c, (direction - 1) % 4, 1000))
    return neighbors

def solve(grid, start, target):
    q = [(0, start, 0)]
    visited = set()
    predecessors = {}  # Store predecessors (parent nodes)

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
                predecessors[neighbor] = (c, direction) # Store the predecessor
    return -1, None  # No path found

def part1(pitch, start, target):
    cost, path = solve(pitch, start, target)
    print (f"🎄 Part 1: {cost}")

def part2(inputs):
    print (f"🎄🎅 Part 2: {0}")

def draw2(pitch, sits):
    xmax = int(max([c[0] for c in pitch]))+1
    ymax = int(max([c[1] for c in pitch]))+1
    points = {c[0]:c[1] for c in sits}
    dirs = ['v','>','^','<']
    for y in range(ymax):
        for x in range(xmax):
            c = (x, y)
            if c in points:
                print (dirs[points[c]], end='')
            elif pitch[c] == 1:
                print ("#", end='')
            elif pitch[c] == 0:
                print (".", end='')
        print ("")

def solve_with_path(grid, start, target):
    # rows = len(grid)
    # cols = len(grid[0])
    # start_row, start_col = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'S')
    # end_row, end_col = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'E')

    def is_valid(grid, c):
        #return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#'
        return c in grid and grid[c] != 1

    def get_neighbors(grid, c, direction):
        dc = [(0, 1), (1, 0), (0, -1), (-1, 0)][direction]
        nc = (c[0] + dc[0], c[1]+dc[1])
        neighbors = []
        if is_valid(grid, nc):
            neighbors.append((nc, direction, 1))
        neighbors.append((c, (direction + 1) % 4, 1000))
        neighbors.append((c, (direction - 1 + 4) % 4, 1000))
        return neighbors

    q = [(0, start, 0)]
    visited = set()
    predecessors = {}  # Store predecessors (parent nodes)

    while q:
        cost, c, direction = heapq.heappop(q)

        if (c, direction) in visited:
            continue
        visited.add((c, direction))

        if c == target: # r == end_row and c == end_col:
            # Reconstruct the path
            path = []
            current = (c, direction)
            while current:
                path.append((current[0],current[1]))
                current = predecessors.get(current)
            return cost, path[::-1] # Reverse the path to get it from start to end

        for nc, nd, move_cost in get_neighbors(grid, c, direction):
            neighbor = (nc, nd)
            if neighbor not in visited:
                new_cost = cost + move_cost
                heapq.heappush(q, (new_cost, nc, nd))
                predecessors[neighbor] = (c, direction) # Store the predecessor

    return -1, None  # No path found

if __name__ == '__main__':
    title = "Day 16: Reindeer Maze"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    #t1 = timeit.timeit(lambda: part1(*inputs), number=1)
    #print (f"{t1*1000:.3f} ms")
    res = (solve_with_path(*inputs))
    print (res[0])
    draw2(inputs[0], res[1])
    # t2 = timeit.timeit(lambda: part2(*inputs), number=1)
    # print (f"{t2*1000:.3f} ms")


# # Example usage:
# with open("input_16.txt", "r") as f:
#     grid = [list(line.strip()) for line in f]

# cost, path = solve_with_path(grid)

# if path:
#     print(f"Lowest Cost: {cost}")
#     print(f"Best Path: {path}")
# else:
#     print("No path found.")
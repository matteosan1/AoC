import heapq, copy

def solve_a_star(grid):
    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'S')
    end_row, end_col = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'E')

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#'

    def get_neighbors(r, c, direction):
        dr, dc = [(0, 1), (1, 0), (0, -1), (-1, 0)][direction]
        nr, nc = r + dr, c + dc
        neighbors = []
        if is_valid(nr, nc):
            neighbors.append((nr, nc, direction, 1))
        neighbors.append((r, c, (direction + 1) % 4, 1000))
        neighbors.append((r, c, (direction - 1 + 4) % 4, 1000))
        return neighbors

    def heuristic(r, c): # Manhattan distance heuristic
        return abs(r - end_row) + abs(c - end_col)

    q = [(heuristic(start_row, start_col), 0, start_row, start_col, 0, [(start_row, start_col)])]
    visited = {}
    min_cost = float('inf')
    best_paths = []
    
    while q:
        f_cost, cost, r, c, direction, path = heapq.heappop(q)

        if cost > min_cost:
            continue

        #if (r, c, direction) in visited and visited[(r, c, direction)] <= cost:
        #    continue
        visited[(r, c, direction)] = cost

        if r == end_row and c == end_col:
            if cost < min_cost:
                min_cost = cost
                best_paths = [path] # Start new list of best paths
            elif cost == min_cost:
                print ("TWO")
                best_paths.append(path) # Add to existing list of best paths
            continue

        for nr, nc, nd, move_cost in get_neighbors(r, c, direction):
            new_path = copy.deepcopy(path) + [(nr, nc)]
            new_cost = cost + move_cost
            new_f_cost = new_cost + heuristic(nr, nc) # Calculate f_cost (cost + heuristic)
            heapq.heappush(q, (new_f_cost, new_cost, nr, nc, nd, new_path))

    return min_cost, best_paths

def draw(pitch, sits):
    for y in range(len(pitch)):
        for x in range(len(pitch[0])):
            c = (y, x)
            if c in sits:
                print ("O", end='')    
            else:
                print (pitch[y][x], end='')
            # if pitch[y][x] == 1:
            #     print ("#", end='')
            # elif pitch[y][x] == 0:
            #     print (".", end='')
        print ("")


# Example usage:
with open("input_16_prova.txt", "r") as f:
    grid = [list(line.strip()) for line in f]

min_cost, best_paths = solve_a_star(grid)

if best_paths:
    print(f"Lowest Cost: {min_cost}")
    print("Best Paths:")
    for path in best_paths:
        print(path)

    # To get the tiles on the best paths (for Part 2 of the problem):
    tiles_on_best_paths = set()
    for path in best_paths:
        for tile in path:
            tiles_on_best_paths.add(tile)
    draw(grid, tiles_on_best_paths)
    print(f"Number of tiles on best paths: {len(tiles_on_best_paths)}")
else:
    print("No path found.")
import heapq

def solve_with_path(grid):
    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'S')
    end_row, end_col = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 'E')

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != '#'

    def get_neighbors(r, c, direction):
        dr, dc = [(0, -1), (1, 0), (0, 1), (-1, 0)][direction]
        nr, nc = r + dr, c + dc
        neighbors = []
        if is_valid(nr, nc):
            neighbors.append((nr, nc, direction, 1))
        neighbors.append((r, c, (direction + 1) % 4, 1000))
        neighbors.append((r, c, (direction - 1 + 4) % 4, 1000))
        return neighbors

    q = [(0, start_row, start_col, 0)]
    visited = set()
    predecessors = {}  # Store predecessors (parent nodes)

    while q:
        cost, r, c, direction = heapq.heappop(q)

        if (r, c, direction) in visited:
            continue
        visited.add((r, c, direction))

        if r == end_row and c == end_col:
            path = []
            current = (r, c, direction)
            while current:
                path.append(((current[0],current[1]), current[2]))
                current = predecessors.get(current)
            return cost, path[::-1] # Reverse the path to get it from start to end

        for nr, nc, nd, move_cost in get_neighbors(r, c, direction):
            neighbor = (nr, nc, nd)
            if neighbor not in visited:
                new_cost = cost + move_cost
                heapq.heappush(q, (new_cost, nr, nc, nd))
                predecessors[neighbor] = (r, c, direction) # Store the predecessor

    return -1, None  # No path found

# Example usage:
with open("input_16_prova.txt", "r") as f:
    grid = [list(line.strip()) for line in f]

cost, path = solve_with_path(grid)
print (cost)
def draw2(grid, sits):
    points = {c[0]:c[1] for c in sits}
    dirs = ['^','>','v','<']
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            c = (y, x)
            if c in points:
                print (dirs[points[c]], end='')
            else:
                print (grid[y][x], end='')
        print ("")
print (path)
draw2(grid, path)
# if path:
#     print(f"Lowest Cost: {cost}")
#     print(f"Best Path: {path}")
# else:
#     print("No path found.")
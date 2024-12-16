import heapq

def solve(grid):
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
            neighbors.append((nr, nc, direction, 1))  # Move forward
        neighbors.append((r, c, (direction + 1) % 4, 1000))  # Rotate clockwise
        neighbors.append((r, c, (direction - 1 + 4) % 4, 1000))  # Rotate counter-clockwise (Corrected)
        return neighbors

    q = [(0, start_row, start_col, 0)]  # (cost, row, col, direction)
    visited = set()

    while q:
        cost, r, c, direction = heapq.heappop(q)

        if (r, c, direction) in visited:
            continue
        visited.add((r, c, direction))

        if r == end_row and c == end_col:
            return cost

        for nr, nc, nd, move_cost in get_neighbors(r, c, direction):
            heapq.heappush(q, (cost + move_cost, nr, nc, nd))

    return -1  # No path found

# Example usage:
with open("input_16.txt", "r") as f:
    grid = [list(line.strip()) for line in f]

result = solve(grid)
print(result)
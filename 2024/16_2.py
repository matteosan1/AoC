import heapq

def solve_part2(grid):
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
        neighbors.extend((r, c, (direction + d) % 4, 1000) for d in [-1, 1])
        return neighbors

    min_cost = float('inf')
    best_path_tiles = set()
    q = [(0, start_row, start_col, 0, {(start_row, start_col)})]
    visited = {}

    while q:
        cost, r, c, direction, path_tiles = heapq.heappop(q)

        if cost > min_cost:
            continue

        if (r, c, direction) in visited and visited[(r, c, direction)] <= cost:
            continue
        visited[(r, c, direction)] = cost

        if r == end_row and c == end_col:
            if cost < min_cost:
                min_cost = cost
                best_path_tiles = path_tiles.copy()
            elif cost == min_cost:
                best_path_tiles.update(path_tiles)
            continue

        for nr, nc, nd, move_cost in get_neighbors(r, c, direction):
            new_path_tiles = path_tiles.copy()
            new_path_tiles.add((nr, nc))
            heapq.heappush(q, (cost + move_cost, nr, nc, nd, new_path_tiles))

    return len(best_path_tiles)


# Example usage:
with open("input_16.txt", "r") as f:
    grid = [list(line.strip()) for line in f]

# part1_result = solve_part1(grid)
# print(f"Part 1: Lowest Score: {part1_result}")

part2_result = solve_part2(grid)
print(f"Part 2: Tiles on Best Paths: {part2_result}")
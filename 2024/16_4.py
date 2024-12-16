import heapq, copy

def solve_with_all_paths(grid):
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

    min_cost = float('inf')
    best_paths = []
    q = [(0, start_row, start_col, 0, [(start_row, start_col)])] # Store the path
    visited = set()

    while q:
        cost, r, c, direction, path = heapq.heappop(q)

        if cost > min_cost:
            continue

        if (r, c, direction) in visited:
            continue
        visited.add((r, c, direction))

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
            heapq.heappush(q, (cost + move_cost, nr, nc, nd, new_path))

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
with open("input_16.txt", "r") as f:
    grid = [list(line.strip()) for line in f]

min_cost, best_paths = solve_with_all_paths(grid)

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



# Computing both answers in a single loop: we keep track of our score and our path. If we reach the end position and our score is optimal (i.e. we did not take a detour), we add the tiles in our path to the set of tiles for part 2.
# On to the Python trick of the day: more and more people are starting to use complex numbers for grid puzzles, and they might have hit a roadblock when using them in a priority queue.
# Suppose you have a queue of (score, position) tuples. As long as the scores are unique, they can fully determine the order of the queue. But when there are duplicate scores (which can easily happen today), Python wants to sort on the second element, position.
# Since complex numbers can't be sorted (1+9j isn't necessarily "less" than 2+2j), Python throws an error:
# TypeError: '<' not supported between instances of 'complex' and 'complex'
# There are a few ways to mitigate this:
# write your own complex number class, inheriting from the built-in complex but redefining less-than (u/xelf did this here),
# store the number as a string, and "re-hydrate" it to complex upon retrieval (u/atreju3647 did this here),
# store the real and imaginary parts separately, and combine them upon retrieval (u/TiCoinCoin did this here),
# when inserting to the priority queue, add a "tie-breaker" to your tuple. So (score, position) becomes (score, t, position), where t is a unique value. This can be a random number, or an ever incrementing value.

# Here's a simple example:
# from heapq import heappush, heappop

# Q = [(1, i:=0, complex(1))]
# for x in [2, 3, 4]:
#     heappush(Q, (x, i := i+1, complex(x,x)))
# When extracting values from the queue, just ignore the tie-breaker:

# x, _, y = heappop(Q)
# If anyone has questions, suggestions or other solutions, feel free to let me know!
import timeit

from utils import readInput, bcolors, solve_BFS_with_path, manhattan_circle

def loadInput():
    #lines = readInput("input_20_prova.txt")
    lines = readInput("input_20.txt")

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

def get_neighbors(grid, c, cheated, cheat, no_cheat_path):
    neighbors = []
    for dc in DIRECTIONS:
        nc = c + dc
        if is_valid(grid, nc):
            neighbors.append((nc, cheated))
        elif cheat and not cheated:
            nc2 = c + 2*dc
            if is_valid(grid, nc2) and nc2 in no_cheat_path:
                neighbors.append((nc2, True))
    return neighbors

def part1(racetrack, start, end):
    path_no_cheat = solve_BFS_with_path(racetrack, start, end)
    path_no_cheat = {p:i for i, p in enumerate(path_no_cheat)}
    n = 0
    for c, cost in path_no_cheat.items():
        # path[n] - i - 2 is how much closer to the goal we 
        # end up. 2 because if we stay on the path after 2
        # steps, we end up 2 steps closer
        for nc in manhattan_circle(c, 2):
            if nc in path_no_cheat and path_no_cheat[nc] - cost - 2 >= 100:
                n += 1
    print (f"🎄 Part 1: {n}")
    
def part2(racetrack, start, end):
    path_no_cheat = solve_BFS_with_path(racetrack, start, end)
    path_no_cheat = {p:i for i, p in enumerate(path_no_cheat)}
    n = 0
    for c, cost in path_no_cheat.items():
        for delta in range(2, 21):
            for nc in manhattan_circle(c, delta):
                if nc in path_no_cheat and path_no_cheat[nc] - cost - delta >= 100:
                    n += 1
    print (f"🎄🎅 Part 2: {n}")

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
    
    t2 = timeit.timeit(lambda: part2(*inputs), number=1)
    print (f"{t2*1000:.3f} ms")

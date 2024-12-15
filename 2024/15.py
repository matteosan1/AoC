import timeit

from utils import readInput

# PROVA RE CON OGGETTI E COLLISION DETECION
# CREARE LISTA DI SPOSTAMENTI E POI INVERTIRLA

dirs = {'^':complex(0,-1), ">":complex(1,0), "<":complex(-1,0), "v":complex(0,1)}

def loadInput(part=1):
    #lines = readInput("input_15_prova.txt")
    lines = readInput("input_15.txt")

    grid = {}
    instructions = ""
    start = None
    y = 0
    while y < len(lines):
        if lines[y][0] != "#":
            instructions += lines[y]
        else:
            if part == 2:
                ix =  0
                for x in range(len(lines[0])):
                    if lines[y][x] == "#":
                        grid[complex(ix, y)] = 1
                        grid[complex(ix+1, y)] = 1
                    elif lines[y][x] == ".":
                        grid[complex(ix, y)] = 0
                        grid[complex(ix+1, y)] = 0
                    elif lines[y][x] == "@":
                        start = complex(ix, y)
                        grid[complex(ix, y)] = 0
                        grid[complex(ix+1, y)] = 0
                    elif lines[y][x] == "O":
                        grid[complex(ix, y)] = 3
                        grid[complex(ix+1, y)] = 4
                    ix += 2
            else:
                for x in range(len(lines[0])):
                    if lines[y][x] == "#":
                        grid[complex(x, y)] = 1
                    elif lines[y][x] == ".":
                        grid[complex(x, y)] = 0
                    elif lines[y][x] == "@":
                        start = complex(x, y)
                        grid[complex(x, y)] = 0
                    elif lines[y][x] == "O":
                        grid[complex(x, y)] = 3
        y += 1
    return grid, instructions, start

def move(pos, grid, dir):
    new_pos = pos + dir
    if grid[new_pos] == 3:
        res = move(new_pos, grid, dir)
    if grid[new_pos] == 0:
        grid[new_pos] = grid[pos]
        grid[pos] = 0
        return new_pos
    return pos

def GPS(grid):
    gps = 0
    for g in grid:
        if grid[g] == 3:
            gps += g.real + g.imag*100
    return gps

def part1(grid, instructions, start):
    for t, i in enumerate(instructions):
        start = move(start, grid, dirs[i])
    score = GPS(grid)
    #draw(grid, start)
    print (f"🎄 Part 1: {int(score)}")

def move2(pos, grid, dir):
    new_pos = [p + dir for p in pos]
    if dir == -1 or dir ==  1:
        if grid[new_pos[0]] == 3 or grid[new_pos[0]] == 4:
            res = move2(new_pos, grid, dir)
    else:
        new_new_pos = []
        for i in range(len(new_pos)):
            if grid[new_pos[i]] == 3:
                new_new_pos.append(new_pos[i])
                new_new_pos.append(new_pos[i]+1)
            elif grid[new_pos[i]] == 4:
                new_new_pos.append(new_pos[i])
                new_new_pos.append(new_pos[i]-1)
            elif grid[new_pos[i]] == 1:
                new_new_pos = []
                break
        new_new_pos = list(set(new_new_pos))
        if len(new_new_pos) > 0:
            res = move2(new_new_pos, grid, dir)
            
    if all([grid[new_pos[i]] == 0 for i in range(len(new_pos))]):
        for i in range(len(new_pos)):
            grid[new_pos[i]] = grid[pos[i]]
            grid[pos[i]] = 0
    if grid[new_pos[0]] == 0:     
        return new_pos[0]
    else:
        return pos[0]

def part2(grid, instructions, start):
    for t, i in enumerate(instructions):
        start = move2([start], grid, dirs[i])
    score = GPS(grid)
    #draw(grid, start, 2)
    print (f"🎄🎅 Part 2: {int(score)}")

def draw(grid, start, part=1):
    xmax = int(max([c.real for c in grid]))+1
    ymax = int(max([c.imag for c in grid]))+1
    for y in range(ymax):
        for x in range(xmax):
            g = complex(x, y)
            if g == start:
                print ("@", end='')
            elif grid[g] == 0:
                print (".", end='')
            elif grid[g] == 1:
                print ("#", end='')
            elif grid[g] == 3:
                if part == 1:
                    print ("O", end='')
                else:
                    print ("[", end='')
            elif grid[g] == 4:
                print ("]", end='')
        print (" ")

if __name__ == '__main__':
    title = "Day 15: Warehouse Woes"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(*inputs), number=1)
    print (f"{t1*1000:.3f} ms")

    inputs = loadInput(part=2)

    t2 = timeit.timeit(lambda: part2(*inputs), number=1)
    print (f"{t2*1000:.3f} ms")

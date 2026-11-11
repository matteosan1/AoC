import time

from utils import readInput, bcolors, manhattan_dist, DIRECTIONS

def loadInput(filename: str):
    lines = readInput(filename)

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

def dijkstra(grid, end):
    D = {end: 0}
    Q = [end]
    while Q:
        p = Q.pop()
        for p2 in [p + dp for dp in DIRECTIONS]:
            if grid[p2] != 1 and p2 not in D:
                Q.append(p2)
                D[p2] = D[p] + 1
    return D

def part1(racetrack, start, end):
    lower_bound = -100
    D = dijkstra(racetrack, end)
    res = [(p1, p3, t) for p1 in D
            for p2 in [p1 + dp for dp in DIRECTIONS] if racetrack[p2] == 1
                for p3 in [p2 + dp for dp in DIRECTIONS]
                    if  p3 in D and (t := D[p3] - D[p1] + 2) <= lower_bound]
    print (f"🎄 Part 1: {len(res)}", end='')
    

def neighborhood(p, radius):
    return [p + complex(dx, 0) + complex(0, dy) 
            for dx in range(-radius, radius + 1)
            for dy in range(-(radius - abs(dx)), radius - abs(dx) + 1)]

def part2(racetrack, start, end):
    radius = 20
    lower_bound = -100
    D = dijkstra(racetrack, end)
    res = [(p1, p2, t)
            for p1 in D
            for p2 in neighborhood(p1, radius)
            if  p2 in D and (t := D[p1] - D[p2] + manhattan_dist(p1, p2)) <= lower_bound]
    print (f"🎄🎅 Part 2: {len(res)}", end='')

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
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_20.txt")
    
    t0 = time.time()
    part1(*inputs)
    print (" - {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(*inputs)
    print (" - {:.5f}".format(time.time()-t0))

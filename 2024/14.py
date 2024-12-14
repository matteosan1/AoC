import timeit, numpy as np, copy

from utils import readInput

def loadInput():
    #lines = readInput("input_14_prova.txt")
    #xmax, ymax = 11, 7
    lines = readInput("input_14.txt")  
    xmax, ymax = 101, 103

    robots = []
    vels = []
    for l in lines:
        items = l.split()
        robots.append(complex(*map(int, items[0].split("=")[1].split(","))))
        vels.append(complex(*map(int, items[1].split("=")[1].split(","))))
    return robots, vels, xmax, ymax

def quadrants(robots, xmax, ymax):
    quadrants = [0, 0, 0, 0]
    for r in robots:
        if r.real < xmax//2:
            if r.imag < ymax//2:
                quadrants[0] += 1
            elif r.imag > ymax//2:
                quadrants[1] += 1
        elif r.real > xmax//2:
            if r.imag < ymax//2:
                quadrants[2] += 1
            elif r.imag > ymax//2:
                quadrants[3] += 1
    return quadrants

import copy
def part1(r, vels, xmax, ymax):
    robots = copy.deepcopy(r)
    for i in range(len(robots)):
        npos = complex(robots[i]+vels[i]*100)
        robots[i] = complex(npos.real%xmax, npos.imag%ymax)
    print (f"🎄 Part 1: {np.prod(quadrants(robots, xmax, ymax))}")

def draw(ps, xmax, ymax):
    for y in range(0, ymax):
        for x in range(0, xmax):
            pos = complex(x, y)
            c = ps.count(pos)
            if c != 0:
                print (str(c), end='')
            else:
                print (" ", end='')
        print (" ")

def part2(robots, vels, xmax, ymax):
    seconds = 10403 # found when the starting position is found again
    #positions = [r[0] for r in robots]
    bye = False
    stds = [np.inf, np.inf]
    for second in range(1, seconds):
        for i in range(len(robots)):
            npos = complex(robots[i]+vels[i])
            robots[i] = complex(npos.real%xmax, npos.imag%ymax)

        std = (np.std([float(r.real) for r in robots]), np.std([float(r.imag) for r in robots]))
        if std[0] <= stds[0] and std[1] <= stds[1]:
            stds = std
            christmas_tree = second
    print (f"🎄🎅 Part 2: {christmas_tree}")

if __name__ == '__main__':
    title = "Day 14: Restroom Redoubt"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(*inputs), number=1)
    print (f"{t1*1000:.3f} ms")

    t2 = timeit.timeit(lambda: part2(*inputs), number=1)
    print (f"{t2*1000:.3f} ms")

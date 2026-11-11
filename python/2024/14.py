import time, numpy as np, copy

from utils import readInput, manhattan_dist

# FIXME PROVARE CON DISCRETE FOURIER TRANSFORM

def loadInput(filename: str) -> tuple[list[complex], list[complex], int, int]:
    lines = readInput(filename)
    xmax, ymax = 101, 103

    robots: list[complex] = []
    vels: list[complex] = []
    for l in lines:
        items = l.split()
        robots.append(complex(*map(int, items[0].split("=")[1].split(","))))
        vels.append(complex(*map(int, items[1].split("=")[1].split(","))))
    return robots, vels, xmax, ymax

def quadrants(robots: list[complex], xmax: int, ymax: int) -> list[int]:
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

def part1(robots: list[complex], vels: list[complex], xmax: int, ymax: int):
    robots = copy.deepcopy(robots)
    for i in range(len(robots)):
        npos = complex(robots[i]+vels[i]*100)
        robots[i] = complex(npos.real%xmax, npos.imag%ymax)
    print (f"🎄 Part 1: {np.prod(quadrants(robots, xmax, ymax))}", end='')

def draw(ps: list[complex], xmax: int, ymax: int):
    for y in range(0, ymax):
        for x in range(0, xmax):
            pos = complex(x, y)
            c = ps.count(pos)
            if c != 0:
                print (str(c), end='')
            else:
                print (" ", end='')
        print (" ")

def mean_distance_to_centroid(robots: list[complex], distance=manhattan_dist) -> float:
    centroid = np.mean(robots)
    return np.mean([distance(r, centroid) for r in robots])

def part2_bis(robots: list[complex], vels: list[complex], xmax: int, ymax: int):
    seconds = 10403 # found when the starting position is found again
    minimum = (-1, float("inf"))
    for second in range(1, seconds):
        for i in range(len(robots)):
            npos = complex(robots[i]+vels[i])
            robots[i] = complex(npos.real%xmax, npos.imag%ymax)
        dist = mean_distance_to_centroid(robots)
        if dist < minimum[1]:
            minimum = (second, dist)
    print (f"🎄🎅 Part 2: {minimum}", end='')

def part2(robots: list[complex], vels: list[complex], xmax: int, ymax: int):
    seconds = 10403 # found when the starting position is found again

    stds = (-1, float("inf"), float("inf"))
    for second in range(1, seconds):
        for i in range(len(robots)):
            npos = complex(robots[i]+vels[i])
            robots[i] = complex(npos.real%xmax, npos.imag%ymax)

        std = (np.std([float(r.real) for r in robots]), np.std([float(r.imag) for r in robots]))
        if std[0] <= stds[1] and std[1] <= stds[2]:
            stds = (second, std[0], std[1])

    # for i in range(len(r)):
    #     npos = complex(r[i]+vels[i]*christmas_tree)
    #     r[i] = complex(npos.real%xmax, npos.imag%ymax)
    #draw(r, xmax, ymax)
    print (f"🎄🎅 Part 2: {stds[0]}", end='')

if __name__ == '__main__':
    title = "Day 14: Restroom Redoubt"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_14.txt")
    
    t0 = time.time()
    part1(*inputs)
    print (" - {:.6f}s".format(time.time()-t0))
    
    t0 = time.time()
    part2(*inputs)
    print (" - {:.6f}s".format(time.time()-t0))

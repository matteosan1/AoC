import time, re, numpy as np, copy, math

from itertools import combinations

from utils import readInput

def loadInput():
    r = re.compile(r"(\w\=(-?\d+))")
    lines = readInput("input_12.txt")
    moons = []
    for l in lines:
        g = r.findall(l)
        moons.append([int(x[1]) for x in g] + [0, 0, 0])
    return moons

def move(moons):
    for c in combinations(moons, 2):
        for i in range(3):
            dv = 0
            if c[0][i] > c[1][i]:
                dv = -1
            elif c[0][i] < c[1][i]:
                dv = +1
            c[0][i+3] += dv
            c[1][i+3] -= dv

    for m in moons:
        for i in range(3):
            m[i] += m[i+3]

def energy(moon):
    return np.sum(np.abs(moon[:3])) * np.sum(np.abs(moon[3:]))
            
def part1(moons):
    for i in range(1000):
        move(moons)
    tot_energy = 0
    for m in moons:
        tot_energy += energy(m)
    print (f"🎅 Part 1: {tot_energy}")
    
def part2(moons):
    init = copy.deepcopy(moons)
    period = [0 for _ in range(3)]
    cycles = 1
    while True:
        move(moons)
        cycles += 1
        for coord in range(3):
            if period[coord] == 0:
                if all([moons[i][coord] == init[i][coord] for i in range(len(moons))]):
                    period[coord] = cycles
        if all([p != 0 for p in period]):
            break
    print (period)
    print (f"🎅🎄 Part 2: {math.lcm(*period)}")


if __name__ == "__main__":
    title = "Day 12: The N-Body Problem"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(copy.deepcopy(inputs))
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))

    

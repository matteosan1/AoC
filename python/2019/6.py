import time, heapq

from utils import readInput

def loadInput():
    orbits = {}
    orbits2 = {}
    lines = readInput("input_6.txt")
    for l in lines:
        parts = l.split(")")
        orbits.setdefault(parts[0], []).append(parts[1])
        orbits2.setdefault(parts[1], []).append(parts[0])
        orbits2.setdefault(parts[0], []).append(parts[1])
        
    planets = set([])
    for k, v in orbits.items():
        for p in v:
            planets.add(p)
    for p in planets:
        if p not in orbits:
            orbits[p] = []
    return orbits, orbits2

def find_paths(orbits, start='COM'):
    paths = []
    queue = [[start]]
    while len(queue) != 0:
        path = queue.pop()
        pos = path[-1]
        if orbits[pos] == []:
            paths.append(path)
        else:
            for neigh in orbits[pos]:
                queue.append(path[:]+[neigh])
    return paths

def part1(orbits):
    paths = find_paths(orbits)
    tot_orbits = 0
    for k in orbits:
        if k == 'COM':
            continue
        for p in paths:
            if k in p:
                tot_orbits += p.index(k)
                break
    print (f"🎅 Part 1: {tot_orbits}")

def get_dest(orbits, key):
    dests = []
    for k, v in orbits.items():
        if key in v:
            dests.append(k)
    return dests
    
def transfers(orbits, start="YOU", target="SAN"):
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start))
    while len(pq):
        state = heapq.heappop(pq)
        steps, pos = state
        visited.add(pos)
        if pos == target:
            return state
        for new_pos in get_dest(orbits, pos):
            if new_pos not in visited:
                heapq.heappush(pq, (steps+1, new_pos))
    
def part2(orbits):
    print (f"🎅🎄 Part 2: {transfers(orbits)[0]-2}")

if __name__ == "__main__":
    title = "Day 6: Universal Orbit Map"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    input, input2 = loadInput()
    
    t0 = time.time()
    part1(input)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(input2)
    print ("Time: {:.5f}".format(time.time()-t0))

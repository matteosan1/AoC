import time
from utils import readInput

def loadInput():
    #lines = readInput("input_10_prova.txt")
    lines = readInput("input_10.txt")
    starts = []
    map = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "0":
                starts.append(complex(x, y))
            map[complex(x, y)] = int(lines[y][x])
    return map, starts

dirs = {0:complex(0, -1), 1:complex(1, 0),
        2:complex(0, 1), 3:complex(-1, 0)}

def part1(map, starts):
    npaths = []
    for start in starts:
        queue = [(start, 0)]
        visited = [start]
        pos = start
        while len(queue) > 0:
            pos = queue.pop()
            visited.append(pos[0])
            if pos[1] == 9:
                npaths.append(pos[0]) #+= 1
                break
            for i in range(4):
                npos = pos[0] + dirs[i]
                if npos in map and npos not in visited:
                    if (map[npos] - pos[1]) == 1:
                        queue.append((npos, map[npos]))
    return len(npaths)

def part2(disk):
    pass
    return 0

if __name__ == '__main__':
    title = "Day 10: Hoof It"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(*inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

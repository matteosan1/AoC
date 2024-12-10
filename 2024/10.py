import time
from utils import readInput

# TRY DFS to speed up

# def dfs(graph, start_node, visited=None):
#   if visited is None:
#     visited = set()

#   visited.add(start_node)
#   print(start_node)

#   for neighbor in graph[start_node]:
#     if neighbor not in visited:
#       dfs(graph, neighbor, visited)

def loadInput():
    lines = readInput("input_10_prova.txt")
    #lines = readInput("input_10.txt")
    starts = []
    map = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == ".":
                map[complex(x, y)] = 0
            elif lines[y][x] == "0":
                starts.append(complex(x, y))
                map[complex(x, y)] = int(lines[y][x])
            else:
                map[complex(x, y)] = int(lines[y][x])
    return map, starts

dirs = {0:complex(0, -1), 1:complex(1, 0),
        2:complex(0, 1), 3:complex(-1, 0)}

def part1(map, starts):
    score = 0
    for start in starts:
        queue = [(start, 0)]
        visited = [start]
        pos = start
        while len(queue) > 0:
            pos = queue.pop()
            visited.append(pos[0])
            if pos[1] == 9:
                score += 1
            for i in range(4):
                npos = pos[0] + dirs[i]
                if npos in map and npos not in visited:
                    if (map[npos] - pos[1]) == 1:
                        queue.append((npos, map[npos]))
    return score

def part2(map, starts):
    rate = {}
    for start in starts:
        queue = [(start, 0)]
        pos = start
        while len(queue) > 0:
            pos = queue.pop()
            if pos[1] == 9:
                rate[pos[0]] = rate.get(pos[0], 0) + 1
            for i in range(4):
                npos = pos[0] + dirs[i]
                if npos in map:
                    if (map[npos] - pos[1]) == 1:
                        queue.append((npos, map[npos]))
    return sum(rate.values())
    
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
    res2 = part2(*inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

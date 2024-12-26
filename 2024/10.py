import time

from utils import readInput, DIRECTIONS

dirs = {i:d for i,d in enumerate(DIRECTIONS)}

# TRY DFS to speed up

# def dfs(graph, start_node, visited=None):
#   if visited is None:
#     visited = set()

#   visited.add(start_node)
#   print(start_node)

#   for neighbor in graph[start_node]:
#     if neighbor not in visited:
#       dfs(graph, neighbor, visited)

def loadInput(filename: str) -> tuple[dict[complex, int], list[complex]]:
    lines = readInput(filename)
    starts: list[complex] = []
    map: dict[complex, int] = {}
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

def part1(map: dict[complex, int], starts: list[complex]):
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
    print (f"🎄 Part 1: {score}", end="")


def part2(map: dict[complex, int], starts: list[complex]):
    rate: dict[complex, int] = {}
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
    print (f"🎄🎅 Part 2: {sum(rate.values())}", end="")

    
if __name__ == '__main__':
    title = "Day 10: Hoof It"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_10.txt")

    t0 = time.time()
    part1(*inputs)
    print (f" - {time.time()-t0:.5f}")
    
    t0 = time.time()
    part2(*inputs)
    print (f" - {time.time()-t0:.5f}")
    
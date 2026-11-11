import time, heapq

from utils import readInput

def loadInput():
    lines = readInput("input_20.txt")
    maze = {}
    portals = {}
    start = None
    target = None
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "#" or c == ' ':
                continue
            if c == ".":
                maze[(x, y)] = 1
                for d in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nx, ny = x+d[0], y+d[1]
                    if 'A' <= lines[ny][nx] <= 'Z':
                        label = lines[ny][nx]
                        nx, ny = x+2*d[0], y+2*d[1]
                        label += lines[ny][nx]
                        if d[0] == -1 or d[1] == -1:
                            label = "".join(reversed(label))
                        if label == 'AA':
                            start = (x, y)
                            break
                        elif label == 'ZZ':
                            target = (x,y)
                            break
                        inner = True
                        if nx == 0 or ny == 0 or nx == len(lines[0])-1 or ny == len(lines)-1:
                            inner = False
                        if label not in portals:
                            portals[label] = [None, None]
                        if inner:
                            portals[label][0] = (x, y)
                        else:
                            portals[label][1] = (x, y)
                        break
    return maze, portals, start, target

def dfs(m, portals, start, target):
    paths = []
    visited = set()
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    pq = []
    heapq.heappush(pq, (0, start))
    while len(pq):
        state = heapq.heappop(pq)
        steps, pos = state
        visited.add(pos)
        if pos == target:
            return state
            
        for d in dirs:
            offset = 0
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            for p in portals:
                try:             
                    idx = portals[p].index(new_pos)
                    new_pos = portals[p][abs(idx-1)]
                    offset = 1
                    break
                except:
                    pass
            if new_pos in m and new_pos not in visited:
                    heapq.heappush(pq, (steps+1+offset, new_pos))
    return None

def part1(maze, portals, start, target):
    path = dfs(maze, portals, start, target)
    if path is not None:
        print (f"🎅 Part 1: {path[0]}")

def dfs2(m, portals, start, target):
    level = 0
    paths = []
    visited = set()
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    D = {}
    D[(start, 0)] = 0
    pq = []
    heapq.heappush(pq, (0, start, 0))
    while len(pq):
        state = heapq.heappop(pq)
        steps, pos, level = state
        visited.add((pos, level))
        if pos == target and level == 0:
            return state
            
        for d in dirs:
            offset = 0
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            new_level = level
            is_wall = False
            for p in portals:
                try:
                    idx = abs(portals[p].index(new_pos) - 1)
                    new_pos = portals[p][idx]
                    if level == 0 and idx == 0:
                        is_wall = True
                        break
                    if idx == 0:
                        new_level += 1
                    else:
                        new_level -= 1
                    offset = 1
                    break
                except:
                    pass

            if not is_wall and new_pos in m and (new_pos, new_level) not in visited:
                new_steps = steps+1+offset
                if new_steps < D.get((new_pos, new_level), float('inf')):                
                    D[(new_pos, new_level)] = new_steps
                    heapq.heappush(pq, (new_steps, new_pos, new_level))
    return None

        
def part2(maze, portals, start, target):
    path = dfs2(maze, portals, start, target)
    if path is not None:
        print (f"🎄 Part 2: {path[0]}")
    
if __name__ == "__main__":
    title = "Day 20: Donut Maze"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    maze, portals, start, target = loadInput()

    t0 = time.time()
    part1(maze, portals, start, target)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(maze, portals, start, target)
    print ("Time: {:.5f}".format(time.time()-t0))

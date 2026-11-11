from utils import dirs
from queue import PriorityQueue
from collections import deque

def backtrack(visited, start, end):
    d = end
    path = [end]
    while d != start:
        path.append(visited[d].prev)
        d = visited[d].prev
    return list(reversed(path))

def findMin(l):
    val = float('+inf')
    current = None
    for k, v in l.items():
        if v.f < val:
            val = v.f
            current = v
    return current

def astar(m, start, end):
    openList = {}
    closeList = {}

    openList[start] = start
    while len(openList) != 0:
        current = findMin(openList)
        del openList[current]
        closeList[current] = current 

        if current == end:
            break
    
        for d in dirs.values():
            child = d(current)
            if child not in m or child in closeList:
                continue
            child = m[child]
            child.prev = current
            child.g = current.g + child.edge
            child.h = child.distance(end)
            child.f = child.g + child.h
            if child in openList:
                if child.g > openList[child].g:
                    continue
            openList[child] = child
    return backtrack(closeList, start, end)

def dijkstra(m, start, end):
    visited = {}
    D = {i:float('inf') for i in m}
    D[start] = start.edge

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        dist, current = pq.get()
        visited[current] = current
        for d in dirs.values():
            neigh = d(current)
            if neigh in m:
                distance = m[neigh].edge
                if neigh not in visited:
                    new_cost = D[current] + distance
                    if new_cost < D[neigh]:
                        neigh.prev = current
                        pq.put((new_cost, neigh))
                        D[neigh] = new_cost
    return backtrack(visited, start, end), D

def dfs(m, start, end):
    visited = {}
    stack = [start]

    while len(stack) != 0:
        pos = stack.pop()
        visited[pos] = pos
        
        if pos == end:
            break
        for d in dirs.values():
            new_pos = d(pos)
            if new_pos in m and new_pos not in visited.keys():
                new_pos.prev = pos
                stack.append(new_pos)

    return backtrack(visited, start, end)

def bfs(m, start, end):
    visited = {}
    q = deque()
    q.append(start)

    while len(q) != 0:
        pos = q.popleft()
        visited[pos] = pos
        
        if pos == end:
            break
        
        for d in dirs.values():
            new_pos = d(pos)
            if new_pos in m and new_pos not in visited:
                new_pos.prev = pos
                q.append(new_pos)
    return backtrack(visited, start, end)

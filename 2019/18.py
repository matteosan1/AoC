import time, copy

from itertools import combinations
from queue import PriorityQueue

from utils import readInput

#def dfs(m, start, target, keys, doors):
#    paths = []
#    dirs = {0:-1j, 1:1, 2:1j, 3:-1}
#
#    stack = [[(start, 0)]]    
#    while len(stack) != 0:
#        state = stack.pop()
#        pos, coll_k = state[-1]
#        
#        if coll_k == target:
#            paths.append(state)
#            
#        for d in dirs.values():
#            new_pos = pos + d
#                        
#            if new_pos in m:
#                if ord('A') <= m[new_pos] <= ord('Z'):
#                    if coll_k & 2**(m[new_pos]-65) == 0:
#                        continue       
#                new_coll_k = coll_k
#                if ord('a') <= m[new_pos] <= ord('z'):
#                    if coll_k & 2**(m[new_pos]-97) == 0:        
#                        new_coll_k = set_key(new_coll_k, m[new_pos])
#                if (new_pos, new_coll_k) not in state:
#                    new_state = copy.deepcopy(state)
#                    new_state.append((new_pos, new_coll_k))
#                    stack.append(new_state)
#    print (min([len(s)-1 for s in paths]))

def loadInput():
    lines = readInput("input_18.txt")
    dungeon = {}
    #keys = {}
    #doors = {}
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "#":
                continue
            if c != ".":
                dungeon[complex(x, y)] = ord(c)
            else:
                dungeon[complex(x, y)] = 1
    return dungeon

def set_key(keys, n):
    return keys | 2**(n-97)

def set_door(doors, n):
    return doors | 2**(n-65)

def pre_dfs(m, start, target, keys, doors):
    paths = []
    dirs = {0:-1j, 1:1, 2:1j, 3:-1}

    stack = [[(start, 0)]]
    #print ("target", target)
    while len(stack) != 0:
        state = stack.pop()
        pos, found_doors = state[-1]
        #print (state)
        if pos == target:
            paths.append(state)
            continue
        #elif pos != start and ord('a') <= m[pos] <= ord('z'):
        #    continue                
        
        for d in dirs.values():
            new_pos = pos + d
            if new_pos in m:
                new_found_doors = found_doors
                if ord('A') <= m[new_pos] <= ord('Z'):
                    if found_doors & 2**(m[new_pos]-65) == 0:        
                        new_found_doors = set_door(new_found_doors, m[new_pos])
                if (new_pos, new_found_doors) not in state:
                    new_state = copy.deepcopy(state)
                    new_state.append((new_pos, new_found_doors))
                    stack.append(new_state)
    
    best_path = (float('inf'), 0)
    for p in paths:
        if len(p) < best_path[0]:
            best_path = (len(p)-1, p[-1][1])
    return best_path

def dijkstra(m, start, target, keys):
    print ("target ", target)
    visited = []
    D = {(i, 0):float('inf') for i in m}
    #D = {}
    D[(start, 0)] = 0
    #D[start] = 0

    pq = PriorityQueue()
    pq.put((0, start, 0))

    while not pq.empty():
        dist, current, found_keys = pq.get()
        print (dist, chr(current), current, found_keys)
        visited.append((current, found_keys))
        #visited.append(current)
        if found_keys == target:
            print ("FINE ", dist, chr(current), found_keys)
            break
        for neigh in m[current].keys():
            #print ("fk ", found_keys, m[current][neigh][1]) 
            if m[current][neigh][1] != 0 and (found_keys & m[current][neigh][1] != m[current][neigh][1]):
                continue
            #print (neigh)
            new_found_keys = found_keys
            distance = m[current][neigh][0]
            #if neigh not in visited:
            if (neigh, new_found_keys) not in visited:
                new_cost = D[(current, found_keys)] + distance
                #new_cost = D[current] + distance
                if new_cost < D.get((neigh, new_found_keys), float('inf')):
                #if new_cost < D[neigh]:
                    #print (new_found_keys, neigh)
                    new_found_keys = set_key(new_found_keys, int(neigh))
                    pq.put((new_cost, neigh, new_found_keys))
                    #print (chr(neigh))
                    D[(neigh, new_found_keys)] = new_cost
                    #D[neigh] = new_cost
        #print ("PQ: ", pq.qsize())
        
def part1(dungeon):
    start = [i for i in dungeon.keys() if dungeon[i] == ord("@")].pop()
    keys = [i for i in dungeon.keys() if ord('a') <= dungeon[i] <= ord('z')]
    doors = [i for i in dungeon.keys() if ord('A') <= dungeon[i] <= ord('Z')]
    poi = {v:k for k,v in dungeon.items() if ord('a') <= v <= ord('z')}
    poi.update({ord("@"):start})
    
    reduced_map = {}
    t0 = time.time()
    #print (poi)
    for comb in combinations(poi.keys(), 2):
        #print (comb)
        best = pre_dfs(dungeon, poi[comb[0]], poi[comb[1]], keys, doors)
        if best[0] != float('inf'):
            if comb[1] != ord('@'):
                reduced_map.setdefault(comb[0], {}).update({comb[1]:best})
            if comb[0] != ord('@'):
                reduced_map.setdefault(comb[1], {}).update({comb[0]:best})
    print (time.time()-t0)
    print (reduced_map)
    #dijkstra(reduced_map, ord('@'), 2**(len(keys))-1, keys)
    #dfs(dungeon, start, target, keys, doors)
    
    print (f"ðŸŽ… Part 1: {0}")
    
def part2(lines):
    print (f"ðŸŽ…ðŸŽ„ Part 2: Intcode")
    
if __name__ == "__main__":
    title = "Day 18: Many-Worlds Interpretation"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    lines = loadInput()
    
    t0 = time.time()
    part1(lines)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    #t0 = time.time()
    #path = part2(lines, path)
    #print ("Time: {:.5f}".format(time.time()-t0))

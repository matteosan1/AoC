import time, copy, heapq

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
    lines = readInput("prova.txt")
    dungeon = {}
    #keys = {}
    #doors = {}
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == "#":
                continue
            if c != ".":
                dungeon[(x, y)] = ord(c)
            else:
                dungeon[(x,y)] = 1
    return dungeon

def set_key(keys, n):
    return keys | 2**(n-97)

def set_door(doors, n):
    return doors | 2**(n-65)
        
def pre_dfs(m, start, target, doors):
    visited = set()
    #dirs = [Complex(0,-1), Complex(1,0), Complex(0,1), Complex(-1,0)]
    dirs = [(0,-1), (1,0), (0,1), (-1,0)]
    pq = []
    heapq.heappush(pq, (0, start, 0))
    while len(pq):
        state = heapq.heappop(pq)
        steps, pos, found_doors = state
        visited.add(pos)
        if pos == target:
            return state
            
        #new_found_doors = found_doors
        if ord('A') <= m[pos] <= ord('Z'):
            found_doors = set_door(found_doors, m[pos])
        
        for d in dirs:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if new_pos in m and new_pos not in visited:
                    heapq.heappush(pq, (steps+1, new_pos, found_doors))
    return None

def keys_doors_match(keys, doors):
    if keys == 0:
        return doors == 0
    else:
        return keys&doors == doors
        
def dfs(m, start, target):
    #print ("target ", target)
    visited = []
    pq = []
    heapq.heappush(pq, (0, start, 0))
    found = False
    best = None
    i = 0
    while len(pq):
        state = heapq.heappop(pq)
        steps, key, collected_keys = state
        #print (steps, chr(key), collected_keys)
        #visited.append((key, collected_keys))
        #visited.append(key)
            
        if ord('a') <= key <= ord('z'):
            collected_keys = set_key(collected_keys, key)

        if collected_keys == target:
            found = True
            if best is None or best[0] > steps:
                print ("NEW BEST FOUND ", state)
                best = state
        #print (collected_keys)
        for new_key in m[key].keys():
            #if m[key][new_key][2] & collected_keys != collected_keys:
            #    continue
            #print (collected_keys, set_key(0, new_key), keys_doors_match(collected_keys, new_key))
            if keys_doors_match(collected_keys, set_key(0, new_key)):
                continue
            if not keys_doors_match(collected_keys, m[key][new_key][2]):# or new_key in visited:
                continue
            #print ("possible ", m[key][new_key], chr(new_key), new_key)
            #if (new_key, collected_keys) not in visited:
            #if new_key not in visited:
            #state = (steps+m[key][new_key][0], new_key, collected_keys)
            #idx = pq.index(state)
            #if 
               
            #    if state[0] <
            #if not state in pq:
            heapq.heappush(pq, state)
            
        #if i == 8:
        #    print (pq)
        #    break
        #i += 1
    if found:
        return best
    else:
        return None
        
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
    #poi = {v:k for k,v in dungeon.items() if ord('a') <= v <= ord('z')}
    #poi.update({ord("@"):start})
    reduced_map = {dungeon[k]:{} for k in keys}
    t0 = time.time()
    for k in keys:
        #if dungeon[k] != ord('i'):
        #    continue
        best = pre_dfs(dungeon, start, k, doors)
        if best is not None:            
            reduced_map.setdefault(ord('@'), {}).update({dungeon[k]:best})
        for dest in keys:
            if k == dest and dungeon[k] not in reduced_map[dungeon[dest]]:
                continue
            best = pre_dfs(dungeon, k, dest, doors)
            if best is not None:
                reduced_map.setdefault(dungeon[k], {}).update({dungeon[dest]:best})
                reduced_map.setdefault(dungeon[dest], {}).update({dungeon[k]:best})
    print (time.time()-t0)
    print (len(reduced_map))
    for k, v in reduced_map.items():
        if k == ord('i'):
            print ([chr(x) for x in v.keys()])
        print (chr(k), len(v))
    #dijkstra(reduced_map, ord('@'), 2**(len(keys))-1, keys)
    #print (dfs(reduced_map, ord('@'), 2**(len(keys))-1))
    
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

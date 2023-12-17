import time
from queue import PriorityQueue
from copy import deepcopy
import heapq

from utils import readInput, Point

class Lavatube:
    def __init__(self):
        self.map = {}
        self.xlims = (0, 0)
        self.ylims = (0, 0)

    def load(self, lines):
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                self.map[Point(x, y)] = int(c) 
                    
        xs = [p.x for p in self.map.keys()]
        ys = [p.y for p in self.map.keys()]
        self.xlims = (0, max(xs))
        self.ylims = (0, max(ys))

def loadInput():
    lines = readInput("prova.txt")
    #lines = readInput("input_17.txt")
    lavatube = Lavatube()
    lavatube.load(lines)
    return lavatube

dirs = {0:lambda c:c + complex(0,1),
        1:lambda c:c + complex(1,0),
        2:lambda c:c + complex(0,-1),
        3:lambda c:c + complex(-1,0),}

class State:
    def __init__(self, start, _dir, count=1):
        self.pos = start
        self.cost = 0
        #self.prev = None
        self.dir = _dir
        self.dir_count = count

    def totuple(self):
        return (self.cost, self.pos.x, self.pos.y, self.dir.x, self.dir.y, self.dir_count)
        
    def __repr__(self):
        return f"({self.cost}, {self.pos.x}, {self.pos.y}, ({self.dir.x}, {self.dir.y}), {self.dir_count})"

    def totuple2(self):
        return (self.pos.x, self.pos.y, (self.dir.x, self.dir.y), self.dir_count)

    def __lt__(self, obj):
        return self.totuple() < obj.totuple()
#        
#        #print ("PIPPO5")
#        if self.cost == obj.cost:
#            if self.pos.x == obj.pos.y:
#                if self.pos.y == obj.pos.y:
#                    pippo1 = (self.dir.x, self.dir.y)
#                    pippo2 = (obj.dir.x, obj.dir.y)
#                    if pippo1 == pippo2:
#                        return self.dir_count < obj.dir_count
#                    return pippo1 > pippo2
#                return self.pos.y < obj.pos.y
#            return self.pos.x < obj.pos.x
#        return self.cost < obj.cost
    
    #def __le__(self, obj):
    #    print ("PIPPO4")
    #    if self.cost == obj.cost:
    #        return self.dir.x <= obj.dir.x
    #    return self.cost <= obj.cost

    #def __eq__(self, obj):
    #    #print ("PIPPO")
    #    return self.cost == obj.cost

    #def __ne__(self, obj):
    #    print ("PIPPO3")
    #    return self.cost != obj.cost
    #
    #def __gt__(self, obj):
    #    print ("PIPPO2")
    #    return self.cost > obj.cost
    #
    #def __ge__(self, obj):
    #    print ("PIPPO1")
    #    return self.cost >= obj.cost
    
def get_neighs(state, m):
    new_dir = [state.dir-1, state.dir, state.dir+1]
    new_states = []
    for i, d in enumerate(new_dir):
        if i == 1 and state.forward == 3:
            continue
        new_state = deepcopy(state)
        new_state.dir = d%4
        new_state.pos = dirs[new_state.dir](new_state.pos)
        if new_state.pos in m.map:
            if i == 1:
                new_state.forward += 1
            else:
                new_state.forward = 1
            new_states.append(new_state)
    return new_states

def backtrack(visited, start, target):
    d = target
    path = [target]
    print (d)
    while d != start:
        path.append(visited[d].prev)
        d = visited[d].prev
        print (d)
    return list(reversed(path))

Right = Point(1, 0)
Down = Point(0, 1)
Left = Point(-1, 0)
Up = Point(0, -1)

def dijkstra_bis(m, start, target, min_conse, max_conse):
    visited = set()
    worklist = [State(start, Right, 1), State(start, Down, 1)]
    #pq = PriorityQueue()
    #pq.put(worklist[0])
    #pq.put(worklist[1])
    
    #while not pq.empty():
    i = 0
    while len(worklist) > 0:
        #print (f"-------------- {i} ----------------")
        #current = pq.get() 
        current = heapq.heappop(worklist)
        #print (current)
        x = current.pos.x
        y = current.pos.y
        dir = current.dir
        dir_count = current.dir_count
        #print ("visited", visited)
        if current.totuple2() in visited:
            continue
        else:
            visited.add(current.totuple2())#(x, y, dir, dir_count))
            
        new_pos = Point(x + dir.x, y + dir.y)
        #print ("new_pos", new_pos)
        if new_pos not in m.map:
            continue
        new_cost = current.cost + m.map[new_pos]
        if dir_count >= min_conse and dir_count <= max_conse:
            if new_pos == target:
               # print (new_cost)
                #print (backtrack(visited, start, target))
                return new_cost
            
        for d in [Right, Down, Left, Up]:
            if (d.x + dir.x, d.y+dir.y) == (0, 0):
                continue
            new_d_count = dir_count + 1 if d == dir else 1
            if (d != dir and dir_count < min_conse) or new_d_count > max_conse:
                continue
            new_state = State(new_pos, d, new_d_count)
            new_state.cost = new_cost
            new_state.prev = current.pos
            #print ("d:", d)
            heapq.heappush(worklist, new_state)
            #pq.put(new_state)
        #print ("worklist", worklist)
        i += 1
        #if i == 28:
        #    break
    print ("worklist", worklist)
    
def part1(lavatube):
    start = Point(0, 0)
    target = Point(lavatube.xlims[1], lavatube.ylims[1])
    cost = dijkstra_bis(lavatube, start, target, 0, 3)
    return cost

def part2(lavatube):
    start = Point(0, 0)
    target = Point(lavatube.xlims[1], lavatube.ylims[1])
    cost = dijkstra_bis(lavatube, start, target, 4, 10)
    return cost

if __name__ == '__main__':
    print(" Day 17:  Clumsy Crucible ")
    print("--------------------------")
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

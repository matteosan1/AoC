from itertools import combinations
import heapq

part = 2
if part == 1:
    strontium, plutonium, thulium, ruthenium, curium = 1, 2, 3, 4, 5
    initial = (0, (
        tuple(sorted((strontium, -strontium, plutonium, -plutonium))),
        tuple(sorted((thulium, ruthenium, -ruthenium, curium, -curium))),
        (-thulium,),
        ())
    )
else:
    strontium, plutonium, thulium, ruthenium, curium, elerium, dilithium = 1, 2, 3, 4, 5, 6, 7
    initial = (0, (
        tuple(sorted((strontium, -strontium, plutonium, -plutonium, elerium, -elerium, dilithium, -dilithium))),
        tuple(sorted((thulium, ruthenium, -ruthenium, curium, -curium))),
        (-thulium,),
        ())
    )
    
def correct(floor):
    if not floor or floor[-1] < 0: # no generators
        return True
    return all(-chip in floor for chip in floor if chip < 0)

frontier = []
heapq.heappush(frontier, (0, initial))
cost_so_far = {initial: 0}

while frontier:
    _, current = heapq.heappop(frontier)
    floor, floors = current
    if floor == 3 and all(len(f) == 0 for f in floors[:-1]): # goal!
        break

    directions = [d for d in (-1, 1) if 0 <= floor + d < 4]
    moves = list(combinations(floors[floor], 2)) + list(combinations(floors[floor], 1))
    for move in moves:
        for direction in directions:
            new_floors = list(floors)
            new_floors[floor] = tuple(x for x in floors[floor] if x not in move)
            new_floors[floor+direction] = tuple(sorted(floors[floor+direction] + move))
            if not correct(new_floors[floor]) or not correct(new_floors[floor+direction]):
                continue

            next = (floor+direction, tuple(new_floors))
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost - len(new_floors[3])*5 # silly manually tweakable heuristic factor
                heapq.heappush(frontier, (priority, next))

if part == 1:
    print ("🎄Part 1: {} {}".format(cost_so_far[current], current))
else:
    print ("🎁🎄Part 2: {} {}".format(cost_so_far[current], current))

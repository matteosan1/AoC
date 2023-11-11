import copy
from itertools import combinations

#floors = {1:["SG", "SM", "PG", "PM"], 2:["TG", "RG", "RM", "CG", "CM"], 3:["TM"], 4:[]}
floors = {1:["HM", "LM"], 2:["HG"], 3:["LG"], 4:[]}
#floors = {1:["HM", "LM"], 2:[], 3:[], 4:[]}
elevator = 1

def check_radiation(b, floor):
    floor = floor + [item for item in b]
    radiation = False
    for c in floor:
        if c[1] == "G" and c[0]+"M" not in floor:
            radiation = True
            break
    
    if radiation:
        for c in floor:
            if c[1] == "M" and c[0]+"G" not in floor:
                return False

    return True

def possible_moves(elevator, floors):
    #print (elevator, floors)
    moves = []
    to_bring = [[item] for item in floors[elevator]]
    if len(floors[elevator]) > 1:
        for p in combinations(floors[elevator], 2):
            #print (p)
            if p[0][0] != p[1][0] and p[0][1] != p[1][1]:
                continue
            to_bring.append(list(p))

    #print (to_bring)
    for delta_floor in [-1, 1]:
        new_elevator = elevator + delta_floor
        if new_elevator < 1 or new_elevator > 4:
            continue
        
        #print (to_bring, new_elevator, floors[new_elevator])
        for b in to_bring:
            if check_radiation(b, floors[new_elevator]):
                new_floors = copy.deepcopy(floors)
                new_floors[new_elevator] += b
                new_floors[new_elevator] = sorted(new_floors[new_elevator])
                for item in b:
                    new_floors[elevator].remove(item)
                moves.append((new_elevator, new_floors))
    return moves

states = []
seeds = [(1, elevator, floors)]
steps = 0
while len(seeds) != 0:
    s = seeds.pop(0)
    states.append(copy.deepcopy(s))
    #print ("50 ", s[1], s[2])
    moves = possible_moves(s[1], s[2])
    if len(s[2][4]) == 4:
        #print(s)
        for t in states:
            print (t)
        quit()

    mini_states = [s[1:] for s in states]
    for m in moves:
        if m not in mini_states:
            print (m, states)
            seeds.append((s[0]+1, *m))
    #print ("SEEDS: ", seeds)
    #steps += 1
    #if steps == 3:
    #    break


import time, heapq
from utils import readInput

def loadInput():
    lines = readInput("input_5.txt")

    orderings = []
    updates = []
    for l in lines:
        if "|" in l:
            orderings.append(list(map(int, l.split("|"))))
        elif "," in l:
            updates.append(list(map(int, l.split(","))))
        else:
            continue

    return  orderings, updates


def part1(orderings, updates):
    mid_page = 0
    ordered = []
    for iu, upd in enumerate(updates):
        for x in range(len(upd)-1):
            if [upd[x], upd[x+1]] not in orderings:
                break
        else:
            ordered.append(iu)
            mid_val = upd[len(upd)//2]
            mid_page += mid_val

    print (f"🎄 Part 1: {mid_page}")
    return ordered

from copy import deepcopy
def finder(upd, orderings):
    new_orderings = [o for o in orderings if o[0] in upd and o[1] in upd]   
    for page in upd:
        queue = [[page]]        
        while len(queue) > 0:
            #print (queue)
            path = queue.pop()
            current = path[-1]
            #print ("current ", current)
            for o in new_orderings:
                #print ("ord", o)
                if current == o[0] and o[1] in upd:
                    new_path = deepcopy(path) + [o[1]]
                    #print ("AGGIUNTO", new_path)
                    if len(new_path) == len(upd):
                        return new_path
                    queue.append(new_path)
                    #print ("queue ", queue)
    return None

def part2(orderings, updates, ordered):
    mid_page = 0
    print (len(updates))
    for iu, upd in enumerate(updates):
        if iu in ordered:
            continue
        print (iu)
        new_order = finder(upd, orderings)
        #print (new_order)
        mid_val = new_order[len(new_order)//2]
        mid_page += mid_val
        
    print (f"🎄🎅 Part 2: {mid_page}")

if __name__ == "__main__":
    title = "Day 5: Print Queue"
    sub = "⛄"*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub) #"⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    
    inputs = loadInput()
    
    t0 = time.time()
    ordered = part1(*inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(*inputs, ordered)
    print ("Time: {:.5f}".format(time.time()-t0))

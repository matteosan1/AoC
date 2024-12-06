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

def part2(orderings, updates, ordered):
    mid_page = 0
    for iu, upd in enumerate(updates):
        if iu in ordered:
            continue
        new_orderings = [o for o in orderings if o[0] in upd and o[1] in upd]   
        rank = {}
        for u in upd:
            rank[u] = 0
            for o in new_orderings:
                if o[1] == u:
                    rank[u] += 1
        sorted_dict = list(dict(sorted(rank.items(), key=lambda item: item[1])).keys())
        mid_page += sorted_dict[len(sorted_dict)//2]
        
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

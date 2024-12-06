import time, heapq
from utils import readInput

def loadInput():
    lines = readInput("input_6.txt")

    area = {}
    start = None
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == ".":
                area[complex(x, y)] = 0
            elif lines[y][x] == "^":
                area[complex(x, y)] = 0
                start = complex(x, y)
            elif lines[y][x] == "#":
                area[complex(x, y)] = 1
            
    return  area, start

movements = {0: complex(0, -1), 1: complex(1, 0),
             2: complex(0, 1), 3: complex(-1, 0)}

def patroling(area, start):
    face = 0
    pos = start
    distincts = set([pos])
    try:
        while True:
            if area[pos + movements[face]] == 1:
                face = (face+1)%4
            pos += movements[face]
            distincts.add(pos)
    except Exception as e:
        pass
    return distincts
    
def part1(area, start):
    distincts = patroling(area, start)
    print (f"🎄 Part 1: {len(distincts)}")
    
def part2(area, start):
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
    title = "Day 6: Guard Gallivant"
    sub = "⛄"*(len(title)//2-1+2)

    print()
    print(f" {title} ")
    print(sub) #"⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(*inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    # t0 = time.time()
    # part2(*inputs, ordered)
    # print ("Time: {:.5f}".format(time.time()-t0))

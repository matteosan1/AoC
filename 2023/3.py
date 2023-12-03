import time, re
from utils import readInput

def loadInput():
    lines = readInput("input_3.txt")
    return lines

def isvalid_pos(px, py, inputs):
    if px < 0 or py < 0:
        return False
    try:
        inputs[py][px]
        return True
    except IndexError:
        return False
    
def check(inputs, px, py, gear=None):
    dirs = [(0,-1), (1, -1), (1, 0),
            (1, 1), (0, 1), (-1, 1),
            (-1, 0), (-1, -1)]
    for d in dirs:
        new_x = px + d[0]
        new_y = py + d[1]
        if not isvalid_pos(new_x, new_y, inputs):
            continue
        c = inputs[new_y][new_x]
        if gear is None:
            if not c.isdigit() and  c != '.':
                return True
        else:
            if c == "*":
                return (new_x, new_y)
    return None

def part1(inputs):
    lx = len(inputs[0])
    ly = len(inputs)
    numbers = []
    for y in range(ly):
        store = False
        number = ""
        attached = None
        for x in range(lx):
            c = inputs[y][x]
            if c.isdigit():
               store = True
               number += c
               if not attached:
                   if check(inputs, x, y):
                       attached = True
            else:
                if store and attached:
                    numbers.append(int(number))
                store = False
                number = ""
                attached = None
        if store and attached:
            numbers.append(int(number))
        
    print (f"🎄 Part 1: {sum(numbers)}")

def part2(inputs):
    lx = len(inputs[0])
    ly = len(inputs)
    numbers = []
    for y in range(ly):
        store = False
        number = ""
        attached = None
        for x in range(lx):
            c = inputs[y][x]
            if c.isdigit():
               store = True
               number += c
               if attached is None:
                   attached = check(inputs, x, y, "*")
            else:
                if store and attached is not None:
                    numbers.append((int(number), attached))
                store = False
                number = ""
                attached = None
        if store and attached is not None:
            numbers.append((int(number), attached))

    gears = {}
    for n, pos in numbers:
        gears.setdefault(pos, []).append(n)

    tot = 0
    for k, v in gears.items():
        if len(v) == 2:
            tot += v[1]*v[0]
            
    print (f"🎄🎅 Part 2: {tot}")

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 3         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print (f"Time: {time.time()-t0:.5f}")

t0 = time.time()
part2(inputs)
print (f"Time: {time.time()-t0:.5f}")

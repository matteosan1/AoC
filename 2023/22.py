import time

from utils import readInput

def loadInput():
    lines = readInput("input_22.txt")
    xs = []
    for l in lines:        
        xs.append(list(map(int, l.replace("~", ",").split(","))))
    xs.sort(key=lambda b: b[2])
    
    wall = []
    for x,y,z,i,j,k in xs:
        b = []
        for c1 in range(x, i+1):
            b.append((c1, y, z))
        for c2 in range(y, j+1):
            b.append((x, c2, z))
        for c3 in range(z, k+1):
            b.append((x, y, c3))
        wall.append(set(b))
    return wall
    
def fall_down(wall, floor=set()):
    count = 0
    for i in range(len(wall)):
        brick = wall[i]
        start_pos = brick
        while True:
            if any(b[2]==1 for b in brick) or any((x, y, z-1) in floor for (x, y, z) in brick):
                break
            brick = [(x, y, z-1) for (x, y, z) in brick]
        if brick != start_pos:
            count += 1
        floor.update(brick)
        wall[i] = brick
    return count

def check_safety(wall, brick):
    idx = wall.index(brick)
    new_wall = wall[idx+1:]
    floor = []
    for b in wall[:idx]:
        for x in b:
            if x not in brick:
                floor.append(x)
    c = fall_down(new_wall, set(floor))
    return c == 0, c

def part1(wall):
    safe = 0
    fall_down(wall)
    for b in wall:
        safe += check_safety(wall, b)[0]
    return safe

def part2(wall):
    tot = 0
    for b in wall:
        tot += check_safety(wall, b)[1]
    return tot

if __name__ == '__main__':
    title = "Day 22: Sand Slabs"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

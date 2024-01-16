import time, numpy as np, copy

from numpy import array_equal

from utils import readInput

def arreq_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if array_equal(elem, myarr)), False)
    
def loadInput():
    lines = readInput("input_10.txt")
    asteroids = []
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c  == "#":
                asteroids.append(np.array([x, y]))
    return asteroids

def part1(asteroids):
    seen = []
    for a in asteroids:
        angles = []
        for x in asteroids:
            if np.all(a == x):
                continue
            angles.append(np.arctan2(x[1]-a[1], x[0]-a[0]))
        seen.append(len(set(angles)))
    print (f"ðŸŽ„ Part 1: {max(seen)}")
    return asteroids[seen.index(max(seen))]
    
def angle(a):
    val = np.arctan2(a[1],a[0])
    if val < -np.pi/2:
        val += 2*np.pi + np.pi/2
    elif val >= -np.pi/2:
        val += np.pi/2
    return val
    
def show_map(asteroids, vaporized, station):
    v = [v[0] for v in vaporized]
    a = [a[0] for a in asteroids]
    xs = [x[0] for x in a]
    ys = [x[1] for x in a]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            p = np.array([x, y])
            if np.all(p == np.array([0,0])):
                print ("S", end='')
            elif arreq_in_list(p, v):
                print ("0", end='')
            elif arreq_in_list(p, a):
                print ("#", end='')
            else:
                print (" ", end='')
        print ()
    
def create_asteroid(a):
    return (a, angle(a), np.sqrt(a[0]**2+a[1]**2))
    
def part2(asteroids, station):
    asteroids = [create_asteroid(a-station) for a in asteroids]
    sorted_ast = sorted(asteroids, key=lambda x: (x[1], x[2]))
    n = 0
    vaporized = []
    while len(sorted_ast) != 0:
        prev = None
        left_over = []
        for i in range(len(sorted_ast)):
            if sorted_ast[i][2] == 0.0:                
                continue
            if sorted_ast[i][1] == prev:
                left_over.append(sorted_ast[i])
                #print ("left ", sorted_ast[i][0]+station, sorted_ast[i][1:])
            else:
                n += 1
                vaporized.append(sorted_ast[i])
                #print (f"vaporized {n}", sorted_ast[i][0]+station, sorted_ast[i][1:])
                if n == 200:
                    pos = sorted_ast[i][0]+station
                    print (f"ðŸŽ„ðŸŽ… Part 2: {pos[0]*100+pos[1]}")
                    return
                prev = sorted_ast[i][1]
        sorted_ast = copy.deepcopy(left_over)

if __name__ == "__main__":
    title = "Day 10: Monitoring Station"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    station = part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs, station)
    print ("Time: {:.5f}".format(time.time()-t0))

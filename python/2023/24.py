import time
import numpy as np, z3

from itertools import combinations

from utils import readInput

def loadInput():
    lines = readInput("input_24.txt")
    hails = []
    for l in lines:
        vals = list(map(int, l.replace(" @ ", ", ").split(", ")))
        hails.append((np.array(vals[:3]), np.array(vals[3:])))
    return hails

#def second_point(h):
#    return (h[0]+h[3], h[1]+h[4], h[2]+h[5], *h[3:])
#
#def det(x1, x2, x3, x4, y1, y2, y3, y4):
#    den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
#    if den == 0:
#        return None, None
#    x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/den
#    y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/den
#    return x,y
#
#def check_past(h, x, y):
#    if (x - h[0])*h[3] < 0:
#        return True
#    return False
#    
#def check_collision(h1, h3, lmin, lmax):
#    h2 = second_point(h1)
#    h4 = second_point(h3)
#    x, y = det(h1[0], h2[0], h3[0], h4[0],
#               h1[1], h2[1], h3[1], h4[1])
#    
#    if x is None:
#        #print ("parallel")
#        return False

#    if check_past(h1, x, y) or check_past(h3, x, y):
#        #print ("past crossing")
#        return False
#
#    # outside region
#    if not lmin <= x <= lmax or not lmin <= y <= lmax:
#        #print ("outside")
#        return False
#    return True

def collisions(h1, h2, lmin, lmax):
    A = np.vstack([h1[1][:2], -h2[1][:2]]).T
    b = h2[0][:2]-h1[0][:2]

    try:
        t1, t2 = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        #print ("parallel")
        return False

    if t1 < 0 or t2 < 0:
        #print ("past crossing")
        return False
    
    p = h1[1]*t1 + h1[0]
    if not all(lmin <= coord <= lmax for coord in p[:2]):
        #print ("outside ")
        return False
    #print ("OK")
    return True

def part1(hails):
    tot = 0
    for h1, h2 in combinations(hails, 2):
        if collisions(h1, h2, 200000000000000, 400000000000000):
            tot += 1
    return tot

def part2(hails):
    x, y, z, u, v, w = map(z3.Int, "xyzuvw")
    ts = [z3.Int(f"t{i}") for i in range(len(hails))]
    s = z3.Solver()
    for t, c in zip(ts, hails):
        s.add(x+t*u == c[0][0]+t*c[1][0])
        s.add(y+t*v == c[0][1]+t*c[1][1])
        s.add(z+t*w == c[0][2]+t*c[1][2])
    s.check()
    m = s.model()
    p2 = sum(m[c].as_long() for c in (x, y, z))        
    return p2

if __name__ == '__main__':
    title = "Day 24: Never Tell Me The Odds"
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

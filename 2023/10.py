# https://en.wikipedia.org/wiki/Shoelace_formula
# https://en.wikipedia.org/wiki/Pick%27s_theorem

import numpy as np
import time
from math import ceil

from utils import readInput

def loadInput():
    lines = readInput("input_10.txt")
    sketch = {}
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == ".":
                continue
            key = complex(x, y)
            if c == 'S':
                start = complex(x, y)
            sketch[key] = c
            
    return start, sketch

def part1(start, sketch):
    dirs = {0: complex(0,-1), 1: complex(1,0), 2: complex(0,1), 3: complex(-1,0)}
    moves = {'J': [-1, 0, 3, -1],
             '|': [0, -1, 2, -1],
             '-': [-1, 1, -1, 3],
             'F': [1, -1, -1, 2],
             '7': [3, 2, -1, -1],
             'L': [-1, -1, 1, 0]}
    
    farthest = 0
    starting_point = ""
    farthest_path = []
    for s, possible_moves in moves.items():
        sketch[start] = s
        for i, m in enumerate(possible_moves):
            path = []
            if m == -1:
                continue
            dir = m
            pos = start
            steps = 0
            loop = True
            while True:
                path.append(pos)
                new_pos = pos + dirs[dir]
                if new_pos not in sketch:
                    loop = False
                    break
                new_dir = moves[sketch[new_pos]][dir]
                if new_dir == -1:
                    loop = False
                    break
                if new_pos == start:
                    break
                steps += 1
                pos = new_pos
                dir = new_dir
            if loop:
                f = ceil(steps/2)
                if farthest < f:
                    farthest = f
                    starting_point = sketch[start]
                    farthest_path = path
    print (f"🎄 Part 1: {farthest}")
    return farthest_path

def det(p1, p2):
    return p1[0]*p2[1] - p1[1]*p2[0]

def schoelace(points):
    A = 0
    for i in range(len(points)):
        if i == len(points)-1:
            A += det(points[i], points[0])
        else:
            A += det(points[i], points[i+1])
    return abs(A/2)

def get_angles(vec_1,vec_2):
    dot = np.dot(vec_1, vec_2)
    det = np.cross(vec_1,vec_2)
    angle_in_rad = np.arctan2(det,dot)
    return np.degrees(angle_in_rad)

def make_vec(p1, p2):
    return ((p1[0]-p2[0], p1[1]-p2[1]))

def keep_vertices(path): 
    vertices = []
    for i, p in enumerate(path):
        if i == 0:
            v1 = make_vec(p, path[-1])
        else:
            v1 = make_vec(p, path[i-1])
        if i == len(path)-1:
            v2 = make_vec(path[0], p)
        else:
            v2 = make_vec(path[i+1], p)
        angle = get_angles(v1, v2)
        if angle != 0:
            vertices.append(p)
    return vertices

def part2(path):
    poly = []
    for p in path:
        poly.append((p.real, p.imag))
    
    vertices = keep_vertices(poly)
    
    A = schoelace(vertices)
    b = len(path)
    i = A + 1 - b/2
    print (f"🎄🎅 Part 2: {i}")
    
def part2_v2(path):
    import shapely

    x = [int(x.real) for x in path]
    y = [int(x.imag) for x in path]
    xmin, xmax = min(x), max(x)
    ymin, ymax = min(y), max(y)
    
    poly = []
    for p in path:
        poly.append((p.real, p.imag))
    
    polygon = shapely.Polygon(poly)
    contained = 0
    for row in range(ymin, ymax+1):
        for col in range(xmin, xmax+1):
            if (col, row) not in poly:
                contained += polygon.contains(shapely.Point(col, row))
    print (f"🎄🎅 Part 2: {contained}")

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 10        ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

start, sketch = loadInput()

t0 = time.time()
path = part1(start, sketch)
print (f"Time: {time.time()-t0:.5f}")

t0 = time.time()
part2(path)
print (f"Time: {time.time()-t0:.5f}")

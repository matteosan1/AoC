import time
from operator import methodcaller
import numpy as np

from utils import readInput

class Brick:
    def __init__(self):
        self.c1 = [0, 0, 0]
        self.c2 = [0, 0, 0]

    def __lt__(self, other):
        return self.c1[2] < other.c1[2]
        
    def __repr__(self):
        return f"{self.c1} - {self.c2}"
            

def loadInput():
    lines = readInput("prova.txt")
    #lines = readInput("input_22.txt")
    wall = []
    for l in lines:
        b = Brick()
        c1, c2 = list(map(methodcaller("split", ","), l.split("~")))
        if c1[0] > c2[0] or c1[1] > c2[1] or c1[2] > c2[2]:
            c2, c1 = c1, c2
        b.c1 = list(map(int, c1))
        b.c2 = list(map(int, c2))
        wall.append(b)
    return wall
    
def check_collision(b1, b2): #c1, c2, d1, d2):
    print (b1, b2)
    fall = [False, False]
    for k in range(2):
        if b2.c1[k] <= b1.c2[k] <= b2.c2[k] or b2.c1[k] <= b1.c1[k] <= b2.c2[k] or (b1.c1[k] < b2.c1[k] and b1.c2[k] > b2.c2[k]):
            fall[k] = True
    return all(fall)
        
        

def part1(wall):
    wall.sort()
    while True:
        fall = False
        for i in range(len(wall)):
            if wall[i].c1[2] == 1:
                continue
            z = wall[i].c1[2]
            collision = False
            for j in range(i):
                if wall[j].c1[2] != z - 1:
                    continue
                c = check_collision(wall[j], wall[i])
                if c:
                    collision = True
                    break
            if not collision:
                fall = True
                wall[i].c1[2] -= 1
                wall[i].c2[2] -= 1
        wall.sort()
        if not fall:
            break
        
    for b in wall:
        print (b)
    return 0

def part2(inputs):
    return 0

if __name__ == '__main__':
    title = "Day 22: Cube Conundrum"
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

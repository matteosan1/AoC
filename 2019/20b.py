from utils import readInput
import numpy as np
from itertools import combinations

class Particle:
    def __init__(self, i, p, v, a):
        self.n = i
        self.p = np.array(p)
        self.a = np.array(a)
        self.v = np.array(v)

    def move(self):
        self.v += self.a
        self.p += self.v

    def distance(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

lines = readInput("input_20.txt")
particles = []
for i, l in enumerate(lines):
    parts = l.split(">,")
    p = list(map(int, parts[0][3:].split(",")))
    v = list(map(int, parts[1][4:].split(",")))
    a = list(map(int, parts[2][4:-1].split(",")))
    particles.append(Particle(i, p, v, a))

print (len(particles))
min_dist = None
for t in range(1000):
    for p in particles:
        p.move()

    if t>9:
        collide = []
        for c in combinations(range(len(particles)), 2):
            if c[0] in collide or c[1] in collide:
                continue
            #print (i, j)
            if (particles[c[0]].p == particles[c[1]].p).all():
                #print (particles[i].p, particles[j].p)
                collide.append(c[0])
                collide.append(c[1])
        particles = [p for p in particles if p.n not in set(collide)]
        #min_dist = min([p.distance() for p in particles])
        #idx = [p.distance() for p in particles].index(min_dist)
        print (len(particles))
#print ([p.distance() for p in particles])
print (len(particles))
print (particles[0].n)
#print ("🎁🎄Part 2: {}".format(count))

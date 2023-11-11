from utils import readInput
import numpy as np

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

min_dist = None
for t in range(1000):
    for p in particles:
        p.move()

    min_dist = min([p.distance() for p in particles])
    idx = [p.distance() for p in particles].index(min_dist)

#print ([p.distance() for p in particles])
print (idx)

print ("🎄Part 1: {}".format(idx))

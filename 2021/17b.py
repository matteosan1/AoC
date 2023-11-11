from utils import readInput
import numpy as np

lines = readInput("input_17.txt")
target_x = lines[0].split(",")[0].split("x=")[1].split("..")
target_x = list(map(int, target_x))
target_y = lines[0].split(",")[1].split("y=")[1].split("..")
target_y = list(map(int, target_y))

good_vx = []
for vx in range(target_x[1]+1):
    distance = 0
    v = vx
    record = ()
    for steps in range(1, vx+1):
        distance += v
        v -= 1
        if record == () and target_x[0] <= distance <= target_x[1]:
            record = (steps, np.inf)
        if distance > target_x[1]:
            if record != ():
                record = (record[0], steps-1)
            break
    if record != ():
        good_vx.append((vx, record))

good_vy = []
for vy in range(target_y[0], 100):
    distance = 0
    v = vy
    record = ()
    for steps in range(1, 1000):
        distance += v
        v -= 1
        if record == () and target_y[0] <= distance <= target_y[1]:
            record = (steps, np.inf)
        if distance < target_y[0]:
            if record != ():
                record = (record[0], steps-1)
            break
    if record != ():
        good_vy.append((vy, record))

def getOverlap(a, b):
    return max(0, min(a[1], b[1]) - max(a[0], b[0]) + 1)

v = []
for gy in good_vy:
    for gx in good_vx:
        if getOverlap(gx[1], gy[1]) > 0:
            v.append((gx[0], gy[0]))

print ("🎄🎅 Part 2: {}".format(len(v)))

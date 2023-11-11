from utils import readInput, printTraj
import numpy as np

lines = readInput("input_17.txt")
target_x = lines[0].split(",")[0].split("x=")[1].split("..")
target_x = list(map(int, target_x))
target_y = lines[0].split(",")[1].split("y=")[1].split("..")
target_y = list(map(int, target_y))

#offset = (0, 50)
#cm = np.zeros(shape=(100, 100))
#cm[target_x[0]+offset[0]:target_x[1]+offset[0],
#   target_y[0]+offset[0]:target_y[1]+offset[1]] = 1
#   
#v = (6, 9)
#points = sim(*v, target_x, target_y)
#print (points)
#printTraj(cm, points, offset)

good_vx = []
for vx in range(0, target_x[1]+1):
    distance = 0
    steps = -1
    record = ()
    for s, i in enumerate(range(vx, -1, -1)):
        distance += i
        if target_x[0] <= distance <= target_x[1]:
            record = (s, np.inf)
        if distance > target_x[1]:
            if record != ():
                record = (record[0], s)
            break
    if record != ():
        good_vx.append((vx, record))

#print (good_vx)

good_vy = []
for vy in range(10000):
    distance = 0
    v = vy
    d_max_temp = 0
    for steps in range(1000):
        distance += v
        d_max_temp = max(distance, d_max_temp)
        v -= 1
        if target_y[0] <= distance <= target_y[1]:
            good_vy.append((vy, steps+1, d_max_temp))
            break

v = []
v0y = max(good_vy, key=lambda x: x[2])
print ("🎄 Part 1: {}".format(v0y[2]))
#for g in good_vx:
#    if g[1][0] <= v0y[2] <=g[1][1]:
#        v.append((g[0], v0y[0]))
#print (v)

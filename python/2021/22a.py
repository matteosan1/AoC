from utils import readInput
import numpy as np

cuboids = []
lines = readInput("input_22.txt")
for l in lines:
    x = list(map(int, l.split("x=")[1].split(",")[0].split("..")))
    y = list(map(int, l.split("y=")[1].split(",")[0].split("..")))
    z = list(map(int, l.split("z=")[1].split("..")))
    if l.startswith("on"):
        cuboids.append([x, y, z, 1])
    else:
        cuboids.append([x, y, z, 0])

offsetx = (-50, 50)
offsety = (-50, 50)
offsetz = (-50, 50)
cm = np.zeros(shape=(101, 101, 101))
              
for c in cuboids:
    for x in range(max(offsetx[0], c[0][0]), min(offsetx[1], c[0][1])+1):
        for y in range(max(offsety[0], c[1][0]), min(offsety[1], c[1][1])+1):
            for z in range(max(offsetz[0], c[2][0]), min(offsetz[1], c[2][1])+1):
                cm[x, y, z] = c[3]

print ("🎄 Part 1: {}".format((cm==1).sum()))


    

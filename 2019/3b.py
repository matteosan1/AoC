wires = []

def path(s, direction):
    steps = int(direction[1:])

    if direction.startswith("R"):
        p = [(s[0]+i, s[1]) for i in range(1, steps+1)]
    elif direction.startswith("L"):
        p = [(s[0]-i, s[1]) for i in range(1, steps+1)]
    elif direction.startswith("U"):
        p = [(s[0], s[1]-i) for i in range(1, steps+1)]
    elif direction.startswith("D"):
        p = [(s[0], s[1]+i) for i in range(1, steps+1)]
    return p

with open("input3a.txt", "r") as f:
    for i, l in enumerate(f):
        l = list(l.split("\n")[0].split(","))
        wires.append(l)

#wires[0] = ["R8","U5","L5","D3"]
#wires[1] = ["U7","R6","D4","L4"]
#wires[0] = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
#wires[1] = ["U62","R66","U55","R34","D71","R55","D58","R83"]
#wires[0] = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
#wires[1] = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]

origin = (0, 0)
paths = [[origin], [origin]]

for iw in range(2):
    for w in wires[iw]:
        paths[iw] += path(paths[iw][-1], w)

#cross = []
#for y in range(-10, 1):
#    for x in range(10):
#        p = [x, y]
#        if p in paths[0] and p in paths[1]:
#            #print ("X", end=""),
#            cross.append(p)
#        #elif p in paths[0] or p in paths[1]:
#        #    print ("*", end=""),
#        #else:
#        #    print (".", end=""),
#    #print ("\n")

cross = set(paths[0]).intersection(paths[1])

min_steps = 10000000000
min_steps_point = (0, 0)
for c in cross:
    steps = paths[0].index(c) + paths[1].index(c)
    if steps < min_steps and steps != 0:
        min_steps = steps
        min_steps_point = c

print (min_steps, min_steps_point)

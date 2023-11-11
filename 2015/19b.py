import re
from random import shuffle

transf = []

with open("instructions19a.txt", "r") as f:
    lines = f.readlines()

for l in lines[:-2]:
    l = l.split("\n")[0]
    items = l.split(" ")

    transf.append((items[0], items[2]))
molecule = lines[-1]
    
reps = transf
target = molecule
part2 = 0

while target != 'e':
    tmp = target
    for a, b in reps:
        if b not in target:
            continue

        target = target.replace(b, a, 1)
        part2 += 1

    if tmp == target:
        target = molecule
        part2 = 0
        shuffle(reps)

print (part2)

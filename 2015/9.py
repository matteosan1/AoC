from itertools import permutations

filename = "instructions9a.txt"
with open(filename, "r") as f:
    data = f.readlines()

distances = {}

for d in data:
    d = d.split("\n")[0]
    items = d.split(" ")
    distances.setdefault(items[0], {}).update({items[2]:int(items[4])})
    distances.setdefault(items[2], {}).update({items[0]:int(items[4])})

min_dist = 1000000000000
max_dist = 0
for p in permutations(distances.keys()):
    dist = 0
    for i in range(len(p)-1):
        dist += distances[p[i]][p[i+1]]

    if dist < min_dist:
        min_dist = dist

    if dist > max_dist:
        max_dist = dist
        
print (min_dist)
print (max_dist)

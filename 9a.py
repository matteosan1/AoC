filename = "instructions9a.txt"
#filename = "examples8b.txt"
with open(filename, "r") as f:
    data = f.readlines()

def findMinimum(d, keys):
    kmin = None
    min = max(d.values())
    for k, v in d.items():
        if k not in keys:
            continue
        if v < min:
            kmin = k
            min = v
    return kmin

distances = {}

for d in data:
    d = d.split("\n")[0]
    items = d.split(" ")
    distances.setdefault(items[0], {}).update({items[2]:int(items[4])})
    distances.setdefault(items[2], {}).update({items[0]:int(items[4])})

for k in distances.keys():
    keys = list(distances.keys())
    keys.remove(k)
    dist = 0
    print (k)
    while len(keys) != 0:
        kmin = findMinimum(distances[k], keys)
        dist += distances[k][kmin]
        keys.remove(kmin)
        k = kmin
    print (dist)
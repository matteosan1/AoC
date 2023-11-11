from itertools import permutations

filename = "instructions13a.txt"
#filename = "instructions13b.txt"

with open(filename, "r") as f:
    data = f.readlines()

happiness = {}

for d in data:
    d = d.split("\n")[0]
    items = d.split(" ")
    if items[2] == "lose":
        happiness.setdefault(items[0], {}).update({items[-1][:-1]: (-1)*int(items[3])})
    else:
        happiness.setdefault(items[0], {}).update({items[-1][:-1]: int(items[3])})

perm = list(permutations(list(happiness.keys())))
happinesses = []

for p in perm:
    happyness = 0
    for f in range(len(p)):
        if f == (len(p) - 1):
            happyness += happiness[p[f]][p[0]] + happiness[p[0]][p[f]]
        else:
            happyness += happiness[p[f]][p[f+1]] + happiness[p[f+1]][p[f]]
    happinesses.append(happyness)
    #print ("Start ", p, happiness)
print (max(happinesses))

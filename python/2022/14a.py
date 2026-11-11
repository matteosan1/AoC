from utils import readInput

filename = "input_14.txt"
lines = readInput(filename)

polymer = None
insertion = {}
for i, l in enumerate(lines):
    if l.strip() == "":
        continue
    if i == 0:
        polymer = l
    else:
        items = l.split("->")
        insertion[items[0].strip()] = items[1].strip()

for s in range(10):
    new_polymer = ""
    for i in range(len(polymer)-1):
        key = polymer[i:i+2]
        new_polymer += polymer[i] + insertion[key]
        #print (i, key, new_polymer)

    polymer = new_polymer + polymer[-1]
    #print (polymer)

counts = {}
for p in polymer:
    counts[p] = counts.setdefault(p, 0) + 1

kmax = max(counts, key=counts.get)
kmin = min(counts, key=counts.get)

print ("🎄 Part 1: {}".format(counts[kmax] - counts[kmin]))

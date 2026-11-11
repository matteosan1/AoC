from utils import readInput
from collections import Counter

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

def count_for_cicle(polymer, patterns, cicle):
    elements = Counter(polymer)
    parts = Counter([polymer[i] + polymer[i + 1] for i in range(len(polymer) - 1)])
    for _ in range(cicle):
        parts, old_parts = Counter(), parts

        for (a, b), add in patterns.items():
            parts[a + add] += old_parts[a + b]
            parts[add + b] += old_parts[a + b]
            elements[add] += old_parts[a + b]
    return elements

counts = count_for_cicle(polymer, insertion, 40)

kmax = max(counts, key=counts.get)
kmin = min(counts, key=counts.get)
print ("🎄🎅 Part 2: {}".format(counts[kmax] - counts[kmin]))

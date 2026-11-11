from utils import readInput
from itertools import combinations

lines = readInput("input_2.txt")

checksum = 0
for l in lines:
    parts = list(map(int, l.split()))
    for c in combinations(sorted(parts), 2):
        if c[1]%c[0] == 0:
            checksum += c[1]/c[0]
    
print ("🎁🎄Part 2: {}".format(checksum))

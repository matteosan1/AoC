from itertools import combinations
import math
from functools import reduce

filename = "instructions24a.txt"

nums = list(map(int, [line.strip("\n") for line in open(filename)]))
part = 2
if part == 1:
    parts = 3
else:
    parts = 4
tot = sum(nums)/parts

def hasSum(lst, sub):
    for y in range(1, len(lst)):
        for x in (z for z in combinations(lst, y) if sum(z) == tot):
            if sub == 2:
                return True
            elif sub < parts:
                return hasSum(list(set(lst) - set(x)), sub - 1)
            elif hasSum(list(set(lst) - set(x)), sub - 1):
                return math.prod(x)
print (hasSum(nums, parts))

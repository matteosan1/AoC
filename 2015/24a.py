import itertools
import operator
from functools import reduce

# presents = []
filename = "instructions24a.txt"
# with open(filename, "r") as f:
#     for i, l in enumerate(f):
#         presents.append(int(l))


nums = list(map(int, [line.strip("\n") for line in open(filename)]))
parts = 4
tot = sum(nums)/parts

def hasSum(lst, sub):
    for y in range(1,len(lst)):
        for x in (z for z in itertools.combinations(lst, y) if sum(z) == tot):
            if sub == 2:
                return True
            elif sub < parts:
                return hasSum(list(set(lst) - set(x)), sub - 1)
            elif hasSum(list(set(lst) - set(x)), sub - 1):
                return reduce(operator.mul, x, 1)
print (hasSum(nums, parts))

# tot_weight = sum(presents) // 3
# #print (tot_weight)
#
# good_sacks = []
# for mask in range(1 << len(presents)+1):
#     if mask % 1000 == 0:
#         print (mask, len(good_sacks))
#     sack = []
#     for j, p in enumerate(presents):
#         if p > tot_weight:
#             continue
#         if (mask & (1 << j)) > 0:
#             sack.append(p)
#     if sum(sack) == tot_weight:
#         good_sacks.append(sack)
#
# real_good_sacks = []
# legroom = 1000000
# from itertools import combinations
# for c in combinations(good_sacks, 3):
#     tot = c[0] + c[1] + c[2]
#     if len(set(tot)) == len(tot):
#         if len(c[0]) < legroom:
#             real_good_sacks = [c]
#             legroom = len(c[0])
#         elif len(c[0]) == legroom:
#             real_good_sacks.append(c)
#
# for c in real_good_sacks:
#     print (c)
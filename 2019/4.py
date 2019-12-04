"""
low = [1,3,0,2,5,4]
high = [6,7,8,2,7,5]

good = 0
for i1 in range(low[0], high[0]+1):
    for i2 in range(i1, high[1] + 1):
        for i3 in range(i2, high[2] + 1):
            for i4 in range(i3, 10):
                for i5 in range(i4, 10):
                    for i6 in range(i5, 10):
                        n = ("{}{}{}{}{}{}".format(i1,i2,i3,i4,i5,i6))
                        if int(n) < 678275 and int(n) > 130254:
                            if i1 == i2 or i2 == i3 or i3 == i4 or i4 == i5 or i5 == i6:
                                print (n)
                                good += 1

print (good)
"""

from collections import defaultdict

# from common import InputForDay

# This time input was given right away, in the task description
# indata = InputForDay(4).get()
left  = 130254
right = 678275

# Convert a number to a list of digits.
digits = lambda n: [int(x) for x in str(n)]

def hasTwoAdjacent(n: list):
    for i, k in enumerate(n[1:]):
        if n[i] == k:
            return True
    return False

def neverDecreases(n: list):
    for i, k in enumerate(n[1:]):
        if n[i] > k:
            return False
    return True

ans = map(digits, range(left, 1 + right))
ans = filter(hasTwoAdjacent, ans)
ans = filter(neverDecreases, ans)
ans = list(ans)
print("Part 1: {}".format(len(ans)))

def hasExactlyTwoAdjacent(n: list):
    # Store adjacent digits and see if any of the digits repeat exactly two
    # times.
    d = defaultdict(int)
    for i in n:
        d[i] += 1
    return 2 in d.values()

print("Part 2: {}".format(len(list(filter(hasExactlyTwoAdjacent, ans)))))
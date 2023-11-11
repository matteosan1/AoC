import itertools
from collections import Counter

def solve(p1, p2):
    p1 -= 1
    p2 -= 1
    u1 = u2 = 0

    universes = Counter([(p1, 0, p2, 0), ])
    dice_count = Counter(sum(p) for p in itertools.product([1, 2, 3], repeat=3))

    while universes:
        newones = Counter()
        for u, uc in universes.items():
            for d, c in dice_count.items():
                pos = (u[0] + d) % 10
                score = u[1] + pos + 1
                if score >= 21:
                    u1 += c*uc
                    continue
                newones[(pos, score, u[2], u[3])] += c*uc
        universes = newones.copy()

        newones = Counter()
        for u,uc in universes.items():
            for d, c in dice_count.items():
                pos = (u[2] + d) % 10
                score = u[3] + pos + 1
                if score >= 21:
                    u2 += c*uc
                    continue
                newones[(u[0], u[1], pos, score)] += c*uc
        universes = newones.copy()

    print ("🎄🎅 Part 2: {}".format(max(u1, u2)))
solve(9, 6)

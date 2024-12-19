import timeit

from functools import cache
from utils import readInput

# Try solution with TRIE
# provare ad aggiungere memoization alla mia soluzione dovrebbe funzionare ugualmente

def loadInput():
    #lines = readInput("input_19_prova.txt")
    lines = readInput("input_19.txt")

    designs = []
    towels = lines[0].split(", ")
    for i in range(1, len(lines)):
        designs.append(lines[i])
    return frozenset(towels), designs

def remove_prefix(prefix, word):
    return word[len(prefix) :]

@cache
def check_design(design, towels):
    if not design:
        return True
    vals = []
    for towel in towels:
        if design.startswith(towel):
            vals.append(check_design(remove_prefix(towel, design), towels))
    return sum(vals)

def part1(towels, designs):
    found = 0
    for design in designs:
        found += (check_design(design, towels) != 0)
# def part1(towels, designs):
#     found = 0
#     for design in designs:
#         q = [0]
#         seen = set([])
#         while q:
#             l = heapq.heappop(q)
#             l = -l
#             seen.add(design[:l])
#             if l == len(design):
#                 found += 1
#                 break

#             for t in towels:
#                 if l + len(t) > len(design):
#                     continue
#                 if design[l:l+len(t)] == t:
#                     if design[:l+len(t)] not in seen:
#                         heapq.heappush(q, -l-len(t))
    print (f"🎄 Part 1: {found}")

def part2(towels, designs):
    found = 0
    for design in designs:
        found += (check_design(design, towels))
    print (f"🎄🎅 Part 2: {found}")

if __name__ == '__main__':
    title = "Day 19: "
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(*inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    t2 = timeit.timeit(lambda: part2(*inputs), number=1)
    print (f"{t2*1000:.3f} ms")


# with open("input_19_prova.txt") as f:
#     towels = [p.strip() for p in f.readline().split(",")]
#     designs = [line.strip() for line in f if line.strip()]

# # Build trie
# def build_trie(towels):
#     root = {}
#     for t in towels:
#         d = root
#         for color in t:
#             if color not in d:
#                 d[color] = {}
#             d = d[color]
#         d[''] = None
#     return root

# @functools.cache
# def ways(design, trie):
#     return _ways(design, trie)

# def _ways(design, d={}):
#     if not design:
#         return 1 if '' in d else 0
    
#     nways = ways(design) if '' in d else 0
        
#     ch = design[0]
#     if ch in d:
#         return nways + _ways(design[1:], d[ch])
#     else:
#         return nways

# def part1(towels, designs):
#     trie = build_trie(towels)
#     res = 0
#     for design in designs:
#         if ways(design) > 0:
#             res += 1
#     print res

# part1(towels, designs)
# #print(sum(1 for design in designs if ways(design)>0))
# #print(sum(map(ways, designs)))
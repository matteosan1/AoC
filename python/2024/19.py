import time

from functools import cache

from utils import readInput

# Try solution with TRIE
# provare ad aggiungere memoization alla mia soluzione dovrebbe funzionare ugualmente

def loadInput(filename: str):
    lines = readInput(filename)

    designs = []
    towels = lines[0].split(", ")
    for i in range(1, len(lines)):
        designs.append(lines[i])
    return frozenset(towels), designs

@cache
def check_design(design, towels):
    if not design:
        return 1
    res = 0
    for towel in towels:
        if design.startswith(towel):
            res += check_design(design[len(towel):], towels)
    return res

def part1(towels, designs):
    found = sum([check_design(design, towels) != 0 for design in designs])
    print (f"🎄 Part 1: {found}", end='')

def part2(towels, designs):
    found = 0
    for design in designs:
        found += (check_design(design, towels))
    print (f"🎄🎅 Part 2: {found}", end='')

if __name__ == '__main__':
    title = "Day 19: Linen Layout"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_19.txt")
    
    t0 = time.time()
    part1(*inputs)
    print (" - {:.6f} s".format(time.time()-t0))
    
    t0 = time.time()
    part2(*inputs)
    print (" - {:.6f} s".format(time.time()-t0))


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
with open("plants2.txt", "r") as f:
    lines = f.readlines()

state = "###.......##....#.#.#..###.##..##.....#....#.#.....##.###...###.#...###.###.#.###...#.####.##.#....#"

import collections
import re

def nextg(cur, recipe):
  start = min(cur)
  end = max(cur)
  x = set()

  for i in range(start - 3, end + 4):
    pat = ''.join('#' if i + k in cur else '.' for k in [-2, -1, 0, 1, 2])
    if pat in recipe:
      x.add(i)

  return x

def viz(cur):
  print (''.join('#' if i in cur else '.' for i in range(-5, 120)))

#with open('day12test.txt') as f:
with open('plants.txt') as f:
  lines = [l.rstrip('\n') for l in f]
  print (lines)

  init = lines[0][len('initial state: '):]
  recipe = set()
  for l in lines[2:]:
    if l[-1] == '#':  # I forgot this line the first time around.
      recipe.add(l[:5])

  cur = set(i for i, c in enumerate(init) if c == '#')

# Part 1:
#for i in range(20):
#    cur = nextg(cur, recipe)
#print (sum(cur))

# Part 2:
ls = 0
# viz(cur)
for i in range(2000):
  cur = nextg(cur, recipe)
  # viz(cur)
  s = sum(cur)
  print (i, s, s - ls)
  ls = s
print (sum(cur))
print ((50000000000 - 2000) * 52 + sum(cur))
# #state = "...#..#.#..##......###...###........."
# rules = {}
# for l in lines:
#     items = l.split("\n")[0].split()
#     rules[items[0]] = items[2]
#
#
# offset = 2
# nplants = state.count("#")
# for s in range(20):
#     nstate = len(state)
#     i=offset
#     new_state = state[:offset]
#     while i < (nstate-2):
#         p = state[i-2:i+3]
#         if p in rules.keys():
#             new_state = new_state + rules[p]
#         else:
#             new_state = new_state + "."
#         i = i + 1
#
#     index = new_state.find("#")
#     if index < 3:
#         new_state = "..." + new_state
#
#     index = new_state.rfind("#")
#     if index >= (len(new_state)-3):
#         new_state = new_state + "..."
#
#     print ("{}: {}".format(s+1, new_state))
#
#     state = new_state
#     nplants = nplants + new_state.count("#")
#     print (nplants)
#
#
# a = """
#  0: ...#..#.#..##......###...###...........
#  1: ...#...#....#.....#..#..#..#...........
#  2: ...##..##...##....#..#..#..##..........
#  3: ..#.#...#..#.#....#..#..#...#..........
#  4: ...#.#..#...#.#...#..#..##..##.........
#  5: ....#...##...#.#..#..#...#...#.........
#  6: ....##.#.#....#...#..##..##..##........
#  7: ...#..###.#...##..#...#...#...#........
#  8: ...#....##.#.#.#..##..##..##..##.......
#  9: ...##..#..#####....#...#...#...#.......
# 10: ..#.#..#...#.##....##..##..##..##......
# 11: ...#...##...#.#...#.#...#...#...#......
# 12: ...##.#.#....#.#...#.#..##..##..##.....
# 13: ..#..###.#....#.#...#....#...#...#.....
# 14: ..#....##.#....#.#..##...##..##..##....
# 15: ..##..#..#.#....#....#..#.#...#...#....
# 16: .#.#..#...#.#...##...#...#.#..##..##...
# 17: ..#...##...#.#.#.#...##...#....#...#...
# 18: ..##.#.#....#####.#.#.#...##...##..##..
# 19: .#..###.#..#.#.#######.#.#.#..#.#...#..
# 20: .#....##....#####...#######....#.#..##.
# """
# z = """
# 16: ...#..#...#.#...##...#...#.#..##..##.....
# 194
# 17: ...#..##...#.#.#.#...##...#....#...#...
# 206
# 18: ...#...#....#####.#.#.#...##...##..##...
# 222
# 19: ...##..##..#.#.#######.#.#.#..#.#...#....
# 241
# 20: ..#.#...#...#####...#######....#.#..##....
# """
# b = a.split(":")
# c = 0
# for i in b:
#     c = c + (i.count("#"))
#     print (c)
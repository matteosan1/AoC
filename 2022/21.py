from utils import readInput
import time

def part1():
    ingredients = []
    allergens = set([])
    receipts = []
    with open("input_21.txt") as f:
        for i, l in enumerate(f):
            l = l.split("\n")[0]
            items = l.split(" (contains ")
            ingr = items[0].split(" ")
            receipts.append(ingr)
            a = items[1][:-1].split(", ")
            for i in a:
                allergens.add(i)
                ingredients.append((i, ingr))

    all_ingredients = []
    for ing in ingredients:
        all_ingredients += ing[1]

    all_ingredients = set(all_ingredients)
    
    final = {}
    for a in allergens:
        for ing in ingredients:
            if a == ing[0]:
                if a in final:
                    final[a] = final[a].intersection(set(ing[1]))
                else:
                    final[a] = set(ing[1])

    while True:
        removed = False
        for k,v in final.items():
            v = list(v)
            if len(v) == 1:
                for k1 in final:
                    if k != k1:
                        if v[0] in final[k1]:
                            final[k1].remove(v[0])
                            removed = True

        if not removed:
            break

    ok = []
    for v in final.values():
        ok.append(list(v)[0])
    ok = all_ingredients - set(ok)

    val = 0
    for r in receipts:
        for o in ok:
            if o in r:
                val += 1

    print ("🎄 Part 1: {}".format(val))
    return final

def part2(ok):
    ing = [list(ok[k])[0] for k in sorted(ok)]
    print ("🎄🎅 Part 2: {}".format(",".join(ing)))
    
t0 = time.time()
ok = part1()
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(ok)
print ("Time: {:.5f}".format(time.time()-t0))

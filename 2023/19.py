import time, json

from utils import readInputWithBlank

def loadInput():
    lines = readInputWithBlank("prova.txt")
    lines = readInputWithBlank("input_19.txt")
    conditions = {}
    parts = []
    conds = True
    for l in lines:
        if l == "":
            conds = False
            continue
        if conds:
            p = l.split("{")
            name = p[0]
            val = p[1][:-1].split(",")
            c = []
            for v in val[:-1]:
                operation, dest = v.split(":")
                c.append([operation[0], operation[1], int(operation[2:]), dest])
            c.append([val[-1]])
            conditions[name] = c
        else:
            vals = l[1:-1].split(",")
            temp = {}
            for val in vals:
                k, v = val.split("=")
                temp.update({k:int(v)})
            parts.append(temp)
    return conditions, parts
    
def check_condition(part, name, conditions):
    if name == 'A':
        return True
    elif name == 'R':
        return False
    condition = conditions[name]
    for c in condition:
        if len(c) == 1:
            return check_condition(part, c[0], conditions)
        else:
            if c[1] == '>':
                if part[c[0]] > c[2]:
                    return check_condition(part, c[3], conditions)
            elif c[1] == '<':
                if part[c[0]] < c[2]:
                    return check_condition(part, c[3], conditions)

def branch_conditions(name, conditions, rules, branch=[]):
    if name == 'A':
        rules.append(branch)
    elif name != 'R':
        condition = conditions[name]
        rul = []
        for c in condition[:-1]:
            branch_conditions(c[-1], conditions, rules, branch + rul + [c[:-1]])
            if c[1] == '<':
                rul.append([c[0], '>=', c[2]])
            elif c[1] == '>':
                rul.append([c[0], '<=', c[2]])
        branch_conditions(condition[-1][0], conditions, rules, branch+rul)
                    
def part1(conditions, parts):
    rating = 0
    for part in parts:
        if check_condition(part, "in", conditions):
            rating += sum(part.values())
    return rating
    
def part2(conditions):
    rules = []
    branch_conditions('in', conditions, rules)
    tot = 0
    for branch in rules:
        mins = {k:0 for k in 'xmas'}
        maxs = {k:4001 for k in 'xmas'}
        for r in branch:
            if r[0] in 'xmas' and r[1][0] == '<':
                maxs[r[0]] = min(maxs[r[0]], r[2]+1) if len(r[1]) == 2 else min(maxs[r[0]], r[2])
            elif r[0] in 'xmas' and r[1][0] == '>':
                mins[r[0]] = max(mins[r[0]], r[2]-1) if len(r[1]) == 2 else max(mins[r[0]], r[2])
        p = 1
        for key in maxs:
            p *= (maxs[key] - mins[key] - 1)
        tot += p
    return tot

if __name__ == '__main__':
    title = "Day 19: Aplenty"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    conditions, parts = loadInput()

    t0 = time.time()
    res1 = part1(conditions, parts)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(conditions)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")
 
 
 
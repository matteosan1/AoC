# provare ad implementare con il BFS (problema degli else)
import time, json
from collections import deque

from utils import readInputWithBlank

def loadInput():
    lines = readInputWithBlank("prova.txt")
    #lines = readInputWithBlank("input_19.txt")
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

def find_paths(conditions, start='in', target='A'):
    q = []
    q.append([start])
    paths = []

    while len(q) != 0:
        path = q.pop(0)
        pos = path[-1]
        if pos not in conditions:
            if pos == target:
                paths.append(path)
        else:            
            for c in conditions[pos]:
                new_path = list(path) + [c[-1]]
                q.append(new_path)

    return paths

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
    #for part in parts:
    #    if check_condition(part, "in", conditions):
    #        rating += sum(part.values())
    return rating
    
#def part2_orig(conditions):
#    rules = []
#    branch_conditions('in', conditions, rules)
#    tot = 0
#    for branch in rules[:10]:
#        mins = {k:0 for k in 'xmas'}
#        maxs = {k:4001 for k in 'xmas'}
#        for r in branch:
#            if r[0] in 'xmas' and r[1][0] == '<':
#                maxs[r[0]] = min(maxs[r[0]], r[2]+1) if len(r[1]) == 2 else min(maxs[r[0]], r[2])
#            elif r[0] in 'xmas' and r[1][0] == '>':
#                mins[r[0]] = max(mins[r[0]], r[2]-1) if len(r[1]) == 2 else max(mins[r[0]], r[2])
#        p = 1
#        for key in maxs:
#            print (maxs[key], mins[key], (maxs[key] - mins[key] - 1))
#            p *= (maxs[key] - mins[key] - 1)
#        tot += p
#        print (tot)
#    return tot

def part2_v2(conditions):
    rules = []
    branch_conditions('in', conditions, rules)
    print (rules)
    tot = 0
    for branch in rules:
        ranges = {k:set(range(1, 4001)) for k in 'xmas'}
        for r in branch:
            if r[1] == '<':
                ranges[r[0]] -= set(range(r[2], 4001))
            elif r[1] == '<=':
                ranges[r[0]] -= set(range(r[2]+1, 4001))
            elif r[1] == '>':
                ranges[r[0]] -= set(range(1, r[2]+1))
            elif r[1] == '>=':
                ranges[r[0]] -= set(range(1, r[2]))

        p = 1  
        for key in 'xmas':
            p *= len(ranges[key])
        tot += p
    return tot

def get_rules(rules, dest):
    print (rules, dest)
    for i, r in enumerate(rules):
        if r[-1] == dest:
            if i == 0:
                return [r[:-1]]
            else:
                new_r = []
                for rule in rules[:i]:
                    if rule[1] == '<':
                        rule[1] = '>='
                    else:
                        rule[1] = '<='
                    print (rule[:-1])
                    new_r.append(rule[:-1])
                new_r.append(r[:-1])
                return new_r
#            new_r = []
#            if i == 0:
#                new_r.append(r[:-1])        
#            else:
#                for r_star in rules[:i]:                
#                if len(r) != 1:
#                    new_r.append(r[:-1])
#            return new_r
    return None

def part2(conditions):
    paths = find_paths(conditions)
    
    tot = 0
    for path in paths:
        ranges = {k:set(range(1, 4001)) for k in 'xmas'}
        print (path)
        for ip in range(1, len(path)):
            rules = get_rules(conditions[path[ip-1]], path[ip])
            print (rules)
            for r in rules:
                print (r)
                if r[1] == '<':
                    ranges[r[0]] -= set(range(r[2], 4001))
                elif r[1] == '<=':
                    ranges[r[0]] -= set(range(r[2]+1, 4001))
                elif r[1] == '>':
                    ranges[r[0]] -= set(range(1, r[2]+1))
                elif r[1] == '>=':
                    ranges[r[0]] -= set(range(1, r[2]))

        p = 1  
        for key in 'xmas':
            p *= len(ranges[key])
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
    res2 = part2_v2(conditions)
    res2 = part2(conditions)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")
#[[['s', '<', 1351], ['a', '<', 2006], ['x', '<', 1416]], [['s', '<', 1351], ['a', '<', 2006], ['x', '>=', 1416], ['x', '>', 2662]], [['s', '<', 1351], ['a', '>=', 2006], ['m', '<=', 2090], ['s', '>=', 537], ['x', '<=', 2440]], [['s', '>=', 1351], ['s', '>', 2770], ['s', '>', 3448]], [['s', '>=', 1351], ['s', '>', 2770], ['s', '<=', 3448], ['m', '>', 1548]], [['s', '>=', 1351], ['s', '>', 2770], ['s', '<=', 3448], ['m', '<=', 1548]], [['s', '>=', 1351], ['s', '<=', 2770], ['m', '<', 1801], ['m', '>', 838]], [['s', '>=', 1351], ['s', '<=', 2770], ['m', '<', 1801], ['m', '<=', 838], ['a', '<=', 1716]]]

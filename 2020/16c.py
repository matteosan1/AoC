import numpy
import re
from collections import defaultdict
from dataclasses import dataclass

guide_re = re.compile(r'(?P<location>[\w ]+): (?P<a_from>\d+)-(?P<a_to>\d+) or (?P<b_from>\d+)-(?P<b_to>\d+)')


@dataclass
class Rule:
    name: str
    rule_a: range
    rule_b: range
    field: int = -1

    def __init__(self, name: str, a_from: int, a_to: int, b_from: int, b_to: int):
        self.name = name
        self.rule_a = range(int(a_from), int(a_to) + 1)
        self.rule_b = range(int(b_from), int(b_to) + 1)

    def __contains__(self, item: int):
        return item in self.rule_a or item in self.rule_b


mode = 0
rules = []
tickets = []
with open('input_16a.txt', 'r') as f:
    while f:
        if mode == 0:
            line = f.readline().strip()
            match = guide_re.match(line)
            if line == 'your ticket:':
                mode = 1
            elif match is not None:
                rules.append(Rule(*match.groups()))
        elif mode == 1:
            line = f.readline().strip().split(',')
            my_ticket = tuple([int(x) for x in line])
            f.readline()
            f.readline()
            mode = 2
        elif mode == 2:
            line = f.readline().strip().split(',')
            if not line[0].isdigit():
                break
            tickets.append(tuple([int(x) for x in line]))

error_rate = 0
for ticket in tickets:
    for num in ticket:
        valid = True
        if any([num in x for x in rules]):
            continue
        else:
            error_rate += num

print('Part 1:', error_rate)

valid_tickets = []
for ticket in tickets:
    if all([any([num in x for x in rules]) for num in ticket]):
        valid_tickets.append(ticket)

valid_rules = defaultdict(list)
rules_set = []

for ind, col in enumerate(zip(*valid_tickets)):
    for rule in rules:
        if all([n in rule for n in col]):
            valid_rules[ind].append(rule)

while valid_rules:
    for col, v_rules in valid_rules.items():
        if len(v_rules) == 1:
            v_rules[0].field = col
            rules_set.append(v_rules[0])
    valid_rules = {
        k: [r for r in v if r not in rules_set]
        for k, v in valid_rules.items() if k not in [j.field for j in rules]
    }

print('Part 2:', numpy.prod([my_ticket[r.field] for r in rules if r.name.startswith('departure')]))

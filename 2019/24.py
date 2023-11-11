# from utils import readLines
# import operator
#
# class Group:
#     def __init__(self, n, unit):
#         self.n = n
#         self.unit = unit
#
#     def effective_power(self):
#         return self.n * self.unit.attack_damage
#
#     def __repr__(self):
#         return str(self.n) + " " + str(self.effective_power())
#
# class Unit:
#     def __init__(self, hp, ad, at, initiative, immu, weak):
#         self.hit_points = hp #amount of damage a unit can take before it is destroyed
#         self.attack_damage = ad #amount of damage each unit deals
#         self.attack_type = at
#         self.initiative = initiative #higher initiative units attack first and win ties)
#         self.weaknesses = weak
#         self.immunities = immu
#
# lines = readLines("immune.txt")
#
# immunes = []
# for l in lines:
#     items = l.split(",")
#     u = Unit(int(items[1]), int(items[4].split()[0]), items[4].split()[1], int(items[5]), items[2].split()[1:], items[3].split()[1:])
#     immunes.append(Group(int(items[0]), u))
#
# lines = readLines("infection.txt")
#
# infections = []
# for l in lines:
#     items = l.split(",")
#     u = Unit(int(items[1]), int(items[4].split()[0]), items[4].split()[1], int(items[5]), items[2].split()[1:], items[3].split()[1:])
#     infections.append(Group(int(items[0]), u))
#
# # TARGET SELECTION
# immunes.sort(key=lambda c:int(c.n*c.unit.attack_damage), reverse=True)
# infections.sort(key=lambda c:int(c.n*c.unit.attack_damage), reverse=True)
# for g in immunes:
#     g_max = None
#     for i1, g1 in enumerate(infections):
#         for at in g.attack_type:
#             if at in g1.weaknesses:
#
#     print (g, g.n, g.unit.attack_damage)
#
#     If
#     an
#     attacking
#     group is considering
#     two
#     defending
#     groups
#     to
#     which
#     it
#     would
#     deal
#     equal
#     damage, it
#     chooses
#     to
#     target
#     the
#     defending
#     group
#     with the largest effective power; if there is still a tie, it chooses the defending group with the highest initiative.If it cannot deal any defending groups damage, it does not choose a target.Defending groups can only be chosen as a target by one attacking group.

import re


def binary_search(f, lo=0, hi=None):
    """
    Returns a value x such that f(x) is true.
    Based on the values of f at lo and hi.
    Assert that f(lo) != f(hi).
    """
    lo_bool = f(lo)
    if hi is None:
        offset = 1
        while f(lo + offset) == lo_bool:
            offset *= 2
        hi = lo + offset
    else:
        assert f(hi) != lo_bool
    best_so_far = lo if lo_bool else hi
    while lo <= hi:
        mid = (hi + lo) // 2
        result = f(mid)
        if result:
            best_so_far = mid
        if result == lo_bool:
            lo = mid + 1
        else:
            hi = mid - 1
    return best_so_far


inp = """
Immune System:
8233 units each with 2012 hit points (immune to radiation) with an attack that does 2 fire damage at initiative 5
2739 units each with 5406 hit points (immune to fire) with an attack that does 16 fire damage at initiative 3
229 units each with 6782 hit points (weak to slashing) with an attack that does 260 cold damage at initiative 7
658 units each with 12313 hit points with an attack that does 132 bludgeoning damage at initiative 4
3231 units each with 1872 hit points (weak to slashing, cold) with an attack that does 5 bludgeoning damage at initiative 1
115 units each with 10354 hit points (immune to fire, radiation, bludgeoning) with an attack that does 788 cold damage at initiative 2
1036 units each with 9810 hit points (weak to radiation) with an attack that does 94 bludgeoning damage at initiative 8
3389 units each with 6734 hit points with an attack that does 19 cold damage at initiative 18
2538 units each with 5597 hit points (weak to slashing, radiation) with an attack that does 15 slashing damage at initiative 16
6671 units each with 6629 hit points (immune to bludgeoning) with an attack that does 8 slashing damage at initiative 14

Infection:
671 units each with 17509 hit points with an attack that does 52 cold damage at initiative 12
7194 units each with 41062 hit points (immune to cold; weak to radiation) with an attack that does 11 bludgeoning damage at initiative 20
1147 units each with 37194 hit points (weak to radiation, fire) with an attack that does 56 slashing damage at initiative 11
569 units each with 27107 hit points (weak to slashing, bludgeoning) with an attack that does 93 slashing damage at initiative 17
140 units each with 19231 hit points (immune to slashing; weak to bludgeoning) with an attack that does 247 slashing damage at initiative 19
2894 units each with 30877 hit points (immune to radiation, bludgeoning) with an attack that does 15 radiation damage at initiative 10
1246 units each with 8494 hit points (weak to fire) with an attack that does 12 bludgeoning damage at initiative 9
4165 units each with 21641 hit points (weak to radiation; immune to fire) with an attack that does 10 radiation damage at initiative 6
7374 units each with 24948 hit points (weak to cold) with an attack that does 5 fire damage at initiative 13
4821 units each with 26018 hit points with an attack that does 10 fire damage at initiative 15
""".strip()


def doit(boost=0, part1=False):
    lines = inp.splitlines()
    immune, infection = inp.split("\n\n")

    teams = []

    REGEX = re.compile(
        r"(\d+) units each with (\d+) hit points (\([^)]*\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)")

    # namedtuple? who needs namedtuple with hacks like these?
    UNITS, HP, DAMAGE, DTYPE, FAST, IMMUNE, WEAK = range(7)

    blah = boost
    for inps in [immune, infection]:
        lines = inps.splitlines()[1:]
        team = []
        for line in lines:
            s = REGEX.match(line)
            units, hp, extra, damage, dtype, fast = s.groups()
            immune = []
            weak = []
            if extra:
                extra = extra.rstrip(" )").lstrip("(")
                for s in extra.split("; "):
                    if s.startswith("weak to "):
                        weak = s[len("weak to "):].split(", ")
                    elif s.startswith("immune to "):
                        immune = s[len("immune to "):].split(", ")
                    else:
                        assert False
            u = [int(units), int(hp), int(damage) + blah, dtype, int(fast), set(immune), set(weak)]
            team.append(u)
        teams.append(team)
        blah = 0

    def power(t):
        return t[UNITS] * t[DAMAGE]

    def damage(attacking, defending):
        mod = 1
        if attacking[DTYPE] in defending[IMMUNE]:
            mod = 0
        elif attacking[DTYPE] in defending[WEAK]:
            mod = 2
        return power(attacking) * mod

    def sort_key(attacking, defending):
        return (damage(attacking, defending), power(defending), defending[FAST])

    while all(not all(u[UNITS] <= 0 for u in team) for team in teams):
        teams[0].sort(key=power, reverse=True)
        teams[1].sort(key=power, reverse=True)

        targets = []

        # target selection
        for team_i in range(2):
            other_team_i = 1 - team_i
            team = teams[team_i]
            other_team = teams[other_team_i]

            remaining_targets = set(i for i in range(len(other_team)) if other_team[i][UNITS] > 0)
            my_targets = [None] * len(team)

            for i, t in enumerate(team):
                if not remaining_targets:
                    break
                best_target = max(remaining_targets, key=lambda i: sort_key(t, other_team[i]))
                enemy = other_team[best_target]
                if damage(t, enemy) == 0:
                    continue
                my_targets[i] = best_target
                remaining_targets.remove(best_target)
            targets.append(my_targets)

        # attacking
        attack_sequence = [(0, i) for i in range(len(teams[0]))] + [(1, i) for i in range(len(teams[1]))]
        attack_sequence.sort(key=lambda x: teams[x[0]][x[1]][FAST], reverse=True)
        did_damage = False
        for team_i, index in attack_sequence:
            to_attack = targets[team_i][index]
            if to_attack is None:
                continue
            me = teams[team_i][index]
            other = teams[1 - team_i][to_attack]

            d = damage(me, other)
            d //= other[HP]

            if teams[1 - team_i][to_attack][UNITS] > 0 and d > 0:
                did_damage = True

            teams[1 - team_i][to_attack][UNITS] -= d
            teams[1 - team_i][to_attack][UNITS] = max(teams[1 - team_i][to_attack][UNITS], 0)
        if not did_damage:
            return None

    if part1:
        return sum(u[UNITS] for u in teams[0]) or sum(u[UNITS] for u in teams[1])
    asd = sum(u[UNITS] for u in teams[0])
    if asd == 0:
        return None
    else:
        return asd


print(doit(part1=True))
# I did a manual binary search, submitted the right answer, then added in did_damage.
# Turns out that doit can infinite loop without the did_damage check!
# WARNING: "doit" is not guaranteed to be monotonic! You should manually check values yourself.
# print(doit(33))
maybe = binary_search(doit)
print(doit(maybe))
from itertools import combinations
from inputs_21 import *

def sim(choice, PP, PB, DB, AB):
    DP = weapons[choice[0]][1]
    AP = armors[choice[1]][1]
    ring1 = rings_p[choice[2][0]][1]
    ring2 = rings_p[choice[2][1]][1]
    ring3 = rings_m[choice[3][0]][1]
    ring4 = rings_m[choice[3][1]][1]

    while True:
        PB -= max(1, DP + ring1 + ring2 + AB)
        if PB <= 0:
            return True
        PP -= max(1, DB + AP + ring3 + ring4)
        if PP <= 0:
            return False
    
PB = 109
DB = 8
AB = -2
PP = 100

cost_max = 0
choice = (None, None)
rings_p_comb = list(combinations(rings_p.keys(), 2)) + [("No ring", "No ring")]
rings_m_comb = list(combinations(rings_m.keys(), 2)) + [("No ring", "No ring")]


for ak, av in armors.items():
    for kr2 in rings_m_comb:
        AP = av[1] + rings_m[kr2[0]][1] + rings_m[kr2[1]][1]
        no_ring1 = kr2.count("No ring")        
        for wk, wv in weapons.items():
            for kr1 in rings_p_comb:
                no_ring2 = kr1.count("No ring")
                if (no_ring2 + no_ring1) >= 2:
                    DP = wv[1] + rings_p[kr1[0]][1] + rings_p[kr1[1]][1]
                    choice = (wk, ak, kr1, kr2)
                    if not sim(choice, PP, PB, DB, AB):
                        cost = wv[0]+rings_p[kr1[0]][0]+rings_p[kr1[1]][0]+av[0]+rings_m[kr2[0]][0]+rings_m[kr2[1]][0]
                        if cost > cost_max:
                            print (choice, cost)
                            cost_max = cost

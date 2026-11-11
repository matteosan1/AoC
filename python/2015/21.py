import time

from itertools import combinations

from utils import readInput

weapons = {"Dagger" :[8, 4],
           "Shortsword":[10, 5],
           "Warhammer":[25, 6],
           "Longsword":[40, 7],
           "Greataxe":[74, 8]}

armors = {"None":[0,0],
          "Leather":[13, -1],
          "Chainmail":[31, -2],
          "Splintmail":[53, -3],
          "Bandedmail":[75, -4],
          "Platemail":[102, -5]}

rings_p = {"No ring":[0, 0],
           "Damage +1":[25, 1],
           "Damage +2":[50, 2],
           "Damage +3":[100, 3]}

rings_m = {"No ring":[0, 0],
           "Defense +1":[20, -1],
           "Defense +2":[40, -2],
           "Defense +3":[80, -3]}

def part1():
    power_b = 109
    damage_b = 8
    armor_b = -2
    hit_points = 100

    res = []
    cost_min = 500
    choice = (None, None)
    rings_p_comb = list(combinations(rings_p.keys(), 2)) + [("No ring", "No ring")]
    rings_m_comb = list(combinations(rings_m.keys(), 2)) + [("No ring", "No ring")]

    for k, v in weapons.items():
        for kr1 in rings_p_comb:
            A = -(v[1]+rings_p[kr1[0]][1] + rings_p[kr1[1]][1]+armor_b)/power_b*hit_points + damage_b
            for k1, v1 in armors.items():
                no_ring1 = kr1.count("No ring")
                for kr2 in rings_m_comb:
                    no_ring2 = kr2.count("No ring")
                    if no_ring2 + no_ring1 >= 2:
                        if (v1[1] + rings_m[kr2[0]][1] + rings_m[kr2[1]][1]) < -A:
                            cost = v[0] + rings_p[kr1[0]][0] + rings_p[kr1[1]][0] + v1[0] + rings_m[kr2[0]][0] + rings_m[kr2[1]][0]
                            if cost < cost_min:
                                choice = (k, k1, kr1, kr2)
                                print (choice, cost)
                                cost_min = cost

    print (f"🎄 Part 1: {cost_min}")

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

def part2():        
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
                                #print (choice, cost)
                                cost_max = cost
    print (f"🎄🎅 Part 2: {cost_max}")
    
if __name__ == "__main__":
    title = "Day 21: RPG Simulator 20XX"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    #inputs = loadInput()
    t0 = time.time()
    part1()
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2()
    print ("Time: {:.5f}".format(time.time()-t0))


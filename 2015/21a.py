from itertools import combinations

weapons = {
    "Dagger" :[8, 4],
    "Shortsword":[10, 5],
    "Warhammer":[25, 6],
    "Longsword":[40, 7],
    "Greataxe":[74, 8]
}

armors = {
    "Leather":[13, -1],
    "Chainmail":[31, -2],
    "Splintmail":[53, -3],
    "Bandedmail":[75, -4],
    "Platemail":[102, -5]
}

rings_p = {
    "No ring":[0, 0],
    "Damage +1":[25, 1],
    "Damage +2":[50, 2],
    "Damage +3":[100, 3]
}

rings_m = {
    "No ring":[0, 0],
    "Defense +1":[20, -1],
    "Defense +2":[40, -2],
    "Defense +3":[80, -3]
}

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

import sys
sys.exit()
damage = weapons[choice[0]][1]
armor = armors[choice[1]][1]
#damage = weapons["Shortsword"][1]
#armor = armors["Platemail"][1]
ring1 = rings_p[choice[2][0]][1]
ring2 = rings_p[choice[2][1]][1]

coeff = max(1, (damage_b + armor)) + min(0, ring1) + min(0, ring2)
coeff_b = max(1, (damage + armor_b)) + max(0, ring1) + max(0, ring2)
print ("COEFF: P {}, B {}".format(coeff_b, coeff))
while hit_points > 0 and power_b > 0:
    power_b -= coeff_b
    print ("Player hits: P {}, B {}".format(hit_points, power_b))
    if power_b <= 0:
#        print (hit_points, hit_points_b)
#        cost = w[0] + a[0] + r1[0] + r2[0]
#        choices.append((damage, armor, ring1, ring2, cost, coeff, coeff_b))
#        print (damage, armor, ring1, ring2, cost, coeff, coeff_b)
        break
    hit_points -= coeff
    print ("Boss hits: P {}, B {}".format(hit_points, power_b))
    
    


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

rings = {
"No ring":[0, 0],
"Damage +1":[25, 1],
"Damage +2":[50, 2],
"Damage +3":[100, 3],
"Defense +1":[20, -1],
"Defense +2":[40, -2],
"Defense +3":[80, -3]
}

damage_b = 9
armor_b = -2

choices = []
for kw, w in weapons.items():
    for aw, a in armors.items():
        for rw1, r1 in rings.items():
            for rw2, r2 in rings.items():
                if rw1 == rw2:
                    continue
                damage = w[1]
                armor = a[1]
                ring1 = r1[1]
                ring2 = r2[1]

                hit_points_b = 103
                hit_points = 100

                while hit_points_b > 0:
                    coeff = max(1, (damage_b + armor + min(0, ring1) + min(0, ring2)))
                    coeff_b = max(1, (damage + armor_b + max(0, ring1) + max(0, ring2)))
                    hit_points_b -= coeff_b
                    hit_points -= coeff
                    print (hit_points, hit_points_b)
                    if hit_points <= 0:
                        print (hit_points, hit_points_b)
                        cost = w[0] + a[0] + r1[0] + r2[0]
                        choices.append((damage, armor, ring1, ring2, cost, coeff, coeff_b))
                        print (damage, armor, ring1, ring2, cost, coeff, coeff_b)
                        break

print (max(choices, key=lambda x: x[4]))

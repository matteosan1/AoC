spacecrafts = []
with open("input1a.txt", "r") as f:
    for i, l in enumerate(f):
        spacecrafts.append(int(l))

fuel = 0
for w in spacecrafts:
    while True:
        delta_fuel = (w//3) - 2
        if delta_fuel <= 0:
            break

        fuel += delta_fuel
        w = delta_fuel

print (fuel)
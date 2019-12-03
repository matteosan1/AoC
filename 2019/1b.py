spacecrafts = []
with open("input1a.txt", "r") as f:
    for i, l in enumerate(f):
        spacecrafts.append(int(l))

fuel = 0
for w in spacecrafts:
    fuel += (w//3) - 2

print (fuel)
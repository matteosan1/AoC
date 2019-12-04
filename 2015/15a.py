
class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def property(self, spoons):
        return spoons * (max(0, self.capacity) +
                         max(0, self.durability) +
                         max(0, self.flavor) +
                         max(0, self.texture))

filename = "instructions15a.txt"
#filename = "examples14a.txt"

with open(filename, "r") as f:
    data = f.readlines()

ing = []
for d in data:
    d = d.split("\n")[0].split(" ")
    name = d[0][:-1]
    capacity = int(d[2][:-1])
    durability = int(d[4][:-1])
    flavor = int(d[6][:-1])
    texture = int(d[8][:-1])
    calories = int(d[10])
    ing.append(Ingredient(name, capacity, durability, flavor, texture, calories))

def tot_prop(x):
    tot = ing[0].property(x[0])
    tot += ing[1].property(x[1])
    tot += ing[2].property(x[2])
    tot += ing[3].property(x[3])

    return tot #+ 1000000 * abs(100 - sum(x))


#from scipy.optimize import brute, fmin

#bounds = [slice(0, 100, 1), slice(0, 100, 1), slice(0, 100, 1), slice(0, 100, 1)]
#result = brute(tot_prop, bounds, full_output=True, finish=fmin)

#print (result)

test = []
for i1 in range(0, 100, 1):
    for i2 in range(0, 100, 1):
        for i3 in range(0, 100, 1):
            for i4 in range(0, 100, 1):
                if (i1+i2+i3+i4) == 100:
                    test.append([i1,i2,i3,i4])

print ("combination done")
max_prop = 0
comb = None
for t in test:
    prop = tot_prop(t)
    if prop > max_prop:
        comb = t
        max_prop = prop


print (max_prop)
print (comb)



















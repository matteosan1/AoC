
class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.properties = [capacity, durability, flavor, texture, calories]

    def __repr__(self):
        return self.name + " " + str(self.properties)

def score(ingredients, spoons):
    properties = [0 for _ in range(5)]
    for i in range(5):
        for ii, ing in enumerate(ingredients):
            properties[i] += spoons[ii]*ing.properties[i]

    s = 1
    for p in properties[:-1]:
        s *= max(0, p)
    return s, properties[-1]

with open("instructions15a.txt", "r") as f:
    data = f.readlines()

ingredients =  []
for d in data:
    d = d.split("\n")[0].split(" ")
    ingredients.append(Ingredient(d[0], int(d[2][:-1]), int(d[4][:-1]),
                                  int(d[6][:-1]), int(d[8][:-1]), int(d[10])))

max_spoons = None
max_score = 0
for i1 in range(0, 101, 1):
    for i2 in range(0, 101, 1):
        for i3 in range(0, 101, 1):
            for i4 in range(0, 101, 1):
                if i1+i2+i3+i4 == 100:
                    spoons = [i1, i2, i3, i4]
        #if i1+i2 == 100:
            #spoons = [i1, i2]
                    s, p = score(ingredients, spoons)
                    if p == 500:
                        if s > max_score:
                            max_score = s
                            max_spoons = spoons
print (max_score)
import numpy as np
from itertools import product

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def property(self, spoons):
        return np.array([spoons * self.capacity,
                spoons * self.durability,
                spoons * self.flavor,
                spoons * self.texture])

filename = "instructions15a.txt"
#filename = "examples15.txt"

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

def tot_prop(q):
    totals = ing[0].property(q[0])
    #print (totals)
    for i in range(1, len(ing)):
        totals += ing[i].property(q[i])

    totals[totals<0] = 0
    #print (totals)
    return np.prod(totals)

def tot_calories(q):
    return sum([ing[i].calories*q[i] for i in range(len(ing))])
               
tot = 0
for p in product(range(101), repeat=len(ing)):
    if sum(p) != 100:
        continue
    if tot_calories(p) != 500:
        continue
    temp = tot_prop(p)
    #print (new_quants, temp)
    if temp >= tot:
        tot = temp
        idx = p

print (tot)


















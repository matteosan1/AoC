import time, numpy as np

from itertools import product

from utils import readInput

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

def loadInput():
    lines = readInput("instructions15a.txt")
    ing = []
    for d in lines:
        d = d.split(" ")
        name = d[0][:-1]
        capacity = int(d[2][:-1])
        durability = int(d[4][:-1])
        flavor = int(d[6][:-1])
        texture = int(d[8][:-1])
        calories = int(d[10])
        ing.append(Ingredient(name, capacity, durability, flavor, texture, calories))
    return ing

def tot_prop(ing, q):
    totals = ing[0].property(q[0])
    for i in range(1, len(ing)):
        totals += ing[i].property(q[i])

    totals[totals<0] = 0
    return np.prod(totals)

def part1(ing):
    tot = 0
    for p in product(range(101), repeat=len(ing)):
        if sum(p) != 100:
            continue
        temp = tot_prop(ing, p)
        if temp >= tot:
            tot = temp
            idx = p
    print (f"🎄 Part 1: {tot}")

def tot_calories(ing, q):
    return sum([ing[i].calories*q[i] for i in range(len(ing))])

def part2(ing):               
    tot = 0
    for p in product(range(101), repeat=len(ing)):
        if sum(p) != 100:
            continue
        if tot_calories(ing, p) != 500:
            continue
        temp = tot_prop(ing, p)
        if temp >= tot:
            tot = temp
            idx = p
    print (f"🎄🎅 Part 2: {tot}")
    
if __name__ == "__main__":
    title = "Day 15: Science for Hungry People"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))

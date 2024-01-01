import time, numpy as np

from itertools import combinations_with_replacement, permutations, combinations

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
        vals = [int(d[i][:-1]) if d[i].endswith(",") else int(d[i]) for i in (2, 4, 6, 8, 10)] 
        ing.append(Ingredient(name, *vals))
    return ing

def starting_solution(n):
    norm = 100
    solution = np.zeros(shape=(n,))
    for i in range(n-1):
        solution[i] = np.random.randint(norm-solution.sum())
    solution[0] = 27
    solution[-1] = norm - solution.sum()
    return solution.astype('int')

def shift_solution(ingredients, solution, c, max_score):
    if solution[c[0]] > 0 and solution[c[1]] < 100:
        solution[c[0]] -= 1
        solution[c[1]] += 1
        new_score = tot_prop(ingredients, solution)
        if new_score > max_score:
            max_score = new_score
            return (True, max_score)
        else:
            solution[c[0]] += 1
            solution[c[1]] -= 1
    return (False, max_score)
        
def optimize(ingredients):
    max_score = 0
    for _ in range(10):
        solution = starting_solution(len(ingredients))
        score = tot_prop(ingredients, solution)
        max_score = max(score, max_score)
        while True:
            for c in combinations(range(len(ingredients)), 2):
                res = shift_solution(ingredients, solution, c, max_score)
                if res[0]:
                    max_score = res[1]
                    break
                else:
                    c = c[::-1]
                    res = shift_solution(ingredients, solution, c, max_score)
                    if res[0]:
                        max_score = res[1]
                        break
            else:
                break
    return max_score

def tot_prop(ing, q):
    totals = ing[0].property(q[0])
    for i in range(1, len(ing)):
        totals += ing[i].property(q[i])

    totals[totals<0] = 0
    return np.prod(totals)

def part1(ingredients):
    tot = optimize(ingredients)
    print (f"🎄 Part 1: {tot}")

def tot_calories(ing, q):
    return sum([ing[i].calories*q[i] for i in range(len(ing))])

def part2(ing):
    tot = 0
    for c in combinations_with_replacement(range(101), len(ing)):
        if sum(c) != 100:
            continue
        for p in permutations(c, 4):
            if tot_calories(ing, p) != 500:
                continue
            tot = max(tot, tot_prop(ing, p))
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

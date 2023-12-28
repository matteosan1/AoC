import time

from itertools import permutations

from utils import readInput

def loadInput():
    lines = readInput("instructions13a.txt")
    happiness = {}

    for d in lines:
        items = d.split(" ")
        if items[2] == "lose":
            happiness.setdefault(items[0], {}).update({items[-1][:-1]: (-1)*int(items[3])})
        else:
            happiness.setdefault(items[0], {}).update({items[-1][:-1]: int(items[3])})
    return happiness

def compute_happiness(happiness):
    perm = list(permutations(list(happiness.keys())))
    happinesses = []

    for p in perm:
        happyness = 0
        for f in range(len(p)):
            if f == (len(p) - 1):
                happyness += happiness[p[f]][p[0]] + happiness[p[0]][p[f]]
            else:
                happyness += happiness[p[f]][p[f+1]] + happiness[p[f+1]][p[f]]
        happinesses.append(happyness)
    return happinesses

def part1(happiness):
    happinesses = compute_happiness(happiness)
    print (f"🎄 Part 1: {max(happinesses)}")

def part2(happiness):
    happiness["Matteo"] = {}
    for k in happiness.keys():
        happiness["Matteo"].update({k: 0})
        happiness[k].update({"Matteo":0})

    happinesses = compute_happiness(happiness)
    print (f"🎄🎅 Part 2: {max(happinesses)}")
    
if __name__ == "__main__":
    title = "Day 13: Knights of the Dinner Table"
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


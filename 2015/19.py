import time, re

from random import shuffle

from utils import readInput

def loadInput():
    transf = {}
    lines = readInput("instructions19a.txt")
    for l in lines[:-2]:
        items = l.split()
        transf.setdefault(items[0], []).append(items[2])
    molecule = lines[-1]
    return transf, molecule

def part1(transf, molecule):
    new_molecules = []
    molecules = 0
    for k in transf.keys():
        for m in re.finditer(k, molecule):
            for i in transf[k]:
                new_molecules.append(molecule[:m.start()] + i + molecule[m.start()+len(k):])

    new_molecules = set(new_molecules)
    print ()
    print (f"🎄 Part 1: {len(new_molecules)}")

def part2(transf, molecule):
    reps = []
    for k, v in transf.items():
        for item in v:
            reps.append((k, item))

    target = molecule
    steps = 0

    while target != 'e':
        tmp = target
        for a, b in reps:
            if b not in target:
                continue

            target = target.replace(b, a, 1)
            steps += 1

        if tmp == target:
            target = molecule
            steps = 0
            shuffle(reps)
            
    print (f"🎄🎅 Part 2: {steps}")
    
if __name__ == "__main__":
    title = "Day 19: Medicine for Rudolph"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(*inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(*inputs)
    print ("Time: {:.5f}".format(time.time()-t0))


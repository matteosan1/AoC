import time, re

from utils import readInput

r1 = re.compile("(\\d+):")
r2 = re.compile("(\\w+:\\s\\d+)")

class Aunt:
    def __init__(self, name, things):
        self.name = name
        self.things = things

    def check2(self, findings):
        matches = 0
        special = ('cat', 'tree', 'pomeranians', 'goldfish')
        for k, v in findings.items():
            if k in self.things.keys():
                if (k == "cats" or k == "trees") and v < self.things[k]:
                    matches += 1
                elif (k == "pomeranians" or k == "goldfish") and v > self.things[k]:
                    matches += 1
                elif (k not in special) and self.things[k] == v:
                    matches += 1
        return matches

    def check1(self, findings):
        matches = 0
        for k, v in findings.items():
            if k in self.things.keys() and v == self.things[k]:
                matches += 1
        return matches

mfcsam = {'children': 3,
          'cats': 7,
          'samoyeds': 2,
          'pomeranians': 3,
          'akitas': 0,
          'vizslas': 0,
          'goldfish': 5,
          'trees': 3,
          'cars': 2,
          'perfumes': 1}

def loadInput():
    lines = readInput("instructions16a.txt")
    aunts = []
    for d in lines:
        name = r1.findall(d)[0]
        temp = r2.findall(d)
        things = {}
        for k in temp:
            items = k.split(" ")
            things[items[0][:-1]] = int(items[1])
        aunts.append(Aunt(name, things))
    return aunts

def part1(aunts):
    aunt = -1
    best = 0
    for i, a in enumerate(aunts):
        m =  a.check1(mfcsam)
        if m >= best:
            aunt = i
            best = m
    print (f"🎄 Part 1: {aunts[aunt].name} {aunts[aunt].things}")

def part2(aunts):
    aunt = -1
    best = 0
    for i, a in enumerate(aunts):
        m =  a.check2(mfcsam)
        if m >= best:
            aunt = i
            best = m
    print (f"🎄🎅 Part 2: {aunts[aunt].name} {aunts[aunt].things}")
    
if __name__ == "__main__":
    title = "Day 16: Aunt Sue"
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


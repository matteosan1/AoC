import re
r1 = re.compile("(\d+):")
r2 = re.compile("(\w+:\s\d+)")

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

with open("instructions16a.txt", "r") as f:
    data = f.readlines()

aunts = []
for d in data:
    d = d.split("\n")[0]
    name = r1.findall(d)[0]
    temp = r2.findall(d)
    things = {}
    for k in temp:
        items = k.split(" ")
        things[items[0][:-1]] = int(items[1])
    aunts.append(Aunt(name, things))

part = 2
aunt = -1
best = 0
for i, a in enumerate(aunts):
    if part == 1:
        m =  a.check1(mfcsam)
    else:
        m =  a.check2(mfcsam)
    if m >= best:
        aunt = i
        best = m

print (aunts[aunt].name, aunts[aunt].things)

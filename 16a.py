import re
r1 = re.compile("(\d+):")
r2 = re.compile("(\w+:\s\d+)")

class Aunt:
    def __init__(self, name, things):
        self.name = name
        self.things = things

    def check(self, findings):
        matches = 0
        nt = len(self.things.keys())
        for k, v in findings.items():
            if k in self.things.keys():
                if k == "cat" or k == "tree":
                    if self.things[k] > v:
                        matches += 1
                elif k == "pomeranians" or k == "goldfish":
                    if self.things[k] < v:
                        matches += 1
                else:
                    if self.things[k] == v:
                        matches += 1
        if matches == nt:
            print (self.name, self.things)

input = {'children': 3,
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

for a in aunts:
    a.check(input)
import re

transf = {}

with open("instructions19a.txt", "r") as f:
#with open("prova.txt", "r") as f:
    lines = f.readlines()

for l in lines[:-2]:
    l = l.split("\n")[0]
    items = l.split()
    print (items)
    transf.setdefault(items[0], []).append(items[2])
molecule = lines[-1]

new_molecules = []
molecules = 0
for k in transf.keys():
    for m in re.finditer(k, molecule):
        for i in transf[k]:
            new_molecules.append(molecule[:m.start()] + i + molecule[m.start()+len(k):])

new_molecules = set(new_molecules)
print (len(new_molecules))

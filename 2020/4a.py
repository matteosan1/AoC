lines = []
with open ("input_4a.txt") as f:
    for l in f:
        lines.append(l.split("\n")[0])

ids = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #, "cid"]

# select passports
passports = []
temp = []
for l in lines:
    if l == "":
        d = {}
        for t in temp:
            that = t.split(":")
            d[that[0]] = that[1]
        passports.append(d)
        temp = []
    else:
        temp += l.split(" ")

#print (passports)
good = 0
for p in passports:
    for i in ids:
        if i not in p.keys():
            break
    else:
        good += 1
print (good)

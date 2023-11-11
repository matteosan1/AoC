lines = []
with open ("input_4.txt") as f:
    for l in f:
        lines.append(l.split("\n")[0])



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
    print (p)
    for i in p:
        if i not in p.keys():
            break
    else:
        good += 1
print (good)

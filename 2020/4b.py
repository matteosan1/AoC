import re
lines = []
with open ("input_4a.txt") as f:
    for l in f:
        lines.append(l.split("\n")[0])

ids = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #, "cid"]

def rules(p, debug = False):
    for k, v in p.items():
        if k == "byr":
            if len(v) != 4:
                if debug:
                    print ("byr")
                return False
            try:
                val = int(v)
                if val < 1920 or val > 2002:
                    if debug:
                        print ("byr")
                    return False
            except:
                if debug:
                    print ("byr")
                return False
        elif k == "iyr":
            if len(v) != 4:
                if debug:
                    print ("iyr")
                return False
            val = int(v)
            if val < 2010 or val > 2020:
                if debug:
                    print ("iyr")
                return False
        elif k == "eyr":
            if len(v) != 4:
                if debug:
                    print ("eyr")
                return False
            val = int(v)
            if val < 2020 or val > 2030:
                if debug:
                    print ("eyr")
                return False
        elif k == "hgt":
            if not (v.endswith("cm")) and not(v.endswith("in")):
                if debug:
                    print ("hgt unit ", v)
                return False
            val = int(v[:-2])
            unit = v[-2:]
            if val < 150 or val > 193 and unit == "cm":
                if debug:
                    print ("hgt val cm")
                return False
            elif val < 59 or val > 76 and unit == "in":
                if debug:
                    print ("hgt val in")
                return False
        elif k == "hcl":
            r = re.compile("#(\d|[a-f]){6}")
            if len(v) != 7 or r.match(v) is None:
                if debug:
                    print ("hcl")
                return False
        elif k == "ecl":
            if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                if debug:
                    print ("ecl")
                return False
        elif k == "pid":
            r = re.compile("\d{9}")
            if len(v) != 9 or r.match(v) is None:
                if debug:
                    print ("pid")
                return False
        return True
    
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
    for i in ids:
        if i not in p.keys():
            print ("missing ", i)
            break
    else:
        ok = rules(p, True)
        print (ok)
        if ok:
            good += 1
print (good)

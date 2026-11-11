import time, re
from utils import readInputWithBlank

def loadInput():
    lines = readInputWithBlank("prova.txt")
    lines = readInputWithBlank("input_4.txt")
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

    return passports

def checkPassport(p):
    ids = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #, "cid"]
    for i in ids:
        if i not in p.keys():
            return False

    return True

def part1(passports):
    good = 0
    for p in passports:
        if checkPassport(p):
            good += 1
    print ("🎄 Part 1: {}".format(good))

def rules(p, debug = False):
    print ("process ", p)
    for k, v in p.items():
        print (k, v)
        if k == "byr":
            try:
                val = int(v)
                if val < 1920 or val > 2002:
                    if debug:
                        print ("byr")
                    return False
            except:
                if debug:
                    print ("byr not digits")
                return False
        elif k == "iyr":
            try:
                val = int(v)
                if val < 2010 or val > 2020:
                    if debug:
                        print ("iyr")
                    return False
            except:
                if debug:
                    print ("iyr not digits")
                return False
        elif k == "eyr":
            print (k, v)

            try:
                val = int(v)
                print (val)
                if val < 2020 or val > 2030:
                    if debug:
                        print ("eyr")
                    return False
            except:
                if debug:
                    print ("eyr not digits")
                return False                
        elif k == "hgt":
            if (not v.endswith("cm")) and (not v.endswith("in")):
                if debug:
                    print ("hgt unit ", v)
                return False
            try:
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
            except:
                if debug:
                    print ("hgt not digits")
                return False                
        elif k == "hcl":
            r = re.compile("#(\d|[a-f]){6}")
            if r.match(v) is None:
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
            if r.match(v) is None:
                if debug:
                    print ("pid")
                return False
    return True

def part2(passports):
    good = 0
    for p in passports:
        if checkPassport(p) and rules(p, True):
            print ("valid ", p)
            good += 1
    print (good)
    #print ("🎄🎅 Part 2: {}".format())

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 4         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

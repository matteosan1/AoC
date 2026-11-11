from utils import readInput
import re

def lookAba(s):
    a = []
    for i in range(len(s)-2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            a.append(s[i:i+3])
    if a == []:
        return None
    else:
        return a

r = re.compile(r"\w+")
lines = readInput("input_7.txt")

ipv7 = []
for l in lines:
    matches = r.findall(l)
    if matches:
        hasAba = []
        for im in range(0, len(matches), 2):
            aba = lookAba(matches[im])
            if aba is not None:
                hasAba += aba
        if len(hasAba) > 0:
            hasBab = 0
            for aba in hasAba:
                bab = aba[1]+aba[0]+aba[1]
                for im in range(1, len(matches), 2):
                    if bab in matches[im]:
                        hasBab += 1
            if hasBab > 0:
                ipv7.append(l)

print("🎁🎄Part 2: {}".format(len(ipv7)))

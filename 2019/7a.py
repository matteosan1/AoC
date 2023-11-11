from utils import readInput
import re

def lookAbba(s):
    for i in range(len(s)-3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1] and s[i+2] != s[i+3]:
            return True
    return False

r = re.compile(r"\w+")
lines = readInput("input_7.txt")

ipv7 = []
for l in lines:
    matches = r.findall(l)
    if matches:
        hasAbba = 0
        for im in range(0, len(matches), 2):
            if lookAbba(matches[im]):
                hasAbba += 1
        if hasAbba == 1:
            noAbba = False
            for im in range(1, len(matches), 2):
                noAbba = noAbba or (not lookAbba(matches[im]))
            if noAbba:
                ipv7.append(l)

print ("🎄Part 1: {}".format(len(ipv7)))

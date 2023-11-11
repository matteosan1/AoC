from utils import readInput

def ratingCalc(lines, t="oxy"):
    rating = ""
    tmp_lines = lines
    col = 0
    while len(tmp_lines) > 1:
        thrs = len(tmp_lines)/2
        counts = sum([int(l[col]) for l in tmp_lines])
        if t == "oxy":
            if counts >= thrs:
                res = "1"
            else:
                res = "0"
        elif t == "co2":
            if counts >= thrs:
                res = "0"
            else:
                res = "1"
        rating += res
    
        tmp_tmp_lines = [l for l in tmp_lines if l[col]==res]
        tmp_lines = tmp_tmp_lines
        col += 1
    else:
        if len(rating) != len(lines[0]):
            rating += tmp_lines[0][len(rating):]
    return rating

import time
tstart = time.time()
lines = readInput("input_3.txt")
oxygen = ratingCalc(lines, "oxy")
scrubber = ratingCalc(lines, "co2")
res = int(scrubber, 2)*int(oxygen, 2)

print ("🎄🎅 Part 2: ", res)
print (time.time()-tstart)

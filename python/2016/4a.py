from utils import readInput
                  
def freq(s):
    f = {}  
    for c in s:
        f[c] = f.setdefault(c, 0) + 1

    res = {val[0] : val[1] for val in sorted(f.items(), key = lambda x: (-x[1], x[0]))}
    checksum = "".join(res.keys())
    return res, checksum[:5]

rooms = readInput("input_4.txt")

s = 0
for r in rooms:
    code = r.split("-")[:-1]
    code = "".join(code)
    second = r.split("-")[-1]
    ID, checksum = second.split("[")
    checksum = checksum[:-1]
    if freq(code)[1] ==  checksum:
        s += int(ID)

print ("🎄Part 1: {}".format(s))

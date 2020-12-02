lines = []
with open("input_2a.txt") as f:
    for l in f:
        lines.append(l.split("\n")[0])

pwds = []
for l in lines:
    pwds.append(l.split(":"))

good_pwd = 0
for p in pwds:
    c, p = p
    r, w = c.split(" ")
    rm, rM = map(int, r.split("-"))
    c = p.count(w)
    if (rm <= c <= rM):
        good_pwd += 1
print (good_pwd)

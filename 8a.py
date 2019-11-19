import re
r = re.compile('\\\\x\w\w')

filename = "instructions8a.txt"
#filename = "examples8a.txt"
with open(filename, "r") as f:
    data = f.readlines()

real_length = 0
length = 0
for d in data:
    d = d.split("\n")[0]
    real_length += len(d)
    d = d[1:-1]
    d = d.replace('\\"', '"')
    d = d.replace('\\\\', '\\')
    matches = r.findall(d)
    for m in matches:
        try:
            d = d.replace(m, chr(int("0x"+m[2:], 16)))
        except:
            continue
    length += len(d)

print (length)
print (real_length)
print (real_length-length)
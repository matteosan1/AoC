import re
r = re.compile('\\\\x\w\w')

filename = "instructions8a.txt"
#filename = "examples8b.txt"
with open(filename, "r") as f:
    data = f.readlines()

real_length = 0
length = 0
for d in data:
    d = d.split("\n")[0]
    real_length += len(d)
    print ("prima", d)
    d = d.replace('"', '/"')
    d = d.replace('\\', '\\\\')
    d = '"' + d + '"'
    print(d)
    length += len(d)

print (length)
print (real_length)
print (length - real_length)
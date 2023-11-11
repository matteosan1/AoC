part = 2
if part == 1:
    register = {"a":0, "b":0}
else:
    register = {"a":1, "b":0}
il = 0

def compiler(l):
    global register, il

    if l.startswith("hlf"):
        register[l[-1]] //= 2
        il += 1
    elif l.startswith("tpl"):
        register[l[-1]] *= 3
        il += 1
    elif l.startswith("inc"):
        register[l[-1]] += 1
        il += 1
    elif l.startswith("jmp"):
        l = l.split(" ")
        il += int(l[-1])
    elif l.startswith("jie"):
        l = l.split(" ")
        if register[l[1][-2]] %2 == 0:
            il += int(l[2])
        else:
            il += 1
    elif l.startswith("jio"):
        l = l.split(" ")
        if register[l[1][-2]] == 1:
            il += int(l[2])
        else:
            il += 1
    else:
        print ("Wrong command {}".format(l))
        import sys
        sys.exit()

filename = "instructions23a.txt"
#filename = "examples23a.txt"
with open (filename, "r") as f:
    lines = f.readlines()

while il < len(lines):
    l = lines[il].split("\n")[0]
    compiler(l)
    print(l, il, register)

print (register)

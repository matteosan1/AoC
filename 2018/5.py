with open("polymers.txt", "r") as f:
    polymer = f.readline()

pol = polymer.split("\n")[0]



def removal(pol):
    while True:
        changed = False
        new_pol = ""
        i = 0
        n = len(pol)
        while i < n:
            remove = False
            if i < n - 1 and (ord(pol[i]) == (ord(pol[i+1]) + 32) or ord(pol[i]) == (ord(pol[i+1]) - 32)):
                remove = True
                changed = True
                i = i + 1

            if not remove:
                new_pol = new_pol + pol[i]
            i = i + 1

        if not changed:
            break
        else:
            pol = new_pol

    return pol


pol = removal(pol)

#print pol
print len(pol)


nchar = {}
for i in range(65, 91):
    temp = pol.replace(chr(i), "").replace(chr(i+32), "")
    
    new_pol = removal(temp)
    nchar[chr(i)] = len(new_pol)


print nchar




    

















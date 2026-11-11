from utils import readInput

def diff(a, b):
    res = a
    for char in a:
        if char in b:
            res = res.replace(char, '')
    return res

lines = readInput("input_8.txt")

codes = []
numbers = []
for l in lines:
    temp1, temp2 = l.split("|")
    codes.append(["".join(sorted(t)) for t in temp1[:-1].split(" ")])
    numbers.append(["".join(sorted(t)) for t in temp2[1:].split(" ")])

c = 0
for n in numbers:
    for d in n:
        if len(d) == 2 or len(d) == 4 or len(d) == 3 or len(d) == 7:
            c += 1
            
print ("🎄 Part 1: {}".format(c))

grand_tot = 0
digit_map = {}
for nc, code in enumerate(codes):
    mapping = {}
    nine_six = []
    last = []

    #print (code)
    for c in code:
        if len(c) == 2:
            mapping[1] = c
        elif len(c) == 4:
            mapping[4] = c
        elif len(c) == 7:
            mapping[8] = c
        elif len(c) == 3:
            mapping[7] = c
        elif len(c) == 6:
            nine_six.append(c)
        elif len(c) == 5:
            last.append(c)

    digit_map[1] = diff(mapping[7], mapping[1])

    char = [diff(mapping[8], d) for d in nine_six]
    #print (char)
    for ic, c in enumerate(char):
        if c in mapping[1]:
            digit_map[3] = c
            mapping[6] = nine_six[ic]
        elif c in mapping[4]:
            digit_map[4] = c
            mapping[0] = nine_six[ic]
        else:
            digit_map[5] = c
            mapping[9] = nine_six[ic]
    
    #print (digit_map)
    #print (nine_six)
    
    five = diff(mapping[4], mapping[1])

    for l in last:
        matches = 0
        for char in five:
            if char in l:
                matches += 1
        if matches == 2:
            mapping[5] = l
            last.remove(l)
            break
        
    if digit_map[5] in last[0]:
        mapping[2] = last[0]
        mapping[3] = last[1]
    else:
        mapping[3] = last[0]
        mapping[2] = last[1]

    tot = 0
    for i, n in enumerate(numbers[nc]):
        #print (n)
        for k, v in mapping.items():
            #print (k, v)            
            if n == v:
                tot += k * 10**(3-i)

    #print (tot)
    grand_tot += tot
    #break

#print (mapping)
print ("🎄🎅 Part 2: {}".format(grand_tot))

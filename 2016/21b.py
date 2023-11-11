from utils import readInput
import itertools

def rotate(s, off, left=True):
    s = "".join(s)
    if left:
        Lfirst = s[0:off] 
        Lsecond = s[off:]
        return list(Lsecond + Lfirst)
    else:
        Rfirst = s[0:len(s)-off] 
        Rsecond = s[len(s)-off:] 
        return list(Rsecond + Rfirst)

def scramble(s, lines):
    s = list(s)
    for l in lines:
        parts = l.split()
        if l.startswith("swap position"):
            s[int(parts[2])], s[int(parts[-1])] = s[int(parts[-1])], s[int(parts[2])]
        elif l.startswith("swap letter"):
            temp = "".join(s)
            s = list(temp.replace(parts[2], "*").replace(parts[-1], parts[2]).replace("*", parts[-1]))
        elif l.startswith("reverse position"):
            s = s[:int(parts[2])] + list(reversed(s[int(parts[2]):int(parts[-1])+1])) + s[int(parts[-1])+1:]
        elif l.startswith("rotate based"):
            idx = s.index(parts[-1])
            if idx >= 4:
                idx += 2
            else:
                idx += 1
            s = rotate(s, idx, False)
        elif l.startswith("rotate"):
            if parts[1] == 'left':
                s = rotate(s, int(parts[-2]))
            else:
                s = rotate(s, int(parts[-2]), False)
        elif l.startswith("move"):
            temp = s[int(parts[2])]
            del s[int(parts[2])]
            s.insert(int(parts[-1]), temp)
    return "".join(s)

lines = readInput("input_21.txt")
res = "fbgdceah"
for p in itertools.permutations("abcdefhg"):
    if scramble(p, lines) == res:
        print ("🎁🎄Part 2: {}".format("".join(p)))

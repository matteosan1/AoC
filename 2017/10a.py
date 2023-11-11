def rotate(l, pos, dir="left"):
    if dir == "right":
        l = l[-pos:] + l[:-pos]
    else:
        l = l[pos:] + l[:pos]
    return l


lengths = [94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243]

size = 256
seq = list(range(size))
pos = 0
skip = 0
for i, l in enumerate(lengths):
    seq = rotate(seq, pos, "left")
    seq = list(reversed(seq[:l])) + seq[l:]
    seq = rotate(seq, pos, "right")
    pos += (l + skip)
    pos %= len(seq)
    skip += 1

print ("🎄Part 1: {}".format(seq[0]*seq[1]))

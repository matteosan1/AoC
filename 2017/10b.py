from functools import reduce

def rotate(l, pos, dir="left"):
    if dir == "right":
        l = l[-pos:] + l[:-pos]
    else:
        l = l[pos:] + l[:pos]
    return l

lengths = "94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243"
lengths = [ord(l) for l in lengths] + [17, 31, 73, 47, 23]

size = 256
seq = list(range(size))
pos = 0
skip = 0
for round in range(64):
    for i, l in enumerate(lengths):
        seq = rotate(seq, pos, "left")
        seq = list(reversed(seq[:l])) + seq[l:]
        seq = rotate(seq, pos, "right")
        pos += (l + skip)
        pos %= len(seq)
        skip += 1

dense = [reduce(lambda a,b:a^b, seq[i:i+16]) for i in range(0, len(seq), 16)]
print ("🎁🎄Part 2: {}".format("".join(['{0:0{1}x}'.format(c, 2) for c in dense])))

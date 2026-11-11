from utils import readInput

def rotate(c, ID):
    ALPHABET_LENGTH = 26
    char_pos = ord(c) - ord('a')
    char_pos = (char_pos + ID) % ALPHABET_LENGTH
    return chr(char_pos + ord('a'))

def decypher(code, ID):
    code = code.replace("-", " ")
    string = ""
    for c in code:
        if c == " ":
            string += c
        else:
            string += rotate(c, ID)

    return string

def decodeRoom(r):
    code = r.split("-")[:-1]
    code = "".join(code)
    second = r.split("-")[-1]
    ID, checksum = second.split("[")
    checksum = checksum[:-1]
    return code, ID, checksum

def freq(s):
    f = {}  
    for c in s:
        f[c] = f.setdefault(c, 0) + 1

    res = {val[0] : val[1] for val in sorted(f.items(), key = lambda x: (-x[1], x[0]))}
    checksum = "".join(res.keys())
    return res, checksum[:5]

rooms = readInput("input_4.txt")

real_rooms = []
for r in rooms:
    code, ID, checksum = decodeRoom(r)
    if freq(code)[1] == checksum:
        real_rooms.append(r)


        
for r in real_rooms:
    code, ID, checksum = decodeRoom(r)
    name = decypher(code, int(ID))
    if "north" in name:
        print("🎁🎄Part 2: {}-{}".format(name, ID))
        break

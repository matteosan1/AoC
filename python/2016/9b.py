from utils import readInput

def search(s, idx = 0, length=0):
    while idx < len(s):
        if s[idx] == "(":
            parc = s[idx:].find(")")
            decompression = list(map(int, s[idx+1:idx+parc].split("x")))
            if "(" in s[idx+parc+1:idx+parc+1+decompression[0]]:
                l = search(s[idx+parc+1:idx+parc+1+decompression[0]], 0, 0)
                length += l * decompression[1]
            else:
                length += decompression[0]*decompression[1]
            idx += parc + decompression[0] + 1
        else:
            idx += 1
            length += 1
    return length

lines = readInput("input_9.txt")
p = search(lines[0])

print ("🎁🎄Part 2: {}".format(p))

with open("input_2.txt") as f:
    lines = []
    for l in f.readlines():
        lines.append(l.split("\n")[0])


digit_map = {(1, 1): "5", (1, 0): "2", (1, 2): "8",
             (0, 1): "4", (0, 0): "1", (0, 2): "7",
             (2, 1): "6", (2, 0): "3", (2, 2): "9"}

x, y = 1, 1
digits = ""
for l in lines:
    for c in l:
        if c == "U":
            if y-1 >= 0:
                y -= 1
        elif c == "D":
            if y+1 <= 2:
                y += 1
        elif c == "L":
            if x-1 >= 0:
                x -= 1
        elif c == "R":
            if x+1 <= 2:
                x += 1
    digits += digit_map[(x, y)]
print ("🎄Part 1: {}".format(digits))




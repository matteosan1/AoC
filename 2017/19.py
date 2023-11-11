from utils import readInput

lines = readInput("input_19.txt", True)

dir = (0, 1)
for y, l in enumerate(lines):
    x = l.find("|")
    if x != -1:
        start = (x, y)
        break

phrase = ""
count = 0
while True:
    start = (start[0]+dir[0], start[1]+dir[1])
    count += 1
    char = lines[start[1]][start[0]]
    if 65 <= ord(char) <= 90:
        phrase += char
    elif char == "+":
        if dir[0] == 0:
            if start[0]+1 < len(lines[start[1]])-1 and lines[start[1]][start[0]+1] != " ":
                dir = (1, 0)
            elif start[0]-1 >= 0 and lines[start[1]][start[0]-1] != " ":
                dir = (-1, 0)
            else:
                break
        else:
            if start[1]+1 < len(lines)-1 and lines[start[1]+1][start[0]] != " ":
                dir = (0, 1)
            elif start[1]-1 >= 0  and lines[start[1]-1][start[0]] != " ":
                dir = (0, -1)
            else:
                break
    elif char == " ":
        break

print ("🎄Part 1: {}".format(phrase))
print ("🎁🎄Part 2: {}".format(count))

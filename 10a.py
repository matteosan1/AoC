init = "1113122113a"

def choice(temp, ch):
    global current, ripet
    if ch == current:
        ripet += 1
    else:
        temp += str(ripet) + current
        current = ch
        ripet = 1
    return temp

for _ in range(50):
    ripet = 1
    temp = ""
    current = init[0]
    for ic in range(1, len(init)):
        temp = choice(temp, init[ic])

    print (temp)
    init = temp + "a"
print (len(temp))
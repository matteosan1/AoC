#pwd = "vzbxkghb"
#pwd = "ghijklmn"
pwd = "vzbxxyzz"
def validate(p):
    result1 = False
    result2 = False
    result3 = False

    new_pwd = list(p)
    for i in range(0, len(new_pwd) - 3):
        if (ord(new_pwd[i+2]) - ord(new_pwd[i+1]) == 1) and (ord(new_pwd[i + 1]) - ord(new_pwd[i]) == 1):
            result1 = True
            break

    if "i" not in new_pwd and "o" not in new_pwd and "l" not in new_pwd:
        result2 = True

    pairs = 0
    i = 0
    while i < (len(new_pwd) - 1):
    #for i in range(0, len(new_pwd) -1):
        if new_pwd[i] == new_pwd[i+1]:
            pairs += 1
            i += 1
        i += 1
    if pairs > 1:
        result3 = True

    if result1 and result2 and result3:
        print ("".join(new_pwd))
        import sys
        sys.exit()

def increment(p):
    new_pwd = list(p)
    pos = 7
    while True:
        ch = ord(new_pwd[pos]) + 1
        if ch == 123:
            new_pwd[pos] = chr(97)
            pos -= 1
        else:
            new_pwd[pos] = chr(ch)
            break
    return ''.join(new_pwd)

while True:
    npwd = increment(pwd)
    #print (npwd)
    validate(npwd)
    pwd = npwd

def check_consecutive(p):
    s = ord(p[0])
    if ord(p[1]) == (s + 1) and ord(p[2]) == (s + 2):
        return True
    return False

def validate(pwd):
    pairs = []
    for i in range(len(pwd)-1):
        if pwd[i] == pwd[i+1]:
            pairs.append(pwd[i:i+2])
    if len(set(pairs)) < 2:
        return False

    for i in range(len(pwd)-2):
        if check_consecutive(pwd[i:i+3]):
            break
    else:
        #print ("no triplet")
        return False

    if "i" in pwd or "o" in pwd or "l" in pwd:
        #print ("iol")
        return False
    
    return True

def prevalidate(pwd):
    for i in range(len(pwd)):
        if pwd[i] == "i" or pwd[i] == "l" or pwd[i] == "o":
            pwd = pwd[:i] + chr(ord(pwd[i])+1) + 'a'*(len(pwd) - i)
            return pwd

    return pwd

def increase(pwd, i=None):
    if i is None:
        i = len(pwd)-1
        
    inc = chr(ord(pwd[i])+1)
    #print (inc)
    if inc == "i" or inc == "l" or inc == "o":
        pwd = pwd[:i] + inc + pwd[i+1:]
        pwd = increase(pwd)              
    elif inc == '{':
        inc = 'a'
        pwd = pwd[:i] + inc + pwd[i+1:] 
        i -= 1
        pwd = increase(pwd, i)
    else:
        pwd = pwd[:i] + inc + pwd[i+1:]
    return pwd


#pwd = 'vzbxkghb'
pwd = "vzbxxzaa"

pwd = prevalidate(pwd)

while not validate(pwd):
    pwd = increase(pwd)
    #print (pwd)

print (pwd)


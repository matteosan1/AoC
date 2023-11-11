import hashlib
import re

def createHashes(start=0, max_id=40000):
    prefix = "jlmsuwbz"
    with open("hashes.txt", "w") as f:
        for i in range(start, max_id):
            salt = prefix + str(i)
            for _ in range(2017):
                md5 = hashlib.md5(salt.encode())
                salt = md5.digest().hex()
            f.write(salt+"\n")
            
def formKey(prefix, i):
    salt = prefix + str(i)
    md5 = hashlib.md5(salt.encode())
    key = md5.digest().hex()
    return key

def findNext(lines, m):
    reg5 = re.compile("(["+m+"])\\1{4,}")
    i = 0
    while i < len(lines):
        if reg5.search(lines[i]):
            return True
        i += 1
    return False
            
def findKey():
    keys = []
    reg3 = re.compile("([a-zA-Z0-9])\\1{2,}")
    with open("hashes.txt") as f:
        lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].split("\n")[0]
        
    idx = 0
    while True:
        match = reg3.search(lines[idx])
        if match:
            if findNext(lines[idx+1:min(idx+1001, len(lines))], match.group(0)[0]):
                keys.append(idx)
        idx += 1
        if len(keys) == 64:
            print ("🎁🎄Part 2: {}".format(keys[-1]))
            break


#createHashes()
findKey()

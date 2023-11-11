import hashlib
import re

def formKey(prefix, i):
    salt = prefix + str(i)
    md5 = hashlib.md5(salt.encode())
    key = md5.digest().hex()
    return key

def findNext(prefix, idx, m):
    global part
    reg5 = re.compile("(["+m+"])\\1{4,}")
    i = 0
    while i < 1000:
        key = formKey(prefix, idx+i)
        if reg5.search(key):
            return True
        i += 1
    return False
            
def findKey(prefix, idx):
    global part
    keys = []
    reg3 = re.compile("([a-zA-Z0-9])\\1{2,}")
    while True:
        key = formKey(prefix, idx)
        match = reg3.search(key)
        if match:
            if findNext(prefix, idx+1, match.group(0)[0]):
                keys.append(idx)
        idx += 1
        if len(keys) == 64:
            print ("🎄Part 1: {}".format(keys[-1]))
            break

salt = "jlmsuwbz"
#salt = "abc"
findKey(salt, 0)


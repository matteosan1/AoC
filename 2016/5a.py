import hashlib

code = "reyedfim"

pwd = ""
i = 0
while len(pwd) < 8:
    c = code + (str(i))
    md5 = hashlib.md5(c.encode())
    digest = md5.hexdigest()
    if digest.startswith("00000"):
        print (digest)
        pwd += digest[5]
    i += 1
    
print ("🎄Part 1: {}".format(pwd))

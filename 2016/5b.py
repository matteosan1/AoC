import hashlib

code = "reyedfim"

pwd = ["_" for _ in range(8)]
i = 0
while "_" in pwd:
    c = code + (str(i))
    md5 = hashlib.md5(c.encode())
    digest = md5.hexdigest()
    if digest.startswith("00000"):
        #print (digest)
        pos = int(digest[5], 16)
        if pos < 8:
            if pwd[pos] == "_":
                pwd[pos] = digest[6]
                print ("".join(pwd), end="\r")
    i += 1
    
print("🎁🎄Part 2: {}".format("".join(pwd)))

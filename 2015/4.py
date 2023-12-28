import time, hashlib

def loadInput():
    return b"bgvyzdsv"

def task(arange, key, hash_begin):
    for i in arange:
        r = hashlib.md5(key + str(i).encode())
        hexa = r.hexdigest()
        if hexa[:len(hash_begin)] == hash_begin:
            return (i, hexa)
    return None

def part1(key):
    res = task(range(1, 2000000), key, "00000")
    print (f"🎄 Part 1: {res[0]} {res[1]}")

def part2(key):
    res = task(range(1, 2000000), key, "000000")
    print (f"🎄🎅 Part 2: {res[0]} {res[1]}")
    
if __name__ == "__main__":
    title = "Day 4: The Ideal Stocking Stuffer"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))


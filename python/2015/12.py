import time, json

def counter(obj, part=1, to_ignore='', c=0):
    if isinstance(obj, dict):
        if part == 2 and to_ignore in obj.values():
            return 0
        for k, v in obj.items():
            c += counter(v, part, to_ignore)
        return c
    elif isinstance(obj, list):
        for i in obj:
            c += counter(i, part, to_ignore)
        return c
    elif isinstance(obj, str):
        return 0
    elif isinstance(obj, int):
        return obj
    return c

def loadInput():
    with open("instructions12a.txt", "r") as f:
        data = json.load(f)
    return data

def part1(inputs):
    c = counter(inputs)
    print (f"🎄 Part 1: {c}")

def part2(inputs):
    c = counter(inputs, to_ignore='red', part=2)
    print (f"🎄🎅 Part 2: {c}")
    
if __name__ == "__main__":
    title = "Day 12: JSAbacusFramework.io"
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


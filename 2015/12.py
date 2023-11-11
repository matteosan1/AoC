import json

part = 2
c = 0
to_ignore = "red"

def counter(obj):
    global c
    if isinstance(obj, dict):
        if part == 2 and to_ignore in obj.values():
            return
        for k, v in obj.items():
            counter(v)
    elif isinstance(obj, list):
        for i in obj:
            counter(i)
    elif isinstance(obj, str):
        return
    elif isinstance(obj, int):
        c += obj
    return


filename = "instructions12a.txt"
#filename = "examples12a.txt"

with open(filename, "r") as f:
    data = json.load(f)

counter(data)
print (c)

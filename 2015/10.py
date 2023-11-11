from itertools import groupby
import time

t = time.time()
init = "1321131112"

def look_and_say(inp):
    return ''.join(str(len(list(v))) + k for k, v in groupby(inp))

p1 = init
for steps in range(50):
    p1 = look_and_say(p1)
    if steps == 39:
        print (len(p1))
print(len(p1))

print (time.time()-t)

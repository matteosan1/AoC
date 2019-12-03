import pandas as pd
import re
from collections import deque

r = re.compile("[a-z]{1,4}")
vars = {}

def decrypt(m):
    m = m.split("->")
    matches = r.findall(m[0])
    m[-1] = m[-1].strip()

    for v in matches:
        m[0]= m[0].replace(v, "____['" + v + "']")
    cmd = m[-1] + "=" + m[0].replace("____", "vars")

    cmd = cmd.replace("RSHIFT", ">>")
    cmd = cmd.replace("LSHIFT", "<<")
    cmd = cmd.replace("NOT", "65535-")
    cmd = cmd.replace("AND", "&")
    cmd = cmd.replace("OR", "|")
    return cmd

data = pd.read_csv("instructions7a.txt", header = None, delimiter=":")
#data = pd.read_csv("examples7a.txt", header = None, delimiter=":")
instructions = deque(data[0])

while len(instructions) != 0:
    m = instructions.popleft()
    if m.startswith("#"):
        continue
    cmd = decrypt(m)
    try:
        print("executing:", cmd)
        c = cmd.split("=")
        vars[c[0]] = eval(c[1])
    except:
        instructions.append(m)

print (vars["a"])


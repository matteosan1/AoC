import pandas as pd

bad = ["ab", "cd", "pq", "xy"]
good = ["a", "e", "i", "o", "u"]

data = pd.read_csv("instructions5a.txt", header = None)
#data = pd.read_csv("examples5b.txt", header = None)
msgs = data[0]

good_msg = 0
for m in msgs:
    #pairs = {}
    isGood = False
    last_pair = ""
    for ic in range(0, len(m)-3):
        pair = m[ic:ic+2]
        if pair in m[ic+2:]:
            for ic in range(0, len(m)-2):                    
                if m[ic] == m[ic+2]:
                    isGood = True
                    break
    if isGood:
        print (m)
        good_msg += 1
        
print (good_msg)
            

import pandas as pd

bad = ["ab", "cd", "pq", "xy"]
good = ["a", "e", "i", "o", "u"]

data = pd.read_csv("instructions5a.txt", header = None)
#data = pd.read_csv("examples5b.txt", header = None)
msgs = data[0]

good_msg = 0
for m in msgs:
    # pairs of letters
    pairs = {}
    isGood = False
    last_pair = ""
    for ic in range(0, len(m)-1):
        pair = m[ic] + m[ic+1]
        if pair != last_pair:
            pairs[pair] = pairs.setdefault(pair, 0) + 1
        last_pair = pair

    for p in pairs.values():
        if p >= 2:
            for ic in range(0, len(m)-2):                    
                if m[ic] == m[ic+2]:
                    isGood = True
                    break
    if isGood:
        good_msg += 1
        
print (good_msg)
            

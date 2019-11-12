#It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

import pandas as pd

bad = ["ab", "cd", "pq", "xy"]
good = ["a", "e", "i", "o", "u"]

data = pd.read_csv("instructions5a.txt", header = None)
#data = pd.read_csv("examples5a.txt", header = None)
msgs = data[0]

good_msg = 0
for m in msgs:
    for b in bad:
        if b in m:
            break
    else:
        vowels = 0
        isGood = False
        for c in m:
            if c in good:
                vowels += 1
            if vowels == 3:
                for ic in range(0, len(m)-1):                    
                    if m[ic] == m[ic+1]:
                        isGood = True
                        break
        if isGood:
            good_msg += 1
        
print (good_msg)
            

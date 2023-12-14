#[1000, 8, 5, 5, 5, 1200, 2, 15, 100, 1200, 2, 1200, 400, 4, 4, 700, 800, 9, 300, 900, 12, 1000, 700, 300, 8, 6, 1, 1, 1, 2, 300, 5, 300, 16, 700, 900, 1, 14, 300, 4, 300, 9, 200, 1100, 6, 14, 7, 100, 700, 11, 6, 1400, 600, 8, 6, 3, 1, 6, 11, 700, 16, 12, 1200, 400, 900, 12, 1200, 5, 400, 11, 1200, 9, 6, 14, 600, 1200, 8, 500, 700, 3, 7, 1600, 200, 1, 5, 7, 200, 400, 1300, 10, 3, 6, 100, 8, 10, 5, 1200, 12, 15, 500]
# NEED TO FIX PART 2 TO RESULT I 31603

import time
import numpy as np

from utils import readInputWithBlank

def loadInput():
    lines = readInputWithBlank("prova.txt")
    lines = readInputWithBlank("input_13.txt")
    patterns = []
    temp = []
    for l in lines:
        if l == "":
            patterns.append(np.array(temp))
            temp = []
        else:
            temp.append([1 if c == "#" else 0 for c in l])
    patterns.append(np.array(temp))
    return patterns

def find_reflection(pattern, mult):
    psize = pattern.shape[0]
    reflections = []
    for i in range(psize-1):
        if (pattern[i, :] == pattern[i+1, :]).all():
            #print (i)
            #print (pattern)
            if (i+1) < psize/2:
                line = 2*(i+1)
                ref = pattern[:line, :]
            elif (i+1) > psize/2:
                line = (psize-i-1)*2
                ref = pattern[-line:, :]
            #print (ref)    
            if (ref[:line//2, :] == np.flip(ref[-line//2:, :], axis=0)).all():
                print ("match", i)
                reflections.append(mult*(i+1))
                #print (pattern[i+1:i+delta+2])
    #    reflections.append(("h", i, mult*(i+1)))
    #print (reflections)
    return reflections

def part1(patterns):
    r = []
    
    for pattern in patterns:
        refs = []
        #if side == 0 or side == 2:
        refs += find_reflection(pattern, mult=100)
        #print (refs)
        #if side == 1 or side == 2:
        pattern = np.rot90(pattern, 3)
        refs += find_reflection(pattern, mult=1)
        #print (refs)
        r += refs
    return r

def find_smudge(pattern, old_ref, mult):
    found = False
    refs = []
    psize = pattern.shape[0]
    for i in range(psize-1):
        for j in range(1, psize):
            diff = pattern[i, :] - pattern[j, :]
            if np.abs(diff).sum() == 1:
                #print (i, j, diff)
                reflection = pattern.copy()
                reflection[i, :] -= diff
                #pattern[i, :] -= diff
                refs += find_reflection(reflection, mult)
                #print (refs)
                if old_ref is not None and old_ref in refs:
                    refs.remove(old_ref)
                if len(refs) != 0:
                    found = True
                    break
                if len(refs) == 0:
                    reflection = pattern.copy()
                    reflection[j, :] += diff
                    refs += find_reflection(reflection, old_ref)
                    if old_ref is not None and old_ref in refs:
                        refs.remove(old_ref)
                    if len(refs) != 0:
                        found = True
        if found:
            break
    return refs

def part2(patterns, no_smudged):
    r = []
    print (no_smudged)
    for ip, pattern in enumerate(patterns):
        print (f"@@@@@@@ {ip} @@@@@@@@@@@")
        #print (pattern)
        old_ref = no_smudged[ip]

        reflections = []
        pat = pattern.copy()
        #print (pat)
        #print (old_ref)
        c = find_smudge(pat, old_ref, mult=100)
        #print ("S ", c)
        reflections += c
        
        pat = pattern.copy()
        pat = np.rot90(pat, 3)
        #print (pat)
        c = find_smudge(pat, old_ref, mult=1)
        #print ("T ", c)
        reflections += c

#        found = True
#        for i in range(pattern.shape[0]-1):
#            for j in range(1, pattern.shape[0]):
#                diff = pattern[i, :] - pattern[j, :]
#                #print (i, j, diff)
#                if np.abs(diff).sum() == 1:
#                    reflection = pattern.copy()
#                    reflection[i, :] -= diff
#                    print ("first ", reflection[i, :])
#                    refs = find_all_reflections(reflection, old_ref)
#                    #find_reflection(reflection, old_ref)
#                    if len(refs) > 0:                        
#                        #refs.remove(old_ref)
#                        print ("1 ", refs)
#                        reflections += refs
#                        #print ("smudge ", i, get_index(diff))
#                        found = True
#                        break
#                    else:
#                        reflection = pattern.copy()
#                        reflection[j, :] += diff
#                        refs = find_all_reflections(reflection, old_ref)
#                        #refs = find_reflection(reflection, old_ref)
#                        if len(refs) > 0:
#                            #refs.remove(old_ref)
#                            print ("2", refs)
#                            #r += refs[0][2]
#                            reflections += refs
#                            #print ("smudge ", i, get_index(diff))
#                            found = True
#                            break
#            if found:
#                break
#        print (reflections)
#        # look for cols
#        found = False
#        if not found:
#            for i in range(pattern.shape[1]-1):
#                for j in range(1, pattern.shape[1]):
#                    diff = pattern[:, i] - pattern[:, j]
#                    if np.abs(diff).sum() == 1:
#                        reflection = pattern.copy()
#                        reflection[:, i] -= diff
#                        #refs = find_reflection(reflection, old_ref)
#                        refs = find_all_reflections(reflection, old_ref)
#                        if len(refs) > 0:
#                            #refs.remove(old_ref)
#                            print ("1c", refs)
#                            #r += refs[0][2]
#                            reflections += refs
#                            #print ("smudge ", i, get_index(diff))
#                            found = True
#                            break
#                        else:
#                            reflection = pattern.copy()
#                            reflection[:, j] += diff
#                            refs = find_all_reflections(reflection, old_ref)
#                            #refs = find_reflection(reflection, old_ref)
#                            if len(refs) > 0:
#                                #refs.remove(old_ref)
#                                print ("2c", refs)
#                                reflections += refs
#                                #print ("smudge ", i, get_index(diff))
#                                #r += refs[0][2]
#                                found = True
#                                break
#                if found:
#                    break
        print ("OLD ", old_ref)
        reflections = list(set(reflections))
        print (reflections)
        if len(reflections) == 0:
            r += [old_ref]
        else:
            r += reflections
    return r

if __name__ == '__main__':
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    print("⛄        Day 13        ⛄")
    print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
    
    inputs = loadInput()

    t0 = time.time()
    r = part1(inputs)
    res1 = sum(r)
    t1 = time.time()-t0
    
    t0 = time.time()
    r = part2(inputs, r)
    res2 = sum(r)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

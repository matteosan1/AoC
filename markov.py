from random import random, seed
import os

def convert(l):
    d = {}
    p = 0
    #print (l)
    for w in l:
        #print (w, d)
        if w in d:
            continue
        p += l.count(w)/len(l)
        d[w] = p
    return d

def check(d, r):
    k = list(d.keys())
    v = list(d.values())
    
    if r < v[0]:
        return k[0]
    else:
        for i in range(1, len(d)):
            if v[i-1] < r < v[i]:
                return k[i]

#testo = ["Il mio nome è Matteo.",
#         "Il tuo nome è Giuseppe.",
#         "Il nome di mia figlia è Greta."]


testo = []
for d, dummy, files in os.walk("testi/"):
    for f in files:
        with open(d+f, "r") as temp:
            lines = temp.readlines()
            text = " ".join(lines)
            text = text.replace("\n", "")
            sents = text.split(".")
            testo += sents#.append(text)

matrix = {}
start = []
step = 1
for t in testo:
    t = t.replace(".", " .").replace(",", "").replace(";", "").replace(":", "").replace("!", "").replace("(", "").replace(")", "")
    t = t.lower()
    words = t.split()
    start.append(" ".join(words[0:step]))
    for i in range(step, len(words)):
        key = " ".join(words[i-step:i])
        matrix.setdefault(key, []).append(words[i])
#        if (words[i] == 'siamo'):
#            print (t, words[i])
#            print (matrix[words[i]])
#            #import sys
#            #sys.exit()
#

start = convert(start)
for k, v in matrix.items():
    #print (k, matrix[k], v)
    matrix[k] = convert(v)

#seed(2)
for _ in range(10):
    sentence = []
    r = random()
    sentence.append(check(start, r))
    w = ""
    n = 0
    while w != ".":
        w = check(matrix[sentence[-1]], random())
        sentence.append(w)
        if w not in matrix:
            break
        n += 1
        if n == 20:
            break
    print (" ".join(sentence))

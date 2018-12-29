import random
import time
carte = 52
n_per_cartella = 25
premio = [4, 5, 25]
giocatori = 300
sample = range(carte)

round = 10000
ncartelle = 1000

cartelle = []
estrazioni = []
for _ in range(round):
    estrazioni.append(random.sample(sample, carte))

for _ in range(ncartelle):
    cartelle.append(random.sample(sample, n_per_cartella))

for estrazione in range(11, carte):
    win = [0 for _ in range(len(premio))]

    for ic in range(ncartelle):
        for r in range(round):
            t1 = time.time()
            test = estrazioni[r][:estrazione]
            for ip, p in enumerate(premio):
                sub_cartella = set(cartelle[ic][:p])
                i = 0
                for t in test:
                    if t in sub_cartella:
                        i = i + 1

                if i == p:
                    win[ip] = win[ip] + 1
            t2 = time.time()
            #print (t2-t1)
    prob = [float(w)/float(round*ncartelle) for w in win]
    print ("Estrazione: {} prob. {} vincitori {}".format(estrazione, prob, [p*giocatori for p in prob]))
    

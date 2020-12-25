import time
start_time = time.time()

deck = [[], []]
id = -1
with open("input_22a.txt") as f:
    for l in f:
        l = l.split("\n")[0]
        if l == "":
            continue
        if "Player" in l:
            id += 1
        else:
            deck[id].append(int(l))

#print (deck[1])
rounds = 1
while len(deck[0]) > 0 and len(deck[1]) > 0:
    if deck[0][0] > deck[1][0]:
        deck[0].append(deck[0][0])
        deck[0].append(deck[1][0])
    elif deck[0][0] < deck[1][0]:
        deck[1].append(deck[1][0])
        deck[1].append(deck[0][0])
    else:
        deck[0].append(deck[0][0])
        deck[1].append(deck[1][0])
    deck[0].pop(0)
    deck[1].pop(0)
    rounds += 1

#print(rounds)
if len(deck[1]) > 0:
    points = sum([(len(deck[1])-i)*deck[1][i] for i, v in enumerate(deck[1])])
elif len(deck[0]) > 0:
    points = sum([(len(deck[0])-i)*deck[0][i] for i, v in enumerate(deck[0])])

print('🎄 Part 1: {} 🎄'.format(points))
print("\n--- %.7s secs ---" % (time.time() - start_time))
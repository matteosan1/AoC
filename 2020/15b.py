import time
start_time = time.time()

input = [16,11,15,0,1,7]

last = {}
new_last = {}
spoken = {}
test = []
turn = 1
while turn <= 30000000:
    if turn >= 2:
        last = dict(new_last)

    if turn <= len(input):
        new_last = {input[turn-1]:turn}
    else:
        last_key = list(last.keys())[0]
        #print (last, spoken)
        if last_key not in spoken.keys():
            new_last = {0:turn}
        else:
            index = spoken[last_key]
            new_last = {(turn - index - 1):turn}
    turn += 1
    if turn >= 2:
        spoken.update(last)

print('🎄 Part 2: {} 🎄'.format(new_last))
print("\n--- %.7s secs ---" % (time.time() - start_time))

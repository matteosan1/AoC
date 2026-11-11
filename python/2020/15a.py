import time
start_time = time.time()

input = [16,11,15,0,1,7]

spoken = []
turn = 0
while turn <= 2019:
    #print (turn)
    if turn < len(input):
        spoken.append(input[turn])
    else:
        previous = spoken[turn-1]
        if previous not in spoken[0:turn-1]:
            spoken.append(0)
        else:
            index = (turn-2) - spoken[turn-2::-1].index(previous)
            #print (previous, index, turn - 1)
            spoken.append(turn - 1 - index)
    turn += 1
    #print (spoken)
print('🎄 Part 1: {} 🎄'.format(spoken[-1]))
print("\n--- %.7s secs ---" % (time.time() - start_time))
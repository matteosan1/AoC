
step = 382
state = [0]
idx = 0
for i in range(1, 2018):
    idx = (idx+step)%len(state) + 1
    state.insert(idx, i)

idx = state.index(2017)
print ("🎄Part 1: {}".format((state[idx-3:idx+4])))

idx = 0
for i in range(1, 50000000+1):
    idx = (idx+step)%i + 1
    if idx == 1:
        val = i
    
print ("🎁🎄Part 2: {}".format(val))

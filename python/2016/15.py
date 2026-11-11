def position(t, sectors, offset):
    return (t+offset)%sectors == 0

part = 1
if part == 1:
    discs = [(17, 1), (7, 0), (19, 2), (5, 0), (3, 0), (13, 5)]
else:
    discs = [(17, 1), (7, 0), (19, 2), (5, 0), (3, 0), (13, 5), (11, 0)]

delay = 0
while True:
    state = [position(delay+i+1, s, o) for i, (s,o) in enumerate(discs)]
    if all(state):
        if part == 1:
            print ("🎄Part 1: {}".format(delay))
        else:
            print ("🎁🎄Part 2: {}".format(delay))
        break
    delay += 1


elves = 3014603
#presents = {(i+1):1 for i in range(elves)}
#
#is_get = True
#while True:
#    for i in presents.keys():
#        if is_get:
#            presents[i] = 1
#            is_get = False
#        else:
#            presents[i] = 0
#            is_get = True
#
#    new_presents = {k:v for k,v in presents.items() if v > 0}
#    if len(new_presents) == 1:
#        print ("🎄Part 1: {}".format(new_presents.keys()))
#        break
#    presents = new_presents

# Josephesus Problem
# Numberphile https://www.youtube.com/watch?v=uCsD3ZGzMgE
b = bin(elves)
winner = int(b[3:]+b[2], 2)
print ("🎄Part 1: {}".format(winner))

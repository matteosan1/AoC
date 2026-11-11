# by looking code by eye

h = 0
for x in range(106700, 123700 + 1,17):
    for i in range(2,x):
        if x % i == 0:
            h += 1
            break
        
print ("🎁🎄Part 2: {}".format("".join(h)))



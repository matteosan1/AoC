nelves = 3014603

# found by hand a similar rule to part 1
#for nelves in range(729, 1035):
#    elves = [i+1 for i in range(nelves)]
#    while True:
#        y = (len(elves)//2)%len(elves)
#        del elves[y]
#        elves = elves[1:] + elves[:1]
#        if len(elves) == 1:
#            print (nelves, elves)
#            break

i = 0
while 3**(i+1) < nelves:
    i += 1

m = nelves%(3**i)
if m < 3**i: 
    print ("🎁🎄Part 2: {}".format(m))
else:
    print ("🎁🎄Part 2: {}".format(2*nelves - 3**(i+1)))

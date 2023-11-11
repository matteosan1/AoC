import time
start_time = time.time()

rules = {}
myticket = []
tickets = []
insertTickets = False
with open("input_16a.txt") as f:
    i = 0
    l = f.readline()
    while l:
        l = l.split("\n")[0]
        if insertTickets:
            tickets.append(list(map(int, l.split(","))))   
        if 'or' in l:
            name = l.split(":")[0]
            rules[name] = []
            r1 = list(map(int, l.split(' ')[-3].split("-")))
            r2 = list(map(int, l.split(' ')[-1].split("-")))
            rules[name].append(r1)
            rules[name].append(r2)
        elif "your" in l:
            i += 1
            l = f.readline().split("\n")[0]
            myticket = list(map(int, l.split(",")))
        elif "tickets" in l:
            insertTickets = True
        i += 1
        l = f.readline()

print (rules)
print ("tickets ", tickets)
print (myticket)

sanity = 0
for t in tickets:
    for val in t:
        print ("checking ", val)
        valid = False
        for c in rules.values():
            if c[0][0] <= val <= c[0][1] or c[1][0] <= val <= c[1][1]:
                valid = True
                break
        print (valid)
        if not valid:
            sanity += val
        
                
print('🎄 Part 1: {} 🎄'.format(sanity))
print("\n--- %.7s secs ---" % (time.time() - start_time))

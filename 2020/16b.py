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

validity = []
for t in tickets:
    temp = []
    for iv, val in enumerate(t):
        valid_rules = [ic for ic, c in enumerate(rules.values()) if c[0][0] <= val <= c[0][1] or c[1][0] <= val <= c[1][1]]
        if len(valid_rules) > 0:
            temp.append(valid_rules)
    if len(temp) == len(t):
        validity.append(temp)

# per ogni field ho lista di regole valide
fields_to_rules = []
for f in range(len(validity[0])):
    valid_for_field = []
    for r in range(len(rules)):
        if all([r in ticket[f] for ticket in validity]):
            valid_for_field.append(r)
    fields_to_rules.append(valid_for_field)

# per ogni field ho le regole possibili
fields = {}
while len(fields) < len(rules):
    for i, f in enumerate(fields_to_rules):
        if len(f) == 1:
            r = f[0]
            fields[r] = i
            for f1 in fields_to_rules:
                try:
                    f1.remove(r)
                except:
                    pass
            break

tot = 1
for i in range(6):
    tot *= myticket[fields[i]]

print('🎄 Part 2: {} 🎄'.format(tot))
print("\n--- %.7s secs ---" % (time.time() - start_time))


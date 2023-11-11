register = {}
max_val = 0
with open("input_8.txt") as f:
    for l in f:
        if l.startswith("###"):
            break
        #print (l)
        parts = l.split("\n")[0].split(" if ")
        cmd = parts[0].split()
        cond = parts[1].split()
        if cond[0] not in register:
            register[cond[0]] = 0
        form = "{} {}".format(register[cond[0]], " ".join(cond[1:]))
        if eval(form):
            if cmd[1] == 'inc':
                register[cmd[0]] = register.setdefault(cmd[0], 0) + int(cmd[2])
            elif cmd[1] == 'dec':
                register[cmd[0]] = register.setdefault(cmd[0], 0) - int(cmd[2])

        temp = max(register.items(), key=lambda x: x[1])
        if max_val < temp[1]:
            max_val = temp[1]
print ("🎄Part 1: {}".format(max(register.items(), key=lambda x: x[1])))
print ("🎁🎄Part 2: {}".format(max_val))

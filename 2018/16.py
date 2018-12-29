import ast, copy

cmds = ["addr", "addi", "mulr", "muli", "banr", "bani",
        "borr", "bori", "setr", "seti", "gtir", "gtri",
        "gtrr", "eqir", "eqri", "eqrr"]

def doCmd(cmd, params, reg):
    reg = copy.deepcopy(reg)
    if cmd == "addr":
        reg[params[3]] = reg[params[1]] + reg[params[2]] 
    elif cmd == "addi":
        reg[params[3]] = reg[params[1]] + params[2] 
    elif cmd == "mulr":
        reg[params[3]] = reg[params[1]] * reg[params[2]] 
    elif cmd == "muli":
        reg[params[3]] = reg[params[1]] * params[2] 
    elif cmd == "banr":
        reg[params[3]] = reg[params[1]] & reg[params[2]] 
    elif cmd == "bani":
        reg[params[3]] = reg[params[1]] & params[2] 
    elif cmd == "borr":
        reg[params[3]] = reg[params[1]] | reg[params[2]] 
    elif cmd == "bori":
        reg[params[3]] = reg[params[1]] | params[2] 
    elif cmd == "setr":
        reg[params[3]] = reg[params[1]]
    elif cmd == "seti":
        reg[params[3]] = params[1]
    elif cmd == "gtir":
        if params[1] > reg[params[2]]:
            reg[params[3]] = 1
        else:
            reg[params[3]] = 0
    elif cmd == "gtri":
        if reg[params[1]] > params[2]:
            reg[params[3]] = 1
        else:
            reg[params[3]] = 0
    elif cmd == "gtrr":
        if reg[params[1]] > reg[params[2]]:
            reg[params[3]] = 1
        else:
            reg[params[3]] = 0
    elif cmd == "eqir":
        if params[1] == reg[params[2]]:
            reg[params[3]] = 1
        else:
            reg[params[3]] = 0
    elif cmd == "eqri":
        if reg[params[1]] == params[2]:
            reg[params[3]] = 1
        else:
            reg[params[3]] = 0
    elif cmd == "eqrr":
        if reg[params[1]] == reg[params[2]]:
            reg[params[3]] = 1
        else:
            reg[params[3]] = 0
    else:
        print "Command not found"
    return reg

with open("optcodes.txt", "r") as f:
    lines = f.readlines()

opcode = {}
inputs = 0
for i in range(0, len(lines), 4):
    reg_state_bef = ast.literal_eval(lines[i][8:])
    cmd = map(int, lines[i+1].split())
    reg_state_aft = ast.literal_eval(lines[i+2][8:])
    isOK = 0
    for c in cmds:
        reg =  doCmd(c, cmd, reg_state_bef)
        #print (c, cmd ,reg_state_bef)
        #print reg
        if reg == reg_state_aft:
            #print c, reg
            isOK = isOK + 1
            opcode.setdefault(cmd[0], set([])).add(c)
    if isOK >= 3:
        inputs = inputs + 1
    #print cmd[0], isOK
print inputs

unique_opcode = {}
while 1:
    #print (opcode)
    for op, ops in opcode.iteritems():
        if len(ops) == 1:
            unique_opcode[op] = ops
    for op1, ops1 in unique_opcode.iteritems():
        for op, ops in opcode.iteritems():
            #print set(ops), set(ops1)
            if op1 != op:
                opcode[op].difference_update(set(ops1))
    if len(unique_opcode) == len(opcode):
        break

for op, ops in unique_opcode.iteritems():
    opcode[op] = unique_opcode[op].pop()

with open("program.txt", "r") as f:
    lines = f.readlines()

reg = [0,0,0,0]
for l in lines:
    items = map(int, l.split())
    #print reg, items, opcode[items[0]]
    reg = doCmd(opcode[items[0]], items, reg)
    #print reg

print reg


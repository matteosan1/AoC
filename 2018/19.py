import ast, copy

def doCmd(cmd, params, reg):
    reg = copy.deepcopy(reg)
    params = [0] + params
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
        print ("Command not found")
    return reg

with open("program_19_2.txt", "r") as f:
    lines = f.readlines()

#reg = [21102536, 10551267, 10551267, 10551267, 0, 2]

reg = [1, 0, 0, 0, 0, 0]
program = []
ip_reg = 0
for l in lines:
    if l == "\n" or l.startswith("##"):
        continue
    if l.startswith("#"):
        ip_reg = int(l.split()[1])
    else:
        cmd, params = l.split()[0], map(int, l.split()[1:4])
        program.append([cmd, params])

ip = 0     
count = 0
while 0 <= ip < len(program):
    reg[ip_reg] = ip
        
    old_reg = copy.deepcopy(reg)
    cmd, params = program[ip]
    reg = doCmd(cmd, params, reg)
    #print ip, old_reg, cmd, params, reg
    ip = reg[ip_reg]
    ip = ip + 1
    if ip >= len(program):
        break
    #if count > 1000:
    #    break
    count = count + 1
    #if count % 1000000 == 0:
    #print ip, reg
    
print (reg[0])

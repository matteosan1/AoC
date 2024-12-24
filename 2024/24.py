import timeit, operator

from utils import readInputWithBlank

OPERATORS = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}

def loadInput():
    lines = readInputWithBlank("input_24_prova.txt")
    lines = readInputWithBlank("input_24.txt")
    register = {}
    gates = {}
    isregister = True
    for l in lines:
        if l == "":
            isregister = False
            continue
        if isregister:
            item = l.split(": ")
            register[item[0]] = int(item[1])
        else:
            oper, res = l.split(" -> ")
            oper = oper.split()
            gates[res] = (oper[0], oper[2], oper[1])

    # print (register)
    # print (gates)
    return register, gates

def get_number(register, prefix="z"):
    number_reg = sorted([k for k in register if k.startswith(prefix)], reverse=True)
    binary = "".join([str(register[k]) for k in number_reg])
    #print (binary)
    return int(binary, 2)

def get_operations(n, gates):
    chain = [n]
    regs = [gates[n][0], gates[n][1]]
    while len(regs) > 0:
        res = regs.pop()
        if res in gates:
            chain.append(res)
            regs.append(gates[res][0])
            regs.append(gates[res][1])
    return chain

def part1(register, gates):
    number_regs = []
    for g in gates:
        if g.startswith("z"):
            number_regs.append(g)
    number_regs = sorted(number_regs)
    for n in number_regs:
        for r in reversed(get_operations(n, gates)):
            register[r] = OPERATORS[gates[r][2]](register[gates[r][0]], register[gates[r][1]])

    print (f"🎄 Part 1: {get_number(register)}")
    
def part2(register, gates):
    res = "1011111111010011010110101000100000011011100110"
    true_res = bin(get_number(register, "x") + get_number(register, "y"))[2:]
    print (res)
    print (true_res)
    for i in range(len(res)):
        if res[i] != true_res[i]:
            ops = get_operations("z"+ str(i).zfill(2), gates)
            for o in reversed(ops):
                print (gates[o], end='')
            print ("")

    print (f"🎄🎅 Part 2: {0}")

if __name__ == '__main__':
    title = "Day 24: "
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(*inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    t2 = timeit.timeit(lambda: part2(*inputs), number=1)
    print (f"{t2*1000:.3f} ms")

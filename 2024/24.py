import time, operator

from utils import readInputWithBlank, readInput

OPERATORS = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}

def loadInput(filename):
    lines = readInputWithBlank(filename)
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
    return register, gates

def get_number(register, prefix="z"):
    number_reg = sorted([k for k in register if k.startswith(prefix)], reverse=True)
    binary = "".join([str(register[k]) for k in number_reg])
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
    print (f"🎄 Part 1: {get_number(register)}", end='')
    
def swap(a: str, b: str, device: dict):
    inv = device.inverse
    device[a], device[b] = device[b], device[a]
    inv[device[a]], inv[device[b]] = inv[device[b]], inv[device[a]]
    return a, b

class Device(dict):
    def __init__(self, lines):
        for line in lines:
            line = line.replace(" -> ", " ").split()
            match line: 
                case (wire, bit):          # e.g., ('x00', 1)
                    self[wire] = bit
                case (x, op, y, out):      # e.g., ('y33', 'AND', 'x33', 'bfn')
                    self[out] = canon(x, op, y) # canonicalize order 
        self.inverse = {self[w]: w for w in self if self[w] not in (0, 1)} # Inverse mapping
                    
def canon(x, op, y): 
    return (min(x, y), op, max(x, y))

def wires(device: Device, letter: str): 
    return sorted([w for w in device if w.startswith(letter)], reverse=True)

def find_swaps(device):
    """For each bit position in the inputs, x and y, look forward for the
    XOR and AND gates they participate in, then look backwards from the 
    corresponding z output, and see where they fail to match up,
    and swap wires accordingly, yielding each swapped wire."""
    
    def wire(x, op, y): return device.inverse.get(canon(x, op, y), None)
        
    for i in range(len(wires(device, 'x'))):
        x, y, z = [f'{v}{i:02d}' for v in 'xyz']
        if x == 'x00':
            carry = wire(x, 'AND', y)
        else:
            a, b = carry, wire(x, 'XOR', y)
            if not wire(a, 'XOR', b):
                a2, op, b2, = device[z] # Look backwards from z to see if they hook up
                once = [w for w in (a, b, a2, b2) if [a, b, a2, b2].count(w) == 1]
                if len(once) == 2: # Wires that appear once in the two gates; they don't connect properly
                  yield from swap(*once, device)
            elif wire(a, 'XOR', b) != z:
                yield from swap(z, wire(a, 'XOR', b), device)
            carry = wire(carry, 'AND', wire(x, 'XOR', y)) # The carry gets propagated through two gates
            carry = wire(carry, 'OR',  wire(x, 'AND', y))
    
def part2(register, gates):
    device = Device(readInput("input_24.txt"))
    print (f"🎄🎅 Part 2: {','.join(sorted(find_swaps(device)))}", end='')

if __name__ == '__main__':
    title = "Day 24: Crossed Wire"
    sub = "❄ "*(len(title)//2+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput("input_24.txt")
    
    t0 = time.time()
    part1(*inputs)
    print (" - {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(*inputs)
    print (" - {:.5f}".format(time.time()-t0))

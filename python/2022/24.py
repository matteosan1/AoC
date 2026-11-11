from utils import readInput
from itertools import product
 
def ALU(prog, inputs):
    v = {'w':0, 'x':0, 'y':0, 'z':0}
    digit = 0
 
    for line in prog:
        parts = line.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "inp":
            v[args[0]] = inputs[digit]
            digit += 1
        elif cmd == "add":
            try:
                v[args[0]] += int(args[1])
            except ValueError:
                v[args[0]] += v[args[1]]
        elif cmd == "mul":
            try:
                v[args[0]] *= int(args[1])
            except ValueError:
                v[args[0]] *= v[args[1]]
        elif cmd == "div":
            try:
                v[args[0]] //= int(args[1])
            except ValueError:
                v[args[0]] //= v[args[1]]
        elif cmd == "mod":
            try:
                v[args[0]] %= int(args[1])
            except ValueError:
                v[args[0]] %= v[args[1]]
        elif cmd == "eql":
            try:
                val = int(args[1])
            except ValueError:
                val = v[args[1]]
 
            if args[0] == 'x' and val == -1:
                x = v[args[0]]
                if x >= 1 and x <= 9:
                    v['w'] = x
                    inputs[digit - 1] = x
                    val = x
                else:
                    return v, inputs
 
            v[args[0]] = 1 if v[args[0]] == val else 0
        else:
            raise Exception(f'Unknown cmd {cmd}')
    return v, inputs
 
 
prog = readInput('input_24.txt')
 
for i in product(range(9, 0, -1), repeat=7):
    full_input = [i[0], i[1], i[2], i[3], -1, -1, i[4], -1, i[5], -1, i[6], -1, -1, -1]
    res, inp = ALU(prog, full_input)

    if res['z'] == 0 and -1 not in inp:
        print ("🎄 Part 1: {}".format("".join([str(i) for i in inp])))
        break
 
for i in product(range(1, 10), repeat=7):
    full_input = [i[0], i[1], i[2], i[3], -1, -1, i[4], -1, i[5], -1, i[6], -1, -1, -1]
    res, inp = ALU(prog, full_input)
 
    if res['z'] == 0 and -1 not in inp:
        print ("🎄🎅 Part 2: {}".format("".join([str(i) for i in inp])))
        break


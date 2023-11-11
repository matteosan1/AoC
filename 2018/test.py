#!/usr/bin/env python3

def list_map(f, s):
    return list(map(f, s))

def addr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + result[b]
    return result

def addi(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] + b
    return result

def mulr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * result[b]
    return result

def muli(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] * b
    return result

def banr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & result[b]
    return result

def bani(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] & b
    return result

def borr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | result[b]
    return result

def bori(registers, a, b, c):
    result = registers[::]
    result[c] = result[a] | b
    return result

def setr(registers, a, b, c):
    result = registers[::]
    result[c] = result[a]
    return result

def seti(registers, a, b, c):
    result = registers[::]
    result[c] = a
    return result

def gtir(registers, a, b, c):
    result = registers[::]
    result[c] = bool(a > result[b])
    return result

def gtri(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] > b)
    return result

def gtrr(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] > result[b])
    return result

def eqir(registers, a, b, c):
    result = registers[::]
    result[c] = bool(a == result[b])
    return result

def eqri(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] == b)
    return result

def eqrr(registers, a, b, c):
    result = registers[::]
    result[c] = bool(result[a] == result[b])
    return result

OPERATIONS = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]

def possible_operations(instruction, before, after):
    result = set()
    for operation in OPERATIONS:
        op_result = operation(before, *instruction[1:])
        if op_result == after:
            result.add(operation)
    return result

def problem1(LINES):
    i = 0
    experiments = []
    while LINES[i].strip():
        before, instruction, after = LINES[i:i+3]
        i += 4
        print (before)

        experiments.append((
            list_map(int, instruction.split(' ')),
            eval(before[8:]),
            eval(after[8:])
        ))
    return len([experiment for experiment in experiments if len(possible_operations(*experiment)) >= 3])

def problem2(LINES):
    i = 0
    experiments = []
    while LINES[i].strip():
        before, instruction, after = LINES[i:i+3]
        i += 4
        experiments.append((
            list_map(int, instruction.split(' ')),
            eval(before[8:]),
            eval(after[8:])
        ))

    operations = {opcode : set(OPERATIONS) for opcode in range(16)}
    for experiment in experiments:
        opcode = experiment[0][0]
        operations[opcode].intersection_update(possible_operations(*experiment))

    print (operations)
    while True:
        unique_ops = {}
        for op, ops in operations.items():
            if len(ops) == 1:
                unique_ops[op] = ops
        for op_, ops_ in unique_ops.items():
            for op, ops in operations.items():
                if op != op_:
                    ops.difference_update(ops_)
        if len(unique_ops) == len(operations):
            break
    print (operations)
    for op in operations:
        operations[op] = operations[op].pop()
    registers = [0, 0, 0, 0]
    for line in LINES[i:]:
        if not line.strip():
            continue
        opcode, a, b, c = list_map(int, line.split(' '))
        registers = operations[opcode](registers, a, b, c)
    return registers[0]

def parse_input_file(fname):
    s = open(fname).read()
    if s and s[-1] == '\n':
        s = s[:-1]
    return s.splitlines()

def main():
    l = parse_input_file('input.txt')
    print(problem1(l))
    print(problem2(l))

if __name__ == '__main__':
    main()
    
#{0: {<function eqri at 0x7f4bbbb02048>}, 1: {<function bori at 0x7f4bbbaf5bf8>}, 2: {<function addi at 0x7f4bbbaf58c8>}, 3: {<function bani at 0x7f4bbbaf5ae8>}, 4: {<function seti at 0x7f4bbbaf5d08>}, 5: {<function eqrr at 0x7f4bbbb020d0>}, 6: {<function addr at 0x7f4bbbaf5620>}, 7: {<function gtri at 0x7f4bbbaf5e18>}, 8: {<function borr at 0x7f4bbbaf5b70>}, 9: {<function gtir at 0x7f4bbbaf5d90>}, 10: {<function setr at 0x7f4bbbaf5c80>}, 11: {<function eqir at 0x7f4bbbaf5f28>}, 12: {<function mulr at 0x7f4bbbaf5950>}, 13: {<function muli at 0x7f4bbbaf59d8>}, 14: {<function gtrr at 0x7f4bbbaf5ea0>}, 15: {<function banr at 0x7f4bbbaf5a60>}}

# import copy
#
# def doCmd(cmd, params, reg):
#     reg = copy.deepcopy(reg)
#     params = [0] + params
#     if cmd == "addr":
#         reg[params[3]] = reg[params[1]] + reg[params[2]]
#     elif cmd == "addi":
#         reg[params[3]] = reg[params[1]] + params[2]
#     elif cmd == "mulr":
#         reg[params[3]] = reg[params[1]] * reg[params[2]]
#     elif cmd == "muli":
#         reg[params[3]] = reg[params[1]] * params[2]
#     elif cmd == "banr":
#         reg[params[3]] = reg[params[1]] & reg[params[2]]
#     elif cmd == "bani":
#         reg[params[3]] = reg[params[1]] & params[2]
#     elif cmd == "borr":
#         reg[params[3]] = reg[params[1]] | reg[params[2]]
#     elif cmd == "bori":
#         reg[params[3]] = reg[params[1]] | params[2]
#     elif cmd == "setr":
#         reg[params[3]] = reg[params[1]]
#     elif cmd == "seti":
#         reg[params[3]] = params[1]
#     elif cmd == "gtir":
#         if params[1] > reg[params[2]]:
#             reg[params[3]] = 1
#         else:
#             reg[params[3]] = 0
#     elif cmd == "gtri":
#         if reg[params[1]] > params[2]:
#             reg[params[3]] = 1
#         else:
#             reg[params[3]] = 0
#     elif cmd == "gtrr":
#         if reg[params[1]] > reg[params[2]]:
#             reg[params[3]] = 1
#         else:
#             reg[params[3]] = 0
#     elif cmd == "eqir":
#         if params[1] == reg[params[2]]:
#             reg[params[3]] = 1
#         else:
#             reg[params[3]] = 0
#     elif cmd == "eqri":
#         if reg[params[1]] == params[2]:
#             reg[params[3]] = 1
#         else:
#             reg[params[3]] = 0
#     elif cmd == "eqrr":
#         if reg[params[1]] == reg[params[2]]:
#             reg[params[3]] = 1
#         else:
#             reg[params[3]] = 0
#     else:
#         print ("Command not found")
#     return reg
#
# with open("program_21.txt", "r") as f:
#     lines = f.readlines()
#
# program = []
# ip_reg = 0
# for l in lines:
#     if l == "\n" or l.startswith("##"):
#         continue
#     if l.startswith("#"):
#         ip_reg = int(l.split()[1])
#     else:
#         cmd, params = l.split()[0], list(map(int, l.split()[1:4]))
#         program.append([cmd, params])
#
# reg = [0, 12446070, 9, 4810, 17, 3544629] #[0, 0, 0, 0, 0, 0]
#
# ip = 18
# count = 0
# while 0 <= ip < len(program):
#     reg[ip_reg] = ip
#
#     cmd, params = program[ip]
#     reg = doCmd(cmd, params, reg)
#     ip = reg[ip_reg]
#     print (ip, cmd, params, reg)
#     if ip == 28:
#         print (reg[3])
#     ip = ip + 1
#     if ip >= len(program):
#         break
#     count = count + 1
#     #if count % 10000000 == 0:
#     #    break
#     #    print (reg[0], count)
# print (reg[0], count)
def run_activation_system(magic_number, is_part_1):
    seen = set()
    c = 0
    last_unique_c = -1

    while True:
        a = c | 65536
        c = magic_number

        while True:
            c = (((c + (a & 255)) & 16777215) * 65899) & 16777215

            if 256 > a:
                if is_part_1:
                    return c
                else:
                    if c not in seen:
                        seen.add(c)
                        last_unique_c = c
                        break
                    else:
                        return last_unique_c
            else:
                a //= 256


magic_number = int(open("program_21.txt", "r").readlines()[8].split()[1])
print(run_activation_system(magic_number, True))
print(run_activation_system(magic_number, False))
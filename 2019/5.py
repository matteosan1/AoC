import time
from utils import readInput

def init_code(line):
    return list(map(int, line.split(",")))

def loadInput():
    return readInput("input_5.txt")
    #return readInput("prova.txt")
    
def replace_mem(code, n, val):
    code[n] = val
    
def get_modes(op):
    return [(op//(10**i))%10 for i in range(1, 5)]
    
def get_val(code, modes, pointer, offset=0):
    if modes[offset] == 0:
        return code[code[pointer+offset]]
    elif modes[offset] == 1:
        return code[pointer+offset]
    
def run(code):
    pointer = 0
    while True:
        op = code[pointer]%100
        modes = get_modes(code[pointer])
        #print (modes)
        #print (op, pointer)
        if op == 99:
            break
        elif op == 1:
            code[code[pointer+3]] = get_val(code, modes, pointer, 1) + get_val(code, modes, pointer, 2)
            #code[code[pointer+3]] = code[code[pointer+1]] + code[code[pointer+2]]
            pointer += 4        
        elif op == 2:
            code[code[pointer+3]] = get_val(code, modes, pointer, 1) * get_val(code, modes, pointer, 2)
            #code[code[pointer+3]] = code[code[pointer+1]] * code[code[pointer+2]]
            pointer += 4      
        elif op == 3:
            a = input("Give input ")
            code[code[pointer+1]] = int(a)
            pointer += 2
        elif op == 4:
            print (f"val: {get_val(code, modes, pointer, 1)}")
            #print (code[code[pointer+1]])
            pointer += 2
        elif op == 5:
            if get_val(code, modes, pointer, 1) != 0:
                pointer = get_val(code, modes, pointer, 2)
            else:
                pointer += 3
        elif op == 6:
            if get_val(code, modes, pointer, 1) == 0:
                pointer = get_val(code, modes, pointer, 2)
            else:
                pointer += 3
        elif op == 7:
            if get_val(code, modes, pointer, 1) < get_val(code, modes, pointer, 2):
                code[code[pointer+3]] = 1
            else:
                code[code[pointer+3]] = 0
            pointer += 4
        elif op == 8:
            if get_val(code, modes, pointer, 1) == get_val(code, modes, pointer, 2):
                code[code[pointer+3]] = 1
            else:
                code[code[pointer+3]] = 0
            pointer += 4
        else:
            raise ValueError(f"Unknown instruction: {op}")
    
def part1(lines):
    code = init_code(lines[0])
    run(code)
    print (f"ðŸŽ„ Part 1: {code[0]}")

def part2(lines):
    code = init_code(lines[0])
    run(code)
    print (f"ðŸŽ„ðŸŽ… Part 2:")

if __name__ == "__main__":
    title = "Day 5: Sunny with a Chance of Asteroids"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    lines = loadInput()
    
    t0 = time.time()
    part1(lines)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(lines)
    print ("Time: {:.5f}".format(time.time()-t0))

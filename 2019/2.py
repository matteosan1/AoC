import time
from utils import readInput

def init_code(line):
    return list(map(int, line.split(",")))

def loadInput():
    return readInput("input_2.txt")
    
def replace_mem(code, n, val):
    code[n] = val
    
def run(code):
    pointer = 0
    while True:
        op = code[pointer]
        if op == 99:
            break
        elif op == 1:
            code[code[pointer+3]] = code[code[pointer+1]] + code[code[pointer+2]]
            pointer += 4        
        elif op == 2:
            code[code[pointer+3]] = code[code[pointer+1]] * code[code[pointer+2]]
            pointer += 4        
        else:
            raise ValueError(f"Unknown instruction: {op}")
    
def part1(code):
    replace_mem(code, 1, 12)
    replace_mem(code, 2, 2)
    run(code)
    print (f"ðŸŽ„ Part 1: {code[0]}")

def part2(lines):
    for noun in range(0, 100):
        for verb in range(0, 100):
            code = init_code(lines[0])
            replace_mem(code, 1, noun)
            replace_mem(code, 2, verb)
            run(code)
            if code[0] == 19690720:
                print (f"ðŸŽ„ðŸŽ… Part 2: {100*noun+verb}")
                return

if __name__ == "__main__":
    title = "Day 2: 1202 Program Alarm"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    lines = loadInput()
    
    t0 = time.time()
    code = read_code(lines[0])
    part1(code)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(lines)
    print ("Time: {:.5f}".format(time.time()-t0))

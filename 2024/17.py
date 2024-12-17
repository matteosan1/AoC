import timeit, copy

from utils import readInputWithBlank

# CONSIDERAZIONI SU reminder vs module
# DISASSEMBLER

class IntCode:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.code = None
        self.rom = None
        self.pointer = 0
        self.out = []

    def reset(self):
        self.code = copy.deepcopy(self.rom['code'])
        self.A = self.rom['A']
        self.B = self.rom['B']
        self.C = self.rom['C']
        self.pointer = 0
        self.out = []

    def setCode(self, code):
        self.code = list(map(int, code.split(",")))
        self.rom = {"code":copy.deepcopy(self.code), "A":self.A, "B":self.B, "C":self.C}

    def setRegister(self, A=None, B=None, C=None):
        if A is not None:
            self.A = A
        if B is not None:
            self.B = B
        if C is not None:
            self.C = C

    def combo(self, value):
        if value == 7:
            raise ValueError("Reserved value !")
        if value == 4:
            return self.A
        elif value == 5:
            return self.B
        elif value == 6:
            return self.C
        else:
            return value
        
    def output(self):
        return ",".join(map(str, self.out))

    def run(self, debug=False):
        if debug:
            print (f"A: {self.A} B: {self.B} C: {self.C}")
        while self.pointer < len(self.code):
            optcode = self.code[self.pointer]
            operand = self.code[self.pointer+1]
            if optcode == 0:    # adv
                if debug:
                    print ("adv ", operand)
                self.A = self.A//2**self.combo(operand)
                self.pointer += 2
            elif optcode == 1:  # bxl
                if debug:
                    print ("bxl ", operand)
                self.B ^= operand
                self.pointer += 2
            elif optcode == 2:  # bst
                if debug:
                    print ("bst ", operand)
                self.B = self.combo(operand) % 8
                self.pointer += 2
            elif optcode == 3:  # jnz
                if debug:
                    print ("jnz ", operand)
                
                if self.A != 0:
                    self.pointer = operand
                else:
                    self.pointer += 2
            elif optcode == 4:  # bxc
                if debug:
                    print ("bxc ", operand)
                
                self.B = self.B ^ self.C
                self.pointer  += 2
            elif optcode == 5:  # out
                self.out.append(self.combo(operand) % 8)
                if debug:
                    print ("out ", self.out)
                self.pointer  += 2
            elif optcode == 6:  # bdv
                if debug:
                    print ("bdv ", operand)
                
                self.B = self.A//2**self.combo(operand)
                self.pointer  += 2
            elif optcode == 7:  # cdv
                if debug:
                    print ("cdv ", operand)
                
                self.C = self.A//2**self.combo(operand)
                self.pointer  += 2
            if debug:
                input()

def loadInput():
    #lines = readInputWithBlank("input_17_prova.txt")
    lines = readInputWithBlank("input_17.txt")

    intcode = IntCode()
    for l in lines:
        if l == "":
            continue
        if l.startswith("Register A:"):
            intcode.setRegister(A=int(l.split(": ")[1]))
        elif l.startswith("Register B:"):
            intcode.setRegister(B=int(l.split(": ")[1]))
        elif l.startswith("Register C:"):
            intcode.setRegister(C=int(l.split(": ")[1]))
        else:
            intcode.setCode(l.split(": ")[1])
    return intcode

def part1(intcode):
    intcode.run()
    print (f"🎄 Part 1: {intcode.output()}")

def pyintcode(A):
    B = A%8
    B = B^6
    C = A//2**B
    B = B ^ C
    B = B ^ 4
    return B % 8

def findQuin(A, program, col=0, res=[]):
    if pyintcode(A) != program[-(col + 1)]:
        return

    if col == len(program) - 1:
        res.append(A)
    else:
        for B in range(8):
            findQuin(A * 8 + B, program, col + 1, res)

def part2(intcode):
    intcode.reset()
    program = intcode.code
    res = []
    for a in range(8):
        findQuin(a, program, res=res)

    print (f"🎄🎅 Part 2: {res[0]}")

if __name__ == '__main__':
    title = "Day 17: Chronospatial Computer"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t1 = timeit.timeit(lambda: part1(inputs), number=1)
    print (f"{t1*1000:.3f} ms")
    
    t2 = timeit.timeit(lambda: part2(inputs), number=1)
    print (f"{t2*1000:.3f} ms")


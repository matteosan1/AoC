import time
from utils import readInput

class Compiler:
    def __init__(self):
        self.code = {}
        self.init()
        with open("input_8.txt") as f:
            for i, l in enumerate(f):
                items = l.split(" ")
                self.code[i] = (items[0], int(items[1]))

    def init(self):
        self.code_run = []
        self.accumulator = 0
        self.pointer = 0

    def list(self):
        for v in self.code.values():
            print (v[0], v[1])

    def run(self):
        while self.pointer < len(self.code):
            if not self.inst_run():
                return False
            self.interpret()
        return True

    def interpret(self):
        inst, param = self.code[self.pointer]
        if inst == "nop":
            self.pointer += 1
        elif inst == "acc":
            self.pointer += 1
            self.accumulator += param
        elif inst == "jmp":
            self.pointer += param
        else:
            raise(RuntimeError("Command not found {} {}".format(inst, param)))

    def inst_run(self):
        if self.pointer not in self.code_run:
            self.code_run.append(self.pointer)
            return True
        else:
            return False

    def fix_code(self):
        orig_code = dict(self.code)
        for i in orig_code:
            self.init()
            self.code = dict(orig_code)
            inst, param = self.code[i]
            if inst == "nop" and param != 0:
                self.code[i] = ("jmp", param)
            elif inst == "jmp":
                self.code[i] = ("nop", param)
            else:
                continue
            res = self.run()
            if res:
                return self.accumulator

def part1():
    c = Compiler()
    c.run()
    print ("🎄 Part 1: {}".format(c.accumulator))

def part2():
    c = Compiler()
    print ("🎄🎅 Part 2: {}".format(c.fix_code()))

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 8         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

t0 = time.time()
part1()
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2()
print ("Time: {:.5f}".format(time.time()-t0))

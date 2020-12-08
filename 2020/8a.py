
class Compiler:
    def __init__(self):
        self.code = {}
        with open("input_8a.txt") as f:
            for i, l in enumerate(f):
                items = l.split(" ")
                self.code[i] = (items[0], int(items[1]))
        self.pointer = 0
        self.accumulator = 0
        self.code_run = []

    def list(self):
        for v in self.code.values():
            print (v[0], v[1])

    def run(self):
        while self.pointer < len(self.code):
            self.inst_run()
            self.interpret()

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
        else:
            print (self.accumulator)
            import sys
            sys.exit()

c = Compiler()
c.run()

class Compiler:
    def __init__(self):
        self.code = {}
        with open("input_8a.txt") as f:
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
            #print (self.accumulator)
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
            #print ("----------")
            #self.list()
            res = self.run()
            #print ("acc ", self.accumulator)
            #print ("point", self.pointer)
            #print (res)
            if res:
                print (self.accumulator)
                import sys
                sys.exit()

c = Compiler()
print (c.fix_code())
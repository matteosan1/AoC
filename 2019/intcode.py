import time, copy

class IntCode:
    def __init__(self, name, code, channel={}, mode="manual", output=0):
        self.code = {}
        self.pointer = 0
        self.relative_base = 0
        self.init_code(code)
        self.name = name
        self.mode = mode
        self.mem = channel
        self.output = output
        self.state = "alive"

    def copy_code(self):
        self.orig_code = copy.deepcopy(self.code)

    def reset(self):
        self.code = copy.deepcopy(self.orig_code)
        self.pointer = 0
        self.relative_base = 0
        
    def init_code(self, line):
        self.code = {i:int(v) for i, v in enumerate(line.split(","))}
        
    def get_modes(self, op):
        return [(op//(10**i))%10 for i in range(1, 5)]
            
    def get_val(self, modes, offset=0, is_input=False):
        if modes[offset] == 0:
            idx = self.code[self.pointer + offset]
        elif modes[offset] == 1:
            idx = self.pointer + offset
        elif modes[offset] == 2:
            idx = self.relative_base + self.code[self.pointer + offset]
        if idx < 0:
            raise ValueError(f"Negative memory bank {idx}")
        
        if is_input:
            return idx
        else:
            return self.code.get(idx, 0)

    def run(self):
        while True:
            op = self.code[self.pointer]%100
            modes = self.get_modes(self.code[self.pointer])
            if op == 99:
                self.state = "dead"
                break
            elif op == 1:
                idx = self.get_val(modes, 3, True)
                self.code[idx] = self.get_val(modes, 1) + self.get_val(modes, 2)
                self.pointer += 4        
            elif op == 2:
                idx = self.get_val(modes, 3, True)
                self.code[idx] = self.get_val(modes, 1) * self.get_val(modes, 2)
                self.pointer += 4      
            elif op == 3:
                if self.mode == "manual":
                    a = input("Give input ")
                    idx = self.get_val(modes, 1, True)
                    self.code[idx] = int(a)
                elif self.mode == "channel":
                    if self.name not in self.mem or len(self.mem[self.name]) == 0:
                        self.state = "blocked"
                        break
                    else:
                        self.state = "alive"
                        idx = self.get_val(modes, 1, True)
                        val = self.mem[self.name].popleft()
                        self.code[idx] = val
                self.pointer += 2
            elif op == 4:
                if self.mode == "manual":
                    print (f"val: {self.get_val(modes, 1)}")
                elif self.mode == "channel":
                    self.mem[self.output].append(self.get_val(modes, 1))
                self.pointer += 2
            elif op == 5:
                val = self.get_val(modes, 1)
                if self.get_val(modes, 1) != 0:
                    self.pointer = self.get_val(modes, 2)
                else:
                    self.pointer += 3
            elif op == 6:
                if self.get_val(modes, 1) == 0:
                    self.pointer = self.get_val(modes, 2)
                else:
                    self.pointer += 3
            elif op == 7:
                idx = self.get_val(modes, 3, True)
                self.code[idx] = int(self.get_val(modes, 1) < self.get_val(modes, 2))
                self.pointer += 4
            elif op == 8:
                idx = self.get_val(modes, 3, True)
                self.code[idx] = int(self.get_val(modes, 1) == self.get_val(modes, 2))
                self.pointer += 4
            elif op == 9:
                self.relative_base += self.get_val(modes, 1)
                self.pointer += 2
            else:
                raise ValueError(f"Unknown instruction: {op}")

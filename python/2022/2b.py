import pandas as pd

class Driver:
    def __init__(self, filename):
        self.instr = []
        with open(filename) as f:
            for l in f:
                self.instr.append(l.split("\n")[0])
        self.horiz = 0
        self.depth = 0
        self.aim = 0
        
    def run(self):
        for l in self.instr:
            if l.lstrip() == "":
                continue
            cmd = l.split(" ")
            X = int(cmd[1])
            
            if cmd[0] == "forward":
                self.horiz += X
                self.depth += self.aim * X
            elif cmd[0] == "down":
                self.aim += X
            elif cmd[0] == "up":
                self.aim -= X

    def result(self):
        return self.horiz * self.depth

d = Driver("input_2.txt")
d.run()

print ("🎄🎅 Part 2: ", d.result())


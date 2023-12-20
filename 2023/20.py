import time
from math import prod

from utils import readInput

debug = False

class Output:
    def __init__(self, name):
        self.name = name
        self.state = 0
        self.dest = []

    def receive(self, pulse):
        self.state = pulse[1]
        if debug:
            print (f"{self.name} = {self.state}")
        return []

    def reset(self):
        self.state = 0

class FlipFlop:
    def __init__(self, name, dest):
        self.name = name
        self.state = 0
        self.dest = dest

    def receive(self, pulse):
        if pulse[1] == 0:
            self.state = int(not self.state)
            output = []
            pulse = self.state
            for d in self.dest:
                if debug:
                    print (f"{self.name} -{pulse}-> {d}")
                output.append((d, (self.name, pulse)))
            return output
        return []
        
    def reset(self):
        self.state = 0

class Conjunction:
    def __init__(self, name, dest):
        self.name = name
        self.memory = {}
        self.dest = dest
    
    def receive(self, pulse):
        self.memory[pulse[0]] = pulse[1]
        if all([v == 1 for v in self.memory.values()]):
            self.pulse = 0
        else:
            self.pulse = 1
            
        output = []
        for d in self.dest:
            if debug:
                print (f"{self.name} -{self.pulse}-> {d}")
            output.append((d, (self.name, self.pulse)))
        return output

    def reset(self):
        self.memory = {k:0 for k in self.memory}

class Broadcaster:
    def __init__(self, name, dest):
        self.name = name
        self.dest = dest
        self.pulse = None

    def receive(self, pulse):
        self.pulse = pulse
        output = []
        if self.pulse is not None:
            for d in self.dest:
                if debug:
                    print (f"{self.name} -{self.pulse}-> {d}")
                output.append((d, (self.name, self.pulse)))
            return output

    def reset(self):
        self.pulse = None
        
def loadInput():
    lines = readInput("input_20.txt")
    modules = {}
    for l in lines:
        parts = l.split(" -> ")
        if l.startswith("%"):
            m = FlipFlop(parts[0][1:], parts[1].split(", "))
            modules[parts[0][1:]] = m
        elif l.startswith("&"):
            m = Conjunction(parts[0][1:], parts[1].split(", "))
            modules[parts[0][1:]] = m
        elif l.startswith("broadcaster"):
            m = Broadcaster('braodcaster', parts[1].split(", "))
            modules['broadcaster'] = m
        else:
            raise ValueError("Wrong component")
    #modules['output'] = Output('output')
    modules['rx'] = Output('rx')
    
    conj_map = {k:[] for k, v in modules.items() if isinstance(v, Conjunction)}
    for m in modules.values():
        for ck, cv in conj_map.items():
            if ck in m.dest:
                conj_map[ck].append(m.name)
    for ck, cv in conj_map.items():
        modules[ck].memory = {k:0 for k in cv}
    return modules

def count_pulses(new_output, counter):
    for o in new_output:
        counter[o[1][1]] += 1            

def part1(modules):
    counter = [0, 0]
    cycle = 0
    while True:
        new_output = modules['broadcaster'].receive(0)
        counter[0] += 1
        count_pulses(new_output, counter)
                
        while len(new_output) != 0:
            output = []
            for o in new_output:
                output += modules[o[0]].receive(o[1])
            new_output = output
            count_pulses(new_output, counter)
        cycle += 1
        if cycle == 1000:
            break

    tot = counter[1]*counter[0]
    return tot
    
def part2(modules):
    for m in modules.values():
        m.reset()

    # found by inspecting the input
    conjs = {'ft':0, 'jz':0, 'sv':0, 'ng':0}
    cycle = 0
    while True:        
        new_output = modules['broadcaster'].receive(0)
        while len(new_output) != 0:
            output = []
            for o in new_output:
                if o[0] == 'xm' and o[1][1] == 1:
                    conjs[o[1][0]] = cycle + 1
                output += modules[o[0]].receive(o[1])
            new_output = output            
            
        cycle += 1
        if all([v != 0 for v in conjs.values()]):
            break

    return (prod(conjs.values()))

if __name__ == '__main__':
    title = "Day 20: Pulse Propagation"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()

    t0 = time.time()
    res1 = part1(inputs)
    t1 = time.time()-t0
    
    t0 = time.time()
    res2 = part2(inputs)
    t2 = time.time()-t0
    
    print (f"🎄 Part 1: {res1} ({t1:.5f}) - 🎄🎅 Part 2: {res2} ({t2:.5f})")

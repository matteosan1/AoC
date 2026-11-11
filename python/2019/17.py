import time, re

from collections import deque
from itertools import groupby, combinations      

from utils import readInput
from intcode import IntCode

def loadInput():
    return readInput("input_17.txt")

dirs = {"^": -1j, "v": 1j, "<": -1, ">": 1}

class Robot:
    def __init__(self, scaffold):
        start = next(k for k,v in scaffold.items() if v in '<^>v')
        facing = scaffold[start]

        self._grid = scaffold
        self._loc = start
        self._cur_dir = {
                '^': complex(0, -1),
                '>': complex(1, 0),
                'v': complex(0, 1),
                '<': complex(-1, 0),
            }[facing]

    def find_path(self):
        steps = []
        move = self._next_move()
        while move is not None:
            steps.append(move)
            move = self._next_move()
        return steps

    def _is_scaffold(self, loc):
        return self._grid.get(loc, '.') in '#<^>v'

    def _next_move(self):
        steps = 0
        while self._is_scaffold(self._loc + self._cur_dir):
            steps += 1
            self._loc = self._loc + self._cur_dir
        if steps:
            return steps

        self._cur_dir = complex(self._cur_dir.imag, -self._cur_dir.real)
        if self._is_scaffold(self._loc + self._cur_dir):
            return 'L'

        # about face (cumulative right turn)
        self._cur_dir = complex(-self._cur_dir.real, -self._cur_dir.imag)
        if self._is_scaffold(self._loc + self._cur_dir):
            return 'R'


def count_repetitions(pattern, full, start=0):
    pat_len = len(pattern)
    c = 0
    for idx in range(start, len(full)-pat_len+1):
        if full[idx:idx+pat_len] == pattern:
            c += 1
    return c

def subsequence_frequencies(path):
    freqs = {}
    max_len = (len(path) // 2) + 1
    for length in range(1, max_len):
        for start in range(len(path)-length):
            pattern = path[start:start+length]
            if tuple(pattern) not in freqs:
                c = count_repetitions(pattern, path, start)
                freqs[tuple(pattern)] = c
    return freqs

class ProgBuilder:
    class BuildFailed(Exception):
        pass

    def __init__(self, path):
        freqs = subsequence_frequencies(path)
        subs = [k for k, v in freqs.items()
                if len(','.join(str(i) for i in k)) <= 20
                   and v > 1]
        subs = sorted(subs, key=lambda v: -len(v))

        self._path = path
        self._subs = subs

        main, parts = self._build_program()

        main = [chr(ord('A') + p) for p in main]
        parts = [[str(v) for v in p] for p in parts]
        while len(parts) < 3:
            parts.append(('L', 'R'))

        self._prepare_prog(main, parts)

    def _build_program(self, main=[], parts=[]):
        expanded = self._expand(main, parts)
        if expanded == self._path:
            return main, parts


        start = len(expanded)
        opts = self._options(main, parts, start)
        for o in opts:
            next_parts = list(parts)
            if o not in next_parts:
                next_parts.append(o)
            if len(next_parts) > 3:
                continue
            idx = next_parts.index(o)
            next_main = main + [idx]

            try:
                return self._build_program(next_main, next_parts)
            except self.BuildFailed:
                pass

        raise self.BuildFailed("Failed to build program")

    def _expand(self, main, parts):
        prog = []
        for idx in main:
            prog.extend(parts[idx])
        return prog

    def _options(self, main, parts, start):
        return [i for i in self._subs
                if len(i) < len(self._path) - start + 1
                   and self._path[start:start+len(i)] == list(i)] 

    def _prepare_prog(self, main, parts):
        prog = ','.join(main) + '\n'
        for p in parts:
            prog += ','.join(p) + '\n'
        prog += '{}' + '\n'

        self._prog = prog

    def prog(self, verbose=False):
        return self._prog.format('y' if verbose else 'n')


#class Routine:
#    def __init__(self, string, verbose=False):
#        self._verbose = verbose
#        self._iterator = iter(string)
#
#    def __call__(self):
#        c = next(self._iterator)
#        if self._verbose:
#            print(c, end='')
#        return ord(c)
#
#class CaptureLastOut:
#    def __init__(self, do_output=False):
#        self.last = 0
#        self.do_output = do_output
#
#    def __call__(self, val):
#        self.last = val
#        if self.do_output and val < 128:
#            print(chr(val), end='')
#
#verbose = False
#path = Robot(c.grid).find_path()
#program = ProgBuilder(path).prog(verbose)
#
#code[0] = 2
#show_io = verbose or False
#routine = Routine(program, show_io)
#capture = CaptureLastOut(show_io)
#Interpreter(routine, capture).run(code)
#
#print(capture.last)

#def show(scaffold, start, dir):
#    xs = [h.real for h in scaffold]
#    ys = [h.imag for h in scaffold]
#    xmin, xmax = min(xs), max(xs)
#    ymin, ymax = min(ys), max(ys)
#    for y in range(int(ymin), int(ymax+1)):
#        for x in range(int(xmin), int(xmax+1)):
#            pos = complex(x, y)
#            if pos in scaffold:
#                print(chr(scaffold[pos]), end='')
#            else:
#                print(" ", end='')
#            
#        print()

def parse_scaffold(scaffold):
    m = {}
    x = 0
    y = 0
    for c in scaffold:
        if c == 10:
            y += 1
            x = -1
        elif c != 46:
            m[complex(x, y)] = chr(c)
        x += 1
    return m
        
def find_intersections(scaffold):
    intersections = []
    for p in scaffold:
        adj = sum(1 for d in dirs.values() if p + d in scaffold)
        if adj == 4:
            intersections.append(p)

    calib = 0
    for i in intersections:
        calib += i.real*i.imag
    return int(calib)
            
def part1(lines):
    channel = {"Robot":deque([]), "me":deque([])}
    prog = IntCode("Robot", lines[0], channel=channel, mode="channel", output="me")
    prog.run()
    scaffold = parse_scaffold(channel["me"])
    #show(scaffold, start, dir)
    print (f"🎅 Part 1: {find_intersections(scaffold)}")
    return scaffold

def get_path(scaffold):
    path = []
    steps = 0
    bot = [None, None]
    bot[0] = [i for i in scaffold if scaffold[i] in dirs.keys()][0]
    bot[1] = dirs[scaffold[bot[0]]]
    #print (bot)
    while True:
        if bot[0] + bot[1] in scaffold:
            steps += 1
            bot[0] += bot[1]
        else:
            if len(path):
                path.append(str(steps))

            if bot[0] + bot[1] * -1j in scaffold:
                bot[1] *= -1j
                path.append("L")
                steps = 0
            elif bot[0] + bot[1] * 1j in scaffold:
                bot[1] *= 1j
                path.append("R")
                steps = 0
            else:
                break
    return path

def group_list(lst):
    res = []    
    for x, y in groupby(lst):
        if x == "1":
            res.append(str(len(list(y))))
        else:
            res.append(x)
    return res
    
def toascii(seq):
    ascii = []
    for i, c in enumerate(list(seq)):
        ascii.append(ord(c))
        #if i < len(seq)-1:
        #    ascii.append(ord(","))        
    ascii.append(ord("\n"))
    return ascii

def print_output(lst):
    s = ""
    while len(lst) > 0:
        s += chr(lst.popleft())
    print (s)

def find_repeat(path, registers=[], sequence=[]):
    cleared = False
    while not cleared:
      cleared = True
  
      for i, prev in enumerate(registers):
        if len(prev) <= len(path) and path[:len(prev)] == prev:
          path = path[len(prev):]
          sequence.append(i)
          cleared = False
          break
  
    if len(registers) == 3:
      return (True, registers, sequence) if len(path) == 0 else (False, None, None)
  
    register_len = min(len(path), 10)

    while len(",".join(path[:register_len])) > 18 \
       or path[register_len - 1] in {'R', 'L'}:
      register_len -= 1
  
    while register_len > 0:
      res, matches, seq = find_repeat(path, registers + [path[:register_len]], sequence.copy())
      if res:
        return [res, matches, seq]
      register_len -= 2
  
    return [False, [], []]

def find_rep(path, i=0, repetitions=[]):
    if i == 3:
        return
    max_len = 12
    temp = []
    for x in range(max_len, 1, -1):
        seq = path[0:x]
        reps = re.findall(seq, path)
        if len(reps) > 1:
            temp.append(reps[0])
    if len(temp) > 0:
        for t in temp:
            if i == 0:
                repetitions = []
            new_path = path.replace(t[0], "")
            if len(new_path) > 0:
                repetitions.append(t)
                print (repetitions)
                find_rep(new_path, i+1, repetitions)
            else:
                return repetitions

def part2(lines, scaffold):
    #path = "".join(group_list(get_path(scaffold)))
    #print (path)
    #regs = find_repeat(path)
    #print(find_rep(path))
    regs = [["L,10,R,8,R,8", "L,10,L,12,R,8,R,10", "R,10,L,12,R,10"], "A,A,B,C,B,C,B,C,C,A"]
    #for i in range(3):
    #    regs[1][i] = "".join(regs[1][i])
    #regs[2] = "".join([chr(65+i) for i in regs[2]])

    channel = {"Robot":deque([]), "me":deque([])}
    prog = IntCode("Robot", lines[0], channel=channel, mode="channel", output="me")
    channel["Robot"].extend(toascii(regs[1])+
                            toascii(regs[0][0])+
                            toascii(regs[0][1])+
                            toascii(regs[0][2])+
                            toascii(["n"]))
    
    prog.code[0] = 2
    prog.run()
    print (f"🎅🎄 Part 2: {channel['me'][-1]}")

if __name__ == "__main__":
    title = "Day 17: Set and Forget"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    lines = loadInput()
    
    t0 = time.time()
    scaffold = part1(lines)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    path = part2(lines, scaffold)
    print ("Time: {:.5f}".format(time.time()-t0))


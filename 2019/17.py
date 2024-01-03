import time, re

from collections import deque
from itertools import groupby, combinations      

from utils import readInput
from intcode import IntCode

def loadInput():
    return readInput("input_17.txt")

def show(scaffold, start, dir):
    xs = [h.real for h in scaffold]
    ys = [h.imag for h in scaffold]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    for y in range(int(ymin), int(ymax+1)):
        for x in range(int(xmin), int(xmax+1)):
            pos = complex(x, y)
            if pos in scaffold:
                if pos == start:
                    if dir == 0:
                        print("^", end='')
                    elif dir == 1:
                        print(">", end='')
                    elif dir == 2:
                        print("v", end='')
                    elif dir == 3:
                        print("<", end='')
                else:
                    print("▮", end='')
            else:
                print(" ", end='')
            
        print()

def parse_scaffold(scaffold):
    m = {}
    x = 0
    y = 0
    for c in scaffold:
        if c == 35:
            m[complex(x, y)] = 1
        elif c == ord('v'):
            m[complex(x, y)] = 1
            start = complex(x, y)
            dir = 2
        elif c == ord('^'):
            m[complex(x, y)] = 1        
            start = complex(x, y)
            dir = 0
        elif c == ord('>'):
            m[complex(x, y)] = 1        
            start = complex(x, y)
            dir = 1
        elif c == ord('<'):
            m[complex(x, y)] = 1        
            start = complex(x, y)
            dir = 3
        elif c == 10:
            y += 1
            x = -1
        x += 1
    return m, start, dir
    
dirs = {0:lambda x: x-1j,
        1:lambda x: x+1,
        2:lambda x: x+1j,
        3:lambda x: x-1}
        
def find_intersections(scaffold, start, dir):
    pos = start
    actual_dir = dir
    visited = [start]
    intersections = []
    path = []
    while True:
        new_dirs = []
        for i,d in dirs.items():
            if d(pos) in scaffold:
                if i == (actual_dir-2)%4:
                    continue
                new_dirs.append(i)
        if len(new_dirs) == 3:
            intersections.append(pos)
            pos = dirs[actual_dir](pos)
            p = "1"
        elif len(new_dirs) == 0:
            break
        else:
            pos = dirs[new_dirs[0]](pos)
            delta = new_dirs[0] - actual_dir
            if delta == -3:
                p = "R"
            elif delta == 3:
                p = "L"
            elif delta > 0:
                p = "R"
            elif delta < 0:
                p = "L"
            else:
                p = "1"
            actual_dir = new_dirs[0]
            visited.append(pos)
            
        path.append(p)
    calib = 0
    for i in set(intersections):
        calib += i.real*i.imag
    return (int(calib), path)
            
    
def part1(lines):
    channel = {"Robot":deque([]), "me":deque([])}
    prog = IntCode("Robot", lines[0], channel=channel, mode="channel", output="me")
    prog.run()
    scaffold, start, dir = parse_scaffold(channel["me"])
    #show(scaffold, start, dir)
    nins, path = find_intersections(scaffold, start, dir)
    print (f"🎅 Part 1: {nins}")
    return path
    
def group_list(lst):
    res = []    
    for x, y in groupby(lst):
        if x == "1":
            res.append(str(len(list(y))))
        else:
            res.append(x)
    print (res)   
    return res

def guess_seq_len2(seq):
    seq = "".join(seq)
    print (seq)
    seqs = []
    max_len = len(seq)//2
    for offset in range(0, max_len):
        for x in range(2, max_len):
            if offset + x > max_len:
                continue
            sub = seq[offset:x+offset]
            occurrences = [m.start() for m in re.finditer(sub, seq)]
            if len(occurrences) > 1 and len(occurrences) <= 3:
                seqs.append((len(sub), sub, len(occurrences)))
    return seqs
    
def toascii(seq):
    ascii = []
    for c in list(seq):
        ascii.append(ord(c))
    return ascii

def print_output(lst):
    s = ""
    while len(lst) > 0:
        s += chr(lst.popleft())
    print (s)
    
def part2(lines, path):
    #res = group_list(path)
    #seqs = guess_seq_len2(res)
    #print (sorted(seqs, key=lambda x: x[0]))
    #return 0
    
    channel = {"Robot":deque([]), "me":deque([])}
    prog = IntCode("Robot", lines[0], channel=channel, mode="channel", output="me")
    main_routine = toascii("A,A,B,B,B,C,A\n")
    routine = [toascii("L,9,R,7,R,7\n"), toascii("L,9,L,1,1,R,7,R,9,R,9,L,1,1,R,9\n"), toascii("R,9,L,1,1,R,9\n")]
    print (routine[0])
    routine[0] = [82, 44, 52, 44, 82, 44, 52, 44, 82, 44, 56, 10]

    #channel["Robot"].extend(toascii("n\n"))
    #print (len(channel["Robot"]))
    prog.code[0] = 2
    prog.run()
    print_output(channel['me'])
    channel["Robot"].extend(main_routine)
    prog.run()
    print_output(channel['me'])
    channel["Robot"].extend(routine[0])
    prog.run()
    print (channel['me'])
    print_output(channel['me'])
    
   #sprint (f"🎅🎄 Part 2: {0}")

if __name__ == "__main__":
    title = "Day 17: Set and Forget"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    lines = loadInput()
    
    t0 = time.time()
    path = part1(lines)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    path = part2(lines, path)
    print ("Time: {:.5f}".format(time.time()-t0))


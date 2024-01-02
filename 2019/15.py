import time

from utils import readInput
from intcode import IntCode
from collections import deque
            
def loadInput():
    return readInput("input_15.txt")

def show_hull(hull):
    xs = [h.real for h in hull]
    ys = [h.imag for h in hull]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    for y in range(int(ymin), int(ymax+1)):
        for x in range(int(xmin), int(xmax+1)):
            pos = complex(x, y)
            if pos in hull:
                if hull[pos] == 0:
                    print("▮", end='')
                else:
                    print(".", end='')
            else:
                print(" ", end='')                
        print()

def part1(lines):
    channel = {"Droid":deque([]), "me":deque([])}
    prog = IntCode("Droid", lines[0], channel=channel, mode="channel", output="me")
    section = {}
    pos = complex(0,0)
    dir = 1
    channel["Droid"].append(dir)
    while True:
        prog.run()
        answ = channel["me"].pop()
        if answ == 0:
            dir += 1
            if dir > 4:
                dir -= 4
        elif answ == 1:            
            section[pos] = 1
            if dir == 1:
                pos -= -1j
            elif dir == 2:
                pos += 1
            elif dir == 3:
                pos += 1j
            else:
                pos -= 1
        elif answ == 2:
            break
        #print (section)
        channel["Droid"].append(dir)
        print ("------------------")
        if len(section) != 0:
            show_hull(section)
        #print (visited)
    
            

    #print (f"🎅 Part 1: {len(playground[0])}")

#def show_game(playground, dir):
#    xs = [h.real for h in playground[1]]
#    ys = [h.imag for h in playground[1]]
#    xmin, xmax = min(xs), max(xs)
#    ymin, ymax = min(ys), max(ys)
#    for y in range(int(ymin), int(ymax+1)):
#        for x in range(int(xmin), int(xmax+1)):
#            pos = complex(x, y)
#            if pos in playground[0]:
#                print("▮", end='')
#            elif pos == playground[2]:
#                if dir == -1:
#                    print("<", end='')
#                elif dir == 1:
#                    print(">", end='')
#                else:
#                    print("W", end='')
#            elif pos == playground[3]:
#                print("O", end='')
#            else:
#                print(" ", end='')
#        print()
    
def part2(lines):
    return 0
    channel = {"Sim":deque([]), "me":deque([])}
    prog = IntCode("Sim", lines[0], channel=channel, mode="channel", output="me")
    prog.code[0] = 2
    prog.run()
    playground = read_output(channel["me"])
    dir = 1
    ball_old = playground[3]
    pad_old = playground[2]
    score_old = playground[4]
    channel["Sim"].append(0)
    while playground[3].imag < 20:
        prog.run()
        if not prog.alive:
            break;
        playground = read_output(channel["me"])
        ball = playground[3]
        pad = playground[2]
        score = playground[4]
        if ball.real > ball_old.real:
            dir = 1
        else:
            dir = -1

        move = 0
        if ball.real == pad.real:
            move = dir
        else:
            if ball.real > pad.real:
                move = 1
            else:
                move = -1
        channel["Sim"].append(move)
        #show_game(playground, move)
        
        ball_old = ball
        pad_old = pad
        channel["me"].clear()
    final_score = channel['me'][-1]
    print (f"🎅🎄 Part 2: {final_score}")

if __name__ == "__main__":
    title = "Day 15: Oxygen System"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    lines = loadInput()
    
    t0 = time.time()
    part1(lines)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(lines)
    print ("Time: {:.5f}".format(time.time()-t0))

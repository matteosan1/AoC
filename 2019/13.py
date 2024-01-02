import time, copy

from utils import readInput
from intcode import IntCode
from collections import deque
            
def loadInput():
    return readInput("input_13.txt")

def read_output(deq):
    blocks = []
    walls = []
    ball = None
    pad = None
    score = 0
    for i in range(2, len(deq), 3):
        pos = complex(deq[i-2], deq[i-1])
        tile_id = deq[i]
        if tile_id == 2:
            blocks.append(pos)
        elif tile_id == 1:
            walls.append(pos)
        elif tile_id == 3:
            pad = pos
        elif tile_id == 4:
            ball = pos
        elif pos.real == -1:
            score = tile_id
    return (blocks, walls, pad, ball, score)

def part1(lines):
    channel = {"Sim":deque([])}
    prog = IntCode("Sim", lines[0], channel=channel, mode="channel", output="Sim")
    prog.run()
    playground = read_output(channel["Sim"])    
    print (f"🎅 Part 1: {len(playground[0])}")

def show_game(playground, dir):
    xs = [h.real for h in playground[1]]
    ys = [h.imag for h in playground[1]]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    for y in range(int(ymin), int(ymax+1)):
        for x in range(int(xmin), int(xmax+1)):
            pos = complex(x, y)
            if pos in playground[0]:
                print("▮", end='')
            elif pos == playground[2]:
                if dir == -1:
                    print("<", end='')
                elif dir == 1:
                    print(">", end='')
                else:
                    print("W", end='')
            elif pos == playground[3]:
                print("O", end='')
            else:
                print(" ", end='')
        print()
    
def part2(lines):
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
    title = "Day 13: Care Package"
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

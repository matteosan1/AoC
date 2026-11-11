import time, copy

from queue import Queue
from threading import Thread

from utils import readInput
from intcode import IntCode
            
def loadInput():
    return readInput("input_13.txt")

class Board:
    def __init__(self):
        self.blocks = []
        self.walls = []
        self.pad = (0, 0)
        self.ball = (0, 0)
        self.score = 0

    def read(self, queue):
        triplet = []
        for i in range(3):
            try:
                triplet.append(queue.get(block=False))
            except:
                return False
            if triplet[-1] == "BYE":
                return False
        if triplet[2] == 2:
            self.blocks.append((triplet[0], triplet[1]))
        elif triplet[2] == 1:
            self.walls.append((triplet[0], triplet[1]))
        elif triplet[2] == 3:
            self.pad = (triplet[0], triplet[1])
        elif triplet[2] == 4:
            self.ball = (triplet[0], triplet[1])
        elif triplet[0] == -1:
            self.score = triplet[2]
        return True
                
    def show_game(self, dir):
        xs = [h[0] for h in self.walls]
        ys = [h[1] for h in self.walls]
        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)
        for y in range(int(ymin), int(ymax+1)):
            for x in range(int(xmin), int(xmax+1)):
                pos = (x, y)
                if pos in self.blocks:
                    print("▮", end='')
                elif pos == self.pad:
                    if dir == -1:
                        print("<", end='')
                    elif dir == 1:
                        print(">", end='')
                    else:
                        print("W", end='')
                elif pos == self.ball:
                    print("O", end='')
                else:
                    print(" ", end='')
            print()

def part1(lines):
    board = Board()
    channel = {"Sim":Queue(), "me":Queue()}
    prog = IntCode("Sim", lines[0], qin=channel['Sim'], qout=channel['me'], mode="channel")
    
    prog.run()
    while True:
        if not board.read(channel["me"]):
            break
    print (f"🎅 Part 1: {len(board.blocks)}")

from threading import Thread
    
def part2(lines):
    board = Board()
    channel = {"Sim":Queue(), "me":Queue()}
    prog = IntCode("Sim", lines[0], qin=channel['Sim'], qout=channel['me'], mode="channel")
    prog.code[0] = 2
    prog.run()
    while True:
        if not board.read(channel["me"]):
            break
    dir = 1
    ball_old = board.ball
    pad_old = board.ball
    score_old = board.score
    channel["Sim"].put(0)

    while board.ball[1] < 20:    
        prog.run()
        while True:
            if not board.read(channel["me"]):
                break

        if prog.state == "dead":
            break

        ball = board.ball
        pad = board.pad
        if ball[0] > ball_old[0]:
            dir = 1
        else:
            dir = -1
        move = 0
        if ball[0] == pad[0]:
            move = dir
        else:
            if ball[0] > pad[0]:
                move = 1
            else:
                move = -1
        channel["Sim"].put(move)
        ball_old = ball
        pad_old = pad
    print (f"🎅🎄 Part 2: {board.score}")

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

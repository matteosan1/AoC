from utils import readInput
import numpy as np
import numpy.ma as ma

class Board:
    def __init__(self, numbers):
        self.board = numbers

    def check(self, drawn):
        res = np.isin(self.board, drawn)
        rw = np.array([True]*5)
        cw = rw.T
        winner = None
        for i in range(5):
            if np.all(np.equal(res[:, i], rw)):
                winner = self.board[:, i]
                break
            if np.all(np.equal(res[i, :], cw)):
                winner = self.board[i, :]
                break
        if winner is not None:
            mx = ma.masked_array(self.board, mask=res)
            s = mx.sum()
            return drawn[-1]*s

bs = []
with open("input_4.txt", "r") as f:
    b = []
    for il, l in enumerate(f):
        if il == 0:
            drawn = [int(v) for v in l.split("\n")[0].split(",")]
        elif l.strip() == "" and il > 1:
            bs.append(np.array(b))
            b = []
        elif il > 1:
            l = l.replace("  ", " ")
            b.append([int (v.lstrip()) for v in l.split("\n")[0].split(" ") if v != ""])

boards = []
for b in bs:
    boards.append(Board(b))

for i in range(5, len(drawn)):
    for b in boards:
        res = b.check(drawn[:i])
        if res:
            print ("🎄 Part 1: ", res)
            import sys
            sys.exit(0)


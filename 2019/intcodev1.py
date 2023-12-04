from collections import defaultdict
from typing import DefaultDict, List, Optional, Tuple
import operator

class Intcode:
    memory: List[int]
    oob: DefaultDict[int, int]
    ip: int
    base: int
    halted: bool

    def __init__(self, memory: List[int]) -> None:
        self.memory = memory + ([0] * len(memory))
        self.oob = defaultdict(int, enumerate(memory))
        self.ip = 0
        self.base = 0
        self.halted = False

    def __repr__(self) -> str:
        return f"Intcode(ip={self.ip}, base={self.base}, halted={self.halted})"

    def debug_negative_index(self, i: int) -> None:
        print("debug memory addresses:")
        print(self[self.ip])
        print(self[self.ip+1])
        print(self[self.ip+2])
        print(self[self.ip+3])
        print("debug index:")
        print(i)

    def __getitem__(self, i: int) -> int:
        if i < 0:
            self.debug_negative_index(i)
            raise IndexError("negative index")
        if i < len(self.memory):
            return self.memory[i]
        else:
            return self.oob[i]

    def __setitem__(self, i: int, item: int) -> int:
        if i < 0:
            self.debug_negative_index(i)
            raise IndexError("negative index")
        if i < len(self.memory):
            self.memory[i] = item
        else:
            self.oob[i] = item

    def addr(self, param: int) -> int:
        out = self.ip + param
        mode = (self[self.ip] // pow(10, param + 2 - 1)) % 10
        if mode == 0:
            out = self[out]
        elif mode == 1:
            pass
        elif mode == 2:
            out = self[out] + self.base
        else:
            raise Exception("bad mode")
        return out

    def run(self, inp: Optional[int] = None) -> Tuple[bool, List[int]]:
        if self.halted:
            raise Exception("already halted")
        out = []
        while True:
            op = self[self.ip] % 100
            if op == 1 or op == 2 or op == 7 or op == 8:
                if op == 1:
                    res = self[self.addr(1)] + self[self.addr(2)]
                elif op == 2:
                    res = self[self.addr(1)] * self[self.addr(2)]
                elif op == 7:
                    res = int(self[self.addr(1)] < self[self.addr(2)])
                else:
                    res = int(self[self.addr(1)] == self[self.addr(2)])
                self[self.addr(3)] = res
                self.ip += 4
            elif op == 5 or op == 6:
                if (op == 5) == bool(self[self.addr(1)]):
                    self.ip = self[self.addr(2)]
                else:
                    self.ip += 3
            elif op == 9:
                self.base += self[self.addr(1)]
                self.ip += 2
            elif op == 3:
                if inp is None:
                    return (False, out)
                self[self.addr(1)] = inp
                inp = None
                self.ip += 2
            elif op == 4:
                out.append(self[self.addr(1)])
                self.ip += 2
            elif op == 99:
                self.halted = True
                return (True, out)
            else:
                raise Exception("invalid opcode " + str(op))
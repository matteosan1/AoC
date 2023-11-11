from utils import readInput

class Parser:
    def __init__(self, msg):
        self.msg = msg

    def parse(self):
        idx = 0
        dec_msg = ""
        while idx < len(self.msg):
            if self.msg[idx] == "(":
                idx += 1
                close = self.msg[idx:].find(")")
                decompression = self.msg[idx:idx+close].split("x")
                idx += close+1
                decompression = list(map(int, decompression))
                for i in range(decompression[1]):
                    dec_msg += self.msg[idx:idx+decompression[0]]
                idx += decompression[0]
            else:
                dec_msg += self.msg[idx]
                idx += 1
        return dec_msg


lines = readInput("test.txt")
p = Parser(lines[0])
print (p.parse())
print ("🎄Part 1: {}".format(len(p.parse())))

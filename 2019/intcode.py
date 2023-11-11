class IntCode:
    def __init__(self, filename):
        with open(filename) as f:
            line = f.readline()    
        self.intcode = list(map(int, line.split(",")))
        self.pointer = 0
        
    def run(self):
        while True:
            optcode = self.intcode[self.pointer] % 100
            modes = [int(d) for d in str(intcode[index] // 100)[::-1]]
            
            if optcode == 99:
                break
            elif optcode == 1:
                self.intcode[self.intcode[self.pointer + 3]] = self.intcode[self.intcode[self.pointer + 1]] + self.intcode[self.intcode[self.pointer + 2]]
                offset = 4
            elif optcode == 2:
                self.intcode[self.intcode[self.pointer + 3]] = self.intcode[self.intcode[self.pointer + 1]] * self.intcode[self.intcode[self.pointer + 2]]
                offset = 4
            elif optcode == 3:
                self.intcode[self.intcode[self.pointer + 1]] = int(input('Input: '))
                offset = 2
            elif optcode == 4:
                print (self.intcode[self.intcode[self.pointer + 1]])
                offset = 2
                
            self.pointer += offset
            


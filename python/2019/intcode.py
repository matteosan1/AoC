import time, copy

#class BlockingQueue:
#    def __init__(self, maxsize=0):
#        self.queue = queue.Queue(maxsize)
#        self.lock = threading.Lock()
#        self.empty_event = threading.Event()
#        self.full_event = threading.Event()
#        
#    def empty(self):
#        return self.queue.empty()
#
#    def put(self, item):
#        with self.lock:
#            #while self.queue.full():
#            #    self.full_event.wait()
#
#            self.queue.put(item)
#            self.empty_event.set()
#            
#    def super_get(self, label):
#        val = None
#        with self.lock:
#            while self.queue.empty():
#                self.empty_event.wait()   
#                #if self.peek() is not None
#                #if self.peek()[0] == label:
#            val = self.queue.get()[1]  
#        return val
#
#    def get(self, timeout=None):
#        with self.lock:
#            while self.queue.empty():
#                self.empty_event.wait(timeout)
#
#                if timeout and timeout < time.monotonic():
#                    return None
#
#            item = self.queue.get()
#            self.full_event.set()
#
#            return item
#
#    def peek(self):
#        with self.lock:
#            if self.queue.empty():
#                return None
#
#            return self.queue.queue[0]

class IntCode:
    def __init__(self, name, code, qin=None, qout=None, channel={}, mode="manual", output=0):
        self.code = {}
        self.pointer = 0
        self.relative_base = 0
        self.init_code(code)
        self.name = name
        self.mode = mode
        #self.mem = channel
        self.output = output
        self.state = "alive"
        self.qin = qin
        self.qout = qout
        #self.queue = queue

    def copy_code(self):
        self.orig_code = copy.deepcopy(self.code)

    def reset(self):
        self.code = copy.deepcopy(self.orig_code)
        self.pointer = 0
        self.relative_base = 0
        
    def init_code(self, line):
        self.code = {i:int(v) for i, v in enumerate(line.split(","))}
        
    def get_modes(self, op):
        return [(op//(10**i))%10 for i in range(1, 5)]
            
    def get_val(self, modes, offset=0, is_input=False):
        if modes[offset] == 0:
            idx = self.code[self.pointer + offset]
        elif modes[offset] == 1:
            idx = self.pointer + offset
        elif modes[offset] == 2:
            idx = self.relative_base + self.code[self.pointer + offset]
        if idx < 0:
            raise ValueError(f"Negative memory bank {idx}")
        
        if is_input:
            return idx
        else:
            return self.code.get(idx, 0)

    def run(self, logic=None):
        #print ("GO")
        while True:
            op = self.code[self.pointer]%100
            modes = self.get_modes(self.code[self.pointer])
            if op == 99:
                self.state = "dead"
                self.qout.put("BYE")
                break
            elif op == 1:
                idx = self.get_val(modes, 3, True)
                self.code[idx] = self.get_val(modes, 1) + self.get_val(modes, 2)
                self.pointer += 4        
            elif op == 2:
                idx = self.get_val(modes, 3, True)
                self.code[idx] = self.get_val(modes, 1) * self.get_val(modes, 2)
                self.pointer += 4      
            elif op == 3:
                if self.mode == "manual":
                    val = int(input("Give input "))                    
                elif self.mode == "channel":
                    #if self.name not in self.mem or len(self.mem[self.name]) == 0:
                    #    self.state = "blocked"
                    #    break
                    #else:
                    #    self.state = "alive"
                    #    val = self.mem[self.name].popleft()
                    if self.qin.empty():
                        break                    
                    val = self.qin.get()
                elif self.mode == "thread":
                    #print (f"{self.name} is waiting...")
                    val = self.qin.get(block=True)                    
                    #print (f"{self.name} {val}")
                idx = self.get_val(modes, 1, True)
                self.code[idx] = val                
                self.pointer += 2
            elif op == 4:                
                val = self.get_val(modes, 1)
                #print(val)
                if self.mode == "manual":
                    #print (f"val: {self.get_val(modes, 1)}")
                    self.output = val
                elif self.mode == "channel":
                    #self.mem[self.output].append(self.get_val(modes, 1))
                    self.qout.put(val)
                elif self.mode == "thread":
                    self.qout.put(val)
                self.pointer += 2
            elif op == 5:
                val = self.get_val(modes, 1)
                if self.get_val(modes, 1) != 0:
                    self.pointer = self.get_val(modes, 2)
                else:
                    self.pointer += 3
            elif op == 6:
                if self.get_val(modes, 1) == 0:
                    self.pointer = self.get_val(modes, 2)
                else:
                    self.pointer += 3
            elif op == 7:
                idx = self.get_val(modes, 3, True)
                self.code[idx] = int(self.get_val(modes, 1) < self.get_val(modes, 2))
                self.pointer += 4
            elif op == 8:
                idx = self.get_val(modes, 3, True)
                self.code[idx] = int(self.get_val(modes, 1) == self.get_val(modes, 2))
                self.pointer += 4
            elif op == 9:
                self.relative_base += self.get_val(modes, 1)
                self.pointer += 2
            else:
                raise ValueError(f"Unknown instruction {op} for bot {self.name}")

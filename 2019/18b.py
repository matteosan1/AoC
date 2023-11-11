from utils import readInput
from queue import Queue
from threading import Thread

lines = readInput("input_18.txt")

def program(q_out, q_in, p):
    n = p
    registry = {'p':p}

    def readParam(p):
        try:
            val = int(p)
        except:
            val = registry.get(p)

        return val

    line = 0
    sent = 0
    while 0 <= line < len(lines):
        parts = lines[line].split()
        cmd = parts[0]
        params = parts[1:]

        if cmd == "snd":
            q_out.put(readParam(params[0]))
            sent += 1
        elif cmd == "set":
            registry[params[0]] = readParam(params[1])
        elif cmd == "add":
            registry[params[0]] = registry.setdefault(params[0], 0) + readParam(params[1])
        elif cmd == "mul":
            registry[params[0]] = registry.setdefault(params[0], 0) * readParam(params[1])
        elif cmd == "mod":
            registry[params[0]] = registry.setdefault(params[0], 0) % readParam(params[1])        
        elif cmd == "rcv":
            try:
                val = q_in.get(True, 2)
            except:
                break
            registry[params[0]] = val            
        elif cmd == "jgz":
            if readParam(params[0]) > 0:
                line += readParam(params[1])
                continue
    
        line += 1
    print ("🎁🎄Part 2: p{} - sent:{}".format(n, sent))

q0 = Queue()
q1 = Queue()

t1 = Thread(target=program, args=(q0, q1, 0))
t2 = Thread(target=program, args=(q1, q0, 1))

t1.start()
t2.start()

t1.join()
t2.join()

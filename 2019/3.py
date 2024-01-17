import time

from utils import readInput
            
def loadInput():
    lines = readInput("input_3.txt")
    #lines = readInput("prova.txt")
    wires = [[],[]]
    wires[0] = lines[0].split(",")
    wires[1] = lines[1].split(",")
    return wires

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

def part1(wires):
    pos = complex(0, 0)
    paths = []
    for i in range(2):
        pos = complex(0, 0)
        path = [pos]
        for p in wires[i]:
            val = int(p[1:])
            if p.startswith("R"):
                pos += val
            elif p.startswith("L"):
                pos -= val
            elif p.startswith("U"):
                pos -= val*complex(0, 1)
            elif p.startswith("D"):
                pos += val*complex(0, 1)
            path.append(pos)
        paths.append(path)
    print (paths[0])
    crossings = []
    for ip in range(len(paths[0])):
        if ip == len(paths[0])-1:
            s1 = (paths[0][-1], paths[0][0])
        else:
            s1 = (paths[0][ip], paths[0][ip+1])
        for ip2 in range(len(paths[1])):
            if ip2 == len(paths[1])-1:
                s2 = (paths[1][-1], paths[1][0])
            else:
                s2 = (paths[1][ip2], paths[1][ip2+1])
            #if s1[0].real == s1[1].real and s2[0].real == s2[1].real:
            #    continue
            #elif s1[0].imag == s1[1].imag and s2[0].imag == s2[1].imag:
            #    continue
            if s1[0].real == s1[1].real:
                if s2[0].real <= s2[1].real and s2[0].real <= s1[0].real <= s2[1].real:
                    crossings.append(complex(s1[0].real, s2[0].imag))
                    print ("1", crossings[-1])
                elif s2[1].real <= s2[0].real and s2[1].real <= s1[0].real <= s2[0].real:
                    crossings.append(complex(s1[0].real, s2[0].imag))
                    print ("2", crossings[-1])
            if s2[0].real == s2[1].real:
                if s1[0].real <= s1[1].real and s1[0].real <= s2[0].real <= s1[1].real:
                    crossings.append(complex(s2[0].real, s1[0].imag))
                    print ("3", crossings[-1])
            #    elif s1[1].real < s1[0].real and s1[1].real <= s2[0].real <= s1[0].real:
            #        crossings.append(complex(s2[0].real, s1[0].imag))
            #        print ("4", crossings[-1])
            #elif s2[0].imag < s2[1].imag and s2[0].imag <= s1[0].imag <= s2[1].imag:
            #    crossings.append(complex(s2[0].real, s1[0].imag))
            #    print ("3", crossings[-1])
            #elif s2[1].imag < s2[0].imag and s2[1].imag <= s1[0].imag <= s2[0].imag:
            #    crossings.append(complex(s2[0].real, s1[0].imag))

    #print (crossings)
    dist = min([abs(c.real)+abs(c.imag) for c in crossings])
    print (f"🎅 Part 1: {dist}")

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
    title = "Day 3: Crossed Wires"
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


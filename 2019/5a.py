with open("input5a.txt") as f:
    line = f.readline()
    
#line = "1101,100,-1,4,0"
#line = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"

intcode = list(map(int, line.split(",")))
index = 0
while index < len(intcode):
    optcode = intcode[index] % 100
    modes = [int(d) for d in str(intcode[index] // 100)[::-1]]
    if len(modes) == 1:
        modes.append(0)
    val = []
    if optcode == 99:
        break
    elif optcode == 1:
        for im in range(2):
            if modes[im] == 0:
                val.append(intcode[intcode[index + 1 + im]])
            else:
                val.append(intcode[index + 1 + im])
        intcode[intcode[index + 3]] = val[0] + val[1]
        index += 4
    elif optcode == 2:
        for im in range(2):
            if modes[im] == 0:
                val.append(intcode[intcode[index + 1 + im]])
            else:
                val.append(intcode[index + 1 + im])
        intcode[intcode[index + 3]] = val[0] * val[1]
        index += 4
    elif optcode == 3:
        intcode[intcode[index + 1]] = int(input('Input: '))
        index += 2
    elif optcode == 4:
        if modes[0] == 0:
            val.append(intcode[intcode[index + 1]])
        else:
            val.append(intcode[index + 1])
        print ("output {}".format(val[0]))
        index += 2
    elif optcode == 5:
        for im in range(2):
            if modes[im] == 0:
                val.append(intcode[intcode[index + 1 + im]])
            else:
                val.append(intcode[index + 1 + im])
        if val[0] != 0:
            index = val[1]
        else:
            index += 3
    elif optcode == 6:
        for im in range(2):
            if modes[im] == 0:
                val.append(intcode[intcode[index + 1 + im]])
            else:
                val.append(intcode[index + 1 + im])
        if val[0] == 0:
            index = val[1]
        else:
            index += 3
    elif optcode == 7:
        for im in range(2):
            if modes[im] == 0:
                val.append(intcode[intcode[index + 1 + im]])
            else:
                val.append(intcode[index + 1 + im])
        if val[0] < val[1]:
            intcode[intcode[index + 3]] = 1
        else:
            intcode[intcode[index + 3]] = 0
        index += 4
    elif optcode == 8:
        for im in range(2):
            if modes[im] == 0:
                val.append(intcode[intcode[index + 1 + im]])
            else:
                val.append(intcode[index + 1 + im])
        if val[0] == val[1]:
            intcode[intcode[index + 3]] = 1
        else:
            intcode[intcode[index + 3]] = 0
        index += 4

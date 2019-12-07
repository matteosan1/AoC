import itertools

with open("input7a.txt") as f:
    code = f.readline()

#code = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
#code = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"

def computer(code, inputs):
    input_counter = 0
    outputs = []
    intcode = list(map(int, code.split(",")))
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
            if inputs is []:
                intcode[intcode[index + 1]] = int(input('Input: '))
            else:
                #print ("going to use input {}:{}".format(input_counter, inputs[input_counter]))
                intcode[intcode[index + 1]] = inputs[input_counter]
                input_counter += 1
            index += 2
        elif optcode == 4:
            if modes[0] == 0:
                val.append(intcode[intcode[index + 1]])
            else:
                val.append(intcode[index + 1])
            #print ("output {}".format(val[0]))
            outputs.append(val[0])
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

    return outputs

phases = [0, 1, 2, 3, 4]
max_out = 0
seq = 0

for p in list(itertools.permutations(phases, len(phases))):
    inputs = [p[0], 0]
    out = computer(code, inputs)[-1]
    inputs = [p[1], out]
    out = computer(code, inputs)[-1]
    inputs = [p[2], out]
    out = computer(code, inputs)[-1]
    inputs = [p[3], out]
    out = computer(code, inputs)[-1]
    inputs = [p[4], out]
    out = computer(code, inputs)[-1]
    if out > max_out:
        max_out = out
        seq = p

print (max_out, seq)
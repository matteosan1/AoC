with open("input2a.txt") as f:
    line = f.readline()

memory = list(map(int, line.split(",")))

for p1 in range(0, 100):
    for p2 in range(0, 100):
        memory[1] = p1
        memory[2] = p2
        intcode = list(memory)
        for index in range(0, len(intcode), 4):
            if intcode[index] == 99:
                break
            elif intcode[index] == 1:
                intcode[intcode[index + 3]] = intcode[intcode[index + 1]] + intcode[intcode[index + 2]]
            elif intcode[index] == 2:
                intcode[intcode[index + 3]] = intcode[intcode[index + 1]] * intcode[intcode[index + 2]]

        if intcode[0] == 19690720:
            print (p1, p2)
            print (p1*100 + p2)
            import sys
            sys.exit()
    

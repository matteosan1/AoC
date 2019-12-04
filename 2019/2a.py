with open("input2a.txt") as f:
    line = f.readline()
    
#1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
#2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
#line = "2,4,4,5,99,0" # becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
#line = "1,1,1,4,99,5,6,0,99"
#line = "1,9,10,3,2,3,11,0,99,30,40,50"


intcode = list(map(int, line.split(",")))
intcode[1] = 12
intcode[2] = 2
print (intcode)

for index in range(0, len(intcode), 4):
    if intcode[index] == 99:
        break
    elif intcode[index] == 1:
        intcode[intcode[index + 3]] = intcode[intcode[index + 1]] + intcode[intcode[index + 2]]
    elif intcode[index] == 2:
        print ("1")
        intcode[intcode[index + 3]] = intcode[intcode[index + 1]] * intcode[intcode[index + 2]]
    
print (intcode)

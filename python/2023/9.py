import time
from utils import readInput

def loadInput():
    lines = readInput("input_9.txt")
    inputs = []
    for l in lines:
        inputs.append(list(map(int, l.split())))
    return inputs

def subtraction(l):
    new_l = []
    for i in range(len(l)-1):
        new_l.append(l[i+1]-l[i])
    return new_l
    
def part1(inputs):
    predictions = []
    for input in inputs:
        new_inputs = [input]
        while True:
            new_inputs.append(subtraction(new_inputs[-1]))
            if all([v==0 for v in new_inputs[-1]]):
                break
        new_inputs[-1].append(0)
        for i in reversed(range(len(new_inputs)-1)):
            new_inputs[i].append(new_inputs[i+1][-1] + new_inputs[i][-1])

        predictions.append(new_inputs[0][-1])
    print (f"🎄 Part 1: {sum(predictions)}")

def part2(inputs):
    predictions = []
    for input in inputs:
        new_inputs = [input]
        while True:
            new_inputs.append(subtraction(new_inputs[-1]))
            if all([v==0 for v in new_inputs[-1]]):
                break
        new_inputs[-1].insert(0, 0)
        for i in reversed(range(len(new_inputs)-1)):
            new_inputs[i].insert(0, (new_inputs[i][0] - new_inputs[i+1][0]))

        predictions.append(new_inputs[0][0])
    print (f"🎄🎅 Part 2: {sum(predictions)}")

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 9         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print (f"Time: {time.time()-t0:.5f}")

t0 = time.time()
part2(inputs)
print (f"Time: {time.time()-t0:.5f}")

import time
from utils import readInputWithBlank

def loadInput():
    lines = readInputWithBlank("input_6.txt")
    answers = []
    temp = []
    for l in lines:
        if l == "":
            answers.append(temp)
            temp = []
        else:
            temp.append(l)

    return answers

def part1(answers):
    counts = 0
    for a in answers:
        temp = []
        for i in a:
            temp += list(i)
        counts += len(set(temp))
    print ("🎄 Part 1: {}".format(counts))

def part2(answers):
    counts = [len(set.intersection(*list(map(set, a)))) for a in answers]
    count = sum(counts)
    print ("🎄🎅 Part 2: {}".format(count))

print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 6         ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()

t0 = time.time()
part1(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(inputs)
print ("Time: {:.5f}".format(time.time()-t0))

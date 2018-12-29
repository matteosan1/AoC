from collections import deque, defaultdict

nplayers = 418
nmarble = 7076900

scores = defaultdict(int)
circle = deque([0])
for i in range(1, nmarble+1):
    if i % 23 == 0:
        circle.rotate(7)
        scores[i%nplayers] += i + circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(i)

print (max(scores.values()))

input = 36000000

house = [0] * (input//11)
for i in range (1, input//11):
    delivery = 0
    for j in range(i, input//11, i):
        house[j] += i
        delivery += 1
        if delivery >= 50:
            break
for i, h in enumerate(house):
    if h > input//11:
        print (i, h)
        break

# def divisori(n):
#     return [c for c in range(1, int(n/2)+1) if n % c == 0]+[n]

input = 36000000

# n = 0
# n_reg = 0
# while n_reg < input:
#     l = divisori(n)
#     n_reg = sum(l)
#     if n % 1000 == 0:
#         print (n, n_reg)
#     n += 1
#
# print (n_reg, max(l))
house = [0] * (input//10)
for i in range (1, input//10):
    for j in range(i, input//10, i):
        house[j] += i

for i, h in enumerate(house):
    if h > input//10:
        print (i, h)
        break

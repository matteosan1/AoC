def generator(n):
    for i in range(n):
        yield i


a = generator(10)
while True:
    try:
        p = next(a)
    except StopIteration:
        break

print (p)

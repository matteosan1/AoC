import time

t1 = time.perf_counter()
for i in range(1, 13):
    my_module = __import__(f"{i}")
    my_module.main()

print (f"Total runtime: {time.perf_counter()-t1}")
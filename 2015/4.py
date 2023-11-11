from concurrent.futures import ProcessPoolExecutor, ALL_COMPLETED, wait
import hashlib

def task(key, hash_begin, range):
    for i in range:
        r = hashlib.md5(key + str(i).encode())
        hexa = r.hexdigest()
        if hexa[:len(hash_begin)] == hash_begin:
            print (i, hexa)

def pooler(key, hash_begin, nmax):
    threads = 6
    executor = ProcessPoolExecutor(threads)
    
    stuffed_futures = []
    for thread in range(threads):
        r = range(1 + thread, 10**nmax + thread, threads)
        f = executor.submit(task, key, hash_begin, r)

        stuffed_futures.append(f)
    wait(stuffed_futures, return_when=ALL_COMPLETED)

key = b"ckczppom"
#key = b"abcdef"

pooler(key, "000000", 7)

    


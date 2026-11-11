from multiprocessing import Process, Pipe

def run(q, seed, gen, divisor):
    import time
    tstart = time.time()
    num = (num * gen) % divisor
    
    for i in range(40000000):
        num = generate(num, gen, divisor)
        q.send(num)
    
    print (time.time()-tstart)


#def worker(q):
#    output_p, input_p = q
#    input_p.close()
#    for task_nbr in range(100000):
#        message = output_p.recv()
#    sys.exit(1)
#
#def main():
#    output_p, input_p = Pipe()
#    Process(target=worker, args=((output_p,input_p),)).start()
#    b = [i for i in range(20)]
#    start_time = time.time()
#    for num in range(100000):
#        input_p.send(b)
#    end_time = time.time()
#
#    duration = end_time - start_time
#    msg_per_sec = 100000 / duration
#
#    print "Duration: %s" % duration
#    print "Messages Per Second: %s" % msg_per_sec

def judge(qa, qb):
    matches = 0
    c = 0
    while True:
        na = qa.recv()
        nb = qb.recv()
        
        if bin(na)[-16:] == bin(nb)[-16:]:
            c += 0
            matches += 1
        if c == 40000000:
            print (matches)
            break
        

if __name__ == '__main__':    
    seed_a = 65#703
    seed_b = 8921#516

    gen_a = 16807
    gen_b = 48271
    divisor = 2147483647

    out_pa, in_pa = Pipe()
    out_pb, in_pb = Pipe()

    t1 = Process(target=run, args=(in_pa, seed_a, gen_a, divisor)).start()
    t2 = Process(target=run, args=(in_pb, seed_b, gen_b, divisor)).start()    
    j = Process(target=judge, args=(out_pa, out_pb)).start()
    

using Base.Threads: @spawn

function generator(num::Int64, gen::Int64, divisor::Int64)
    num = (num * gen) % divisor
    return num 
end

function generator2(num::Int64, gen::Int64, divisor::Int64, mod::Int64)
    while true 
        num = (num * gen) % divisor
        if num % mod == 0
            break
        end
    end
    return num 
end 

function judge(part::Int, n::Int)
    #println(Threads.threadid())
    t = time()
    matches = 0
    na = 703
    nb = 516
    for i in 1:n
        if part == 1
            na = generator(na, 16807, 2147483647)
            nb = generator(nb, 48271, 2147483647)
        else
            na = generator2(na, 16807, 2147483647, 4)
            nb = generator2(nb, 48271, 2147483647, 8)
        end
        
        if (na & 0xFFFF) == (nb & 0xFFFF)
            matches += 1
        end
    end
    println(matches)
    println(time()-t)
end

@sync begin
    @spawn judge(2, 5000000)
    @spawn judge(1, 40000000)
end

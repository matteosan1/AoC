include("utils.jl")
using .AoCUtils


function compute(captcha)
    s = 0
    i = 1

    l = length(captcha)
    while i <= l
        next = (i+1) % l == 0 ? l : (i+1) % l 
        if captcha[i] == captcha[next]
            s += parse(Int, captcha[i])
        end
        i += 1
    end

    println("🎄 $(s)")
end

function compute_v2(captcha)
    s = 0
    i = 1
    l = length(captcha)
    while i <= l
        mod = (i+l÷2) % l
        next = mod == 0 ? l : mod 
        if captcha[i] == captcha[next]
            s += parse(Int, captcha[i])
        end
        i += 1
    end
    println("🎁🎄 $(s)")
end

captcha = AoCUtils.readLines("input_1.txt")[1]
compute(captcha)
compute_v2(captcha)
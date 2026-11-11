include("utils.jl")
using .AoCUtils

#(6x9)JUO
function parser(msg)
    idx::Int = 1
    dec_msg = ""
    while idx < length(msg)
        if msg[idx] == '('
            idx += 1
            close = findnext(isequal(')'), msg, idx)
            decompression = split(msg[idx:close-1], "x")
            idx = close+1
            l::Int = parse(Int, decompression[1])
            times::Int = parse(Int, decompression[2])
            for i in 1:times
                dec_msg *= msg[idx:idx+l]
            end
            idx += l
        else
            dec_msg *= msg[idx]
            idx += 1
        end
    end
    return dec_msg
end

lines = readLines("input_9.txt")
println(parser(lines[1]))
#print ("🎄Part 1: {}".format(len(p.parse())))
#    println("🎄Part 2: $digits")

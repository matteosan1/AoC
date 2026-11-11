include("utils.jl")
using .AoCUtils

function decode(lines, part=1)
    decoded = ""
    for i in 1:8
        counts = Dict{Char, Int}()
        for l in lines
            if haskey(counts, l[i])
                counts[l[i]] += 1
            else
                counts[l[i]] = 1
            end
        end
        if part == 1
            decoded *= findmax(counts)[2]
        else
            decoded *= findmin(counts)[2]
        end
    end     

    println("❄ $decoded")
end

lines = readLines("input_6.txt")
decode(lines)
decode(lines, 2)
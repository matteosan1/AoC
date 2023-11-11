include("utils.jl")
using .AoCUtils

using Combinatorics

function checksum(lines)
    chk = 0
    for l in lines
        parts = parse.(Int, split(l))
        chk += maximum(parts) -  minimum(parts)
    end
    
    println("🎄 $(chk)")
end

function checksum_v2(lines)
    chk = 0
    for l in lines
        parts = parse.(Int, split(l)) 
        for c in permutations(parts, 2)
            if c[2]%c[1] == 0
                chk += c[2]÷c[1]
                break
            end
        end
    end
    println("🎅 $(chk)")
end

lines = AoCUtils.readLines("input_2.txt")
checksum(lines)
checksum_v2(lines)
include("utils.jl")
using .AoCUtils: readInput

function part1()
    lines = readInput("input_1.txt")
    freqs = parse.(Int, lines)
    println("🎅 Part 1: $(sum(freqs))")
end

function part2()
    lines = readInput("input_1.txt")
    freqs = cumsum(parse.(Int, lines))

    for i in eachindex(freqs)
        if freqs[i] in freqs[1:i-1]
            println("🎄🎅 Part 2: $(freqs[i])")
            break
        end
    end
end

part1()
part2()

include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "prova.txt"
    #filename = "input_12.txt"
    lines = readInput(filename)

    return
end

function part1(inputs)
    
    #println("🎄 Part 1: $()")
end

function part2(inputs)

    #println("🎄🎅 Part 2: $()")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 12         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
@time part1(inputs)
@time part2(inputs)

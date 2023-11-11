include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "input_10.txt"
    lines = readInput(filename)
    adapters = parse.(Int, lines)
    push!(adapters, 0)
    push!(adapters, maximum(adapters) + 3)
    sort!(adapters)
    return adapters
end

function part1(adapters::Vector{Int})
    differences = Dict{Int, Int}(1=>0, 2=>0, 3=>0)
    for i in 2:length(adapters)
        differences[adapters[i] - adapters[i-1]] += 1
    end 
    println("🎄 Part 1: $(differences[1]*differences[3])")
end

function part2(adapters::Vector{Int})
    comb = Dict(0=>1, 1=>1, 2=>2, 3=>4, 4=>7)
    jolts = Int[]
    for i in 2:length(adapters)
        push!(jolts, adapters[i] - adapters[i-1])
    end 

    cons = Int[]
    c = 0
    for (i, j) in enumerate(jolts)
        if  j == 1
            c += 1
        else
            push!(cons, c)
            c = 0
        end
    end 

    tot = prod([comb[c] for c in cons])
    println("🎄🎅 Part 2: $(tot)")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 10        ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
@time part1(inputs)
@time part2(inputs)

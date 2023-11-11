include("utils.jl")
using .AoCUtils: readInput
using Combinatorics

function loadInput()
    filename = "input_9.txt"
    lines = readInput(filename)
    numbers = parse.(Int, lines)
    return numbers
end

function XMAS(coding::Vector{Int}, n::Int)
    for c in combinations(coding, 2)
        if sum(c) == n
            return true
        end
    end
    return false
end

function part1(numbers::Vector{Int}, preamble::Int)
    for idx in preamble+1:length(numbers)
        if !XMAS(numbers[idx-preamble:idx-1], numbers[idx])
            println("🎄 Part 1: $(numbers[idx])")
            return numbers[idx]
        end
    end
end

function part2(numbers::Vector{Int}, target::Int)
    start = 1
    stop = 2
    sums = sum(numbers[start:stop])
    while sums != target
        if sums < target
            stop += 1
        elseif sums > target
            start += 1
        end
        sums = sum(numbers[start:stop])
    end
    res = minimum(numbers[start:stop]) + maximum(numbers[start:stop])
    println("🎄🎅 Part 2: $(res)")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 9         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
@time target = part1(inputs, 25)
@time part2(inputs, target)

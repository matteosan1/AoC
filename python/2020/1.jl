include("utils.jl")
using .AoCUtils: readInput
using Combinatorics

function loadInput()
    filename = "input_1.txt"
    lines = readInput(filename)
    expenses = parse.(Int, lines)

    return expenses
end

function part1(expenses::Vector{Int})
    for c in combinations(expenses, 2)
        if sum(c) == 2020
            println("🎄 Part 1: $(prod(c))")
            break
        end
    end
end

function part2(expenses::Vector{Int})
    for c in combinations(expenses, 3)
        if sum(c) == 2020
            println("🎄🎅 Part 2: $(prod(c))")
            break
        end
    end
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 1         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

expenses = loadInput()
@time part1(expenses)
@time part2(expenses)

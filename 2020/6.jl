include("utils.jl")
using .AoCUtils: readInputWithBlank

function loadInput()
    filename = "input_6.txt"
    lines = readInputWithBlank(filename)
    answers = Vector{Vector{String}}()
    temp = String[]
    for l in lines
        if l == ""
            push!(answers, temp)
            temp = String[]
        else
            push!(temp, l)
        end
    end
    push!(answers, temp)
    
    return answers
end

function part1(answers::Vector{Vector{String}})
    counts = 0
    for g in answers
        counts += length(Set([item for a in g for item in collect(a)]))
    end
    println("🎄 Part 1: $(counts)")
end

function part2(answers::Vector{Vector{String}})
    counts = 0
    for g in answers
        counts += length(reduce(intersect, g))
    end
    println("🎄🎅 Part 2: $(counts)")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 6         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
@time part1(inputs)
@time part2(inputs)

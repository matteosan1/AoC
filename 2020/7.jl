include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "input_7.txt"
    lines = readInput(filename)
    bags = Dict{String, Vector{Tuple{Int64, String}}}()
    regexp = r"(\d+)\s(\w+\s\w+)\s[bag,bags]"
    for l in lines
        k = join(split(l)[1:2], " ")
        bags[k] = []
        for m in eachmatch(regexp, l)
            push!(bags[k], (parse(Int, m[1]), m[2]))
        end
    end

    return bags
end

function findbag(bags::Dict{String, Vector{Tuple{Int64, String}}}, current::String, target::String)
    found = false
    for b in bags[current]
        if b[2] == target
            found = true
            break
        else
            found = findbag(bags, b[2], target)
            if found
                break
            end
        end
    end

    return found
end

function countbags(bags::Dict{String, Vector{Tuple{Int64, String}}}, current::String)
    n = 0
    for b in bags[current]
        n += b[1] + b[1]*countbags(bags, b[2])
    end
    return n
end

function part1(bags::Dict{String, Vector{Tuple{Int64, String}}})
    mybag = "shiny gold"
    contains = 0
    for k in keys(bags)
        if k == mybag
            continue
        end
        if findbag(bags, k, mybag)
            contains += 1
        end
    end
    println("🎄 Part 1: $(contains)")
end

function part2(bags::Dict{String, Vector{Tuple{Int64, String}}})
    println("🎄🎅 Part 2: $(countbags(bags, "shiny gold"))")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 7         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
@time part1(inputs)
@time part2(inputs)

include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "input_2.txt"
    lines = readInput(filename)
    pwds = String[split(l, ": ")[2] for l in lines]
    policies = Vector{Tuple{String, Vector{Int}}}()
    for l in lines
        c = split(split(l, ": ")[1])[2]
        counts = parse.(Int, split(split(split(l, ": ")[1])[1], "-"))
        push!(policies, (c, counts))
    end
    return policies, pwds
end

function part1(pols::Vector{Tuple{String, Vector{Int}}}, pwds::Vector{String})
    valid = 0
    for (ip, p) in enumerate(pwds)
        occurrencies = count(x->x==first(pols[ip][1]), p)
        if pols[ip][2][1] <= occurrencies <= pols[ip][2][2]
            valid += 1
        end
    end
    println("🎄 Part 1: $(valid)")
end

function part2(pols::Vector{Tuple{String, Vector{Int}}}, pwds::Vector{String})
    valid = 0
    for (ip, p) in enumerate(pwds)
        if (p[pols[ip][2][1]] == first(pols[ip][1]) && p[pols[ip][2][2]] != first(pols[ip][1])) ||
            (p[pols[ip][2][1]] != first(pols[ip][1]) && p[pols[ip][2][2]] == first(pols[ip][1]))
            valid += 1
        end
    end

    println("🎄🎅 Part 2: $(valid)")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 2         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

pols, pwds = loadInput()
@time part1(pols, pwds)
@time part2(pols, pwds)

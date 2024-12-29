using StatsBase

function loadInput(filename::String)
    lines = readlines(filename)
    ids = [Tuple(parse.(Int64, split(l))) for l in lines]
    return first.(ids), last.(ids) 
end

function part1(id1::Vector{Int64}, id2::Vector{Int64})
    println("🎄 Part 1: $(sum(abs.(x - y) for (x, y) in zip(sort(id1), sort(id2))))")
end

function part2(id1::Vector{Int64}, id2::Vector{Int64})
    tot = 0
    counts = countmap(id2)
    for n in id1
        tot += n * get(counts, n, 0)
    end
    println("🎄🎅 Part 2: $tot")
end

function main()
    title = "Day 1: Historian Hysteria"
    sub = "❄ " ^(length(title) ÷ 2 + 2)

    println()
    println(" $title ")
    println(sub)

    inputs = loadInput("input_1.txt")

    @time part1(inputs...)
    @time part2(inputs...)
end

main()

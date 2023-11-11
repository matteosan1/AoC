include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "input_3.txt"
    lines = readInput(filename)
    pattern = Dict{Tuple{Int, Int}, Int}() 
    for y in eachindex(lines)
        for x in 1:length(lines[1])
            if lines[y][x] == '#'
                pattern[(x-1, y-1)] = 1
            end
        end
    end
    return length(lines[1]), length(lines), pattern
end

function traverse(dx::Int, dy::Int, xmax::Int, ymax::Int, pattern::Dict{Tuple{Int, Int}, Int})
    y = 0
    x = 0
    trees = 0
    while true
        y += dy
        if y >= ymax
            break
        end
        x += dx
        x %= xmax
        if haskey(pattern, (x, y))
            trees += 1
        end
    end
    return trees
end

function part1(xmax::Int, ymax::Int, pattern::Dict{Tuple{Int, Int}, Int})
    trees = traverse(3, 1, xmax, ymax, pattern)
    println("🎄 Part 1: $(trees)")
end

function part2(xmax::Int, ymax::Int, pattern::Dict{Tuple{Int, Int}, Int})
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = Int[]
    for s in slopes
        push!(trees, traverse(s..., xmax, ymax, pattern))
    end
    println("🎄🎅 Part 2: $(prod(trees))")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 3         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

xmax, ymax, inputs = loadInput()
@time part1(xmax, ymax, inputs)
@time part2(xmax, ymax, inputs)

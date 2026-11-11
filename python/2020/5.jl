include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "prova.txt"
    filename = "input_5.txt"
    passes::Vector{String} = readInput(filename)

    return passes
end

function decode(bp::String, bins::Int=8)
    row = [0, 2^bins-1]
    for i in 1:bins-1
        if bp[i] == 'F' || bp[i] == 'L'
            row[2] = 2^*(bins-i) * 0.5-1 + row[1]
        elseif bp[i] == 'B' || bp[i] == 'R'
            row[1] = 2^*(bins-i) * 0.5 + row[1]
        end
        #println(row)
    end
    return row[1]
end

function part1(passes::Vector{String})
    ids = Vector{Int}()
    for bp in passes
        row = decode(bp[1:7])
        seat = decode(bp[8:end], 4)
        id = row*8 + seat
        push!(ids, id)
    end
    println("🎄 Part 1: $(maximum(ids))")
    return ids
end

function part2(ids::Vector{Int})
    sort!(ids)
    r = minimum(ids):maximum(ids)
    miss = setdiff(Set(r), Set(ids))
    println("🎄🎅 Part 2: $(pop!(miss))")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 5         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
@time ids = part1(inputs)
@time part2(ids)

include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    start = [16, 11, 15, 0, 1, 7]
    spoken = Dict{Int, Int}()
    for (i, v) in enumerate(start)
        spoken[v] = i
    end
    last = start[end]
    return spoken, last
end

function play(spoken::Dict{Int, Int}, last_spoken::Int, turns::Int)
    turn = length(spoken)
    while turn < turns
        if !haskey(spoken, last_spoken)
            spoken[last_spoken] = turn
            last_spoken = 0
        else
            spoken[last_spoken], last_spoken = turn, turn - spoken[last_spoken]
        end
        turn += 1
    end
    last_spoken
end

function part1(spoken::Dict{Int, Int}, last::Int)
    println("🎄 Part 1: $(play(spoken, last, 2020))")
end

function part2(spoken::Dict{Int, Int}, last::Int)
    println("🎄🎅 Part 2: $(play(spoken, last, 30000000))")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 15        ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

spoken, last = loadInput()
@time part1(spoken, last)
spoken, last = loadInput()
@time part2(spoken, last)

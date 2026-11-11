include("utils.jl")
using .AoCUtils

function readPos()
    timers = AoCUtils.readInput("input_7.txt")
    return parse.(Int, split(timers[1], ",")) 
end

function part1(pos)
    deltas = [sum([abs(p-i) for p in pos]) for i in minimum(pos):maximum(pos)]
    println("🎄 Part 1: $(minimum(deltas))")
end

function part2(pos)
    deltas = [sum([sum(1:abs(p-i)) for p in pos]) for i in minimum(pos):maximum(pos)]
    println("🎄🎅 Part 2: $(minimum(deltas))")
end

pos = readPos()
part1(pos)
part2(pos)
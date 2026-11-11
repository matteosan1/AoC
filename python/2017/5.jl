include("utils.jl")
using .AoCUtils

function jumps(lines)
    instructions = parse.(Int, lines)
    steps = 0
    line = 1
    while 1 <= line <= length(instructions)
        delta = instructions[line]
        instructions[line] += 1
        line += delta
        steps += 1
    end

    println("🎄 $steps")
end

function jumps_v2(lines)
    instructions = parse.(Int, lines)
    steps = 0
    line = 1
    while 1 <= line <= length(instructions)
        delta = instructions[line]
        if delta >= 3
            instructions[line] -= 1
        else
            instructions[line] += 1
        end
        line += delta
        steps += 1
    end

    println("🎄🎅 $steps")
end

lines = AoCUtils.readLines("input_5.txt")
jumps(lines)
jumps_v2(lines)
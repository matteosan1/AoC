include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "prova.txt"
    filename = "input_8.txt"
    lines = readInput(filename)
    program = Vector{Vector{Union{String, SubString, Int}}}()
    for l in lines
        l = split(l)
        push!(program, [l[1], parse(Int, l[2])])
    end
    return program
end

function run(program::Vector{Vector{Union{String, SubString, Int}}})
    executed_lines = Int[]
    acc = 0
    idx = 1
    inf_loop = false
    while idx <= length(program)
        if idx in executed_lines
            inf_loop = true
            break
        else
            push!(executed_lines, idx)
        end

        line = program[idx]
        if line[1] == "nop"
            idx += 1
        elseif line[1] == "acc"
            acc += line[2]
            idx += 1
        elseif line[1] == "jmp"
            idx += line[2]
        end
    end
    return acc, inf_loop
end

function part1(program::Vector{Vector{Union{String, SubString, Int}}})
    acc, inf_loop = run(program)
    println("🎄 Part 1: $(acc)")
end

function modify_line(line::SubString{String})
    if line == "nop"
        return "jmp"
    else
        return "nop"
    end
end

function part2(program::Vector{Vector{Union{String, SubString, Int}}})
    idxs = findall(x->x[1] == "nop" || x[1] == "jmp", program)
    new_program = deepcopy(program)
    for idx in idxs
        new_program[idx][1] = modify_line(new_program[idx][1])
        acc, loop = run(new_program)
        if !loop
            println("🎄🎅 Part 2: $(acc)")
            break
        end
        new_program[idx][1] = modify_line(new_program[idx][1])
    end     
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 8         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
@time part1(inputs)
@time part2(inputs)

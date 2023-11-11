mutable struct CFlow
    program::Vector{String}
    register::Dict
    line::Int
end

function readInput()
    file = f = open("instructions23a.txt", "r")
    lines = readlines(f)

    return lines
end

function run_program(flow::CFlow)
    while flow.line <= length(flow.program)
        prefix = flow.program[flow.line][1:3]
        args = split(flow.program[flow.line][5:end], ", ")
        if prefix == "hlf"
            flow.register[args[1]] /= 2
            flow.line += 1
        elseif prefix == "tpl"
            flow.register[args[1]] *= 3
            flow.line += 1
        elseif prefix == "inc"
            flow.register[args[1]] += 1
            flow.line += 1
        elseif prefix == "jmp"
            flow.line += parse(Int, args[1])
        elseif prefix == "jie"
            if flow.register[args[1]] % 2 == 0
                flow.line += parse(Int, args[2])
            else
                flow.line += 1
            end
        elseif prefix == "jio"
            if flow.register[args[1]] == 1
                flow.line += parse(Int, args[2])
            else
                flow.line += 1
            end
        else
            println("wrong command $prefix")
            return
        end
    end
    println("🎅 $(flow.register["b"])")
end

program = readInput()
flow = CFlow(program, Dict("a"=>0, "b"=>0), 1)
run_program(flow)

flow = CFlow(program, Dict("a"=>1, "b"=>0), 1)
run_program(flow)


mutable struct Machine
    buttonA::Int
    buttonB::Int
    button::Matrix{Int}
    prize::Vector{Int}
end

function solve(m::Machine)
    a = round((m.prize[2]-((m.button[2,2]*m.prize[1])/m.button[2,1]))/(m.button[1,2]-((m.button[2,2]*m.button[1,1])/m.button[2,1])))
    b = round((m.prize[1]-m.button[1,1]*a)/m.button[2,1])
    if m.button[1,1]*a+m.button[2,1]*b == m.prize[1] && m.button[1,2]*a+m.button[2,2]*b == m.prize[2]
        return (a, b)
    else
        return nothing
    end
end

function cost(m::Machine)
    pushes = solve(m)
    if pushes === nothing
        return 0
    else
        return pushes[1]*3 + pushes[2]*1
    end
end

function toString(m::Machine)
    "A: $(m.buttonA), B: $(m.buttonB), prize: $(m.prize)"
end

function loadInput(filename::String)
    lines = readlines(filename)
    machines = []
    for i in 1:4:length(lines)
        machine = Machine(0, 0, zeros(2,2), [0,0])
        machine.button[1, :] = parse.(Int, map(x -> x[2], split.(split(lines[i], ","), "+")))
        machine.button[2, :] = parse.(Int, map(x -> x[2], split.(split(lines[i+1], ","), "+")))
        machine.prize = parse.(Int, map(x -> x[2], split.(split(lines[i+2], ","), "=")))
        push!(machines, machine)
    end
    machines
end
      
function part1(machines)
    tot_cost = 0
    for m in machines
        tot_cost += cost(m)
    end
    println("🎄 Part 1:  $(tot_cost)")
end

function part2(machines)
    constant = 10000000000000
    tot_cost = 0
    for m in machines
        m.prize = [m.prize[1] + constant, m.prize[2] + constant]
        tot_cost += cost(m)
    end
    println("🎄🎅 Part 2: $(tot_cost)")
end

function main()
    title = "Day 13: Claw Contraption"
    sub = "❄ "^(length(title)÷2 + 2)
    
    println()
    println(" $title ")
    println(sub)
    
    inputs = loadInput("input_13.txt")
    @time part1(inputs)
    @time part2(inputs)
end

main()
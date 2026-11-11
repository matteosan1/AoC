include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "prova.txt"
    filename = "input_12.txt"
    lines = readInput(filename)
    instructions = Vector{Tuple{Union{Char, Int}, Int}}()
    mapping = Dict('N'=>0, 'E'=>1, 'S'=>2, 'W'=>3)

    for l in lines
        if l[1] == 'R' || l[1] == 'L' || l[1] == 'F'
            push!(instructions, (l[1], parse(Int, l[2:end])))
        else
            push!(instructions, (mapping[l[1]], parse(Int, l[2:end])))
        end
    end
    return instructions
end

function manhattan_distance(x::Complex{Int}, y::Complex{Int})
    return Int(sum(abs(real(x-y)) + abs(imag(x-y))))
end

function part1(instructions::Vector{Tuple{Union{Char, Int}, Int}})
    dirs = Complex[-1im, 1, 1im, -1]
    pos = Complex(0, 0)
    dir = 1
    for i in instructions
        if i[1] == 'L'
            dir -= i[2]÷90 
            dir = dir%4 >= 0 ? dir%4 : 4 + (dir%4)
        elseif i[1] == 'R'
            dir += i[2]÷90 
            dir = dir%4
        elseif i[1] == 'F'
            pos += i[2]*dirs[dir+1]
        else
            pos += i[2]*dirs[i[1]+1]
        end
    end
    println("🎄 Part 1: $(manhattan_distance(Complex(0,0), pos))")
end

function rot(θ::Float64)
    return cos(θ)+sin(θ)im
end

function part2(instructions::Vector{Tuple{Union{Char, Int64}, Int64}})
    dirs = Complex[-1im, 1, 1im, -1]
    pos = Complex(0, 0)
    waypoint = Complex(10, -1)
    for i in instructions
        if i[1] == 'R'
            θ = i[2]/180*π 
            offset = waypoint - pos
            waypoint = round(offset*rot(θ)) + pos
        elseif i[1] == 'L'
            θ = -i[2]/180*π 
            offset = waypoint - pos
            waypoint = round(offset*rot(θ)) + pos
        elseif i[1] == 'F'
            offset = (waypoint - pos)
            pos += i[2]*offset
            waypoint = pos + offset
        else
            waypoint += i[2]*dirs[i[1]+1]
        end
    end
    println("🎄🎅 Part 2: $(manhattan_distance(Complex(0,0), pos))")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 12        ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
@time part1(inputs)
@time part2(inputs)

include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "input_11.txt"
    lines = readInput(filename)
    seats = Dict{Complex{Int}, Vector{Int}}()
    for y in eachindex(lines)
        for x in eachindex(lines[1])
            if lines[y][x] == 'L'
                seats[Complex(x, y)] = [0, 0]
            end
        end
    end

    return seats
end

function part1(seats::Dict{Complex{Int}, Vector{Int}})
    dirs = [1+1im, 1+0im, 1-1im,
            +1im, -1im,
            -1+1im, -1+0im, -1-1im]
    while true
        changes = false
        for (k, v) in seats

            neighs = 0
            for d in dirs
                neighs += haskey(seats, k+d) ? seats[k+d][1] : 0
            end
            if neighs == 0 && v[1] == 0
                seats[k][2] = 1
                changes = true
            elseif v[1] == 1 && neighs >= 4
                seats[k][2] = 0
                changes = true
            end
        end
    
        for k in keys(seats)
            seats[k][1] = seats[k][2]
        end

        #drawSeats(seats)
        if !changes
            break
        end
    end
    println("🎄 Part 1: $(sum([v[1] for v in values(seats)]))")
end

function drawSeats(seats::Dict{Complex{Int}, Vector{Int}})
    xmax = maximum([real(k) for k in keys(seats)])
    ymax = maximum([imag(k) for k in keys(seats)])
  
    for y in 1:ymax
        for x in 1:xmax
            if haskey(seats, Complex(x, y))
                if seats[Complex(x, y)][1] == 1
                    print("#")
                elseif seats[Complex(x, y)][1] == 0
                    print("L")
                end
            else
                print(".")
            end
        end
        println()
    end
    println()
end

function part2(seats::Dict{Complex{Int}, Vector{Int}})
    xmax = maximum([real(k) for k in keys(seats)])
    ymax = maximum([imag(k) for k in keys(seats)])
    
    dirs = [1+1im, 1+0im, 1-1im,
            +1im, -1im,
            -1+1im, -1+0im, -1-1im]
    while true
        changes = false
        for (k, v) in seats
            neighs = 0
            for d in dirs
                pos = k
                while true
                    pos += d
                    if !(1 <= real(pos) <= xmax && 1 <= imag(pos) <= ymax)
                        break
                    end
                    if haskey(seats, pos)
                        if seats[pos][1] == 1
                            neighs += 1
                        end
                        break
                    end
                end
            end

            if neighs == 0 && v[1] == 0
                seats[k][2] = 1
                changes = true
            elseif v[1] == 1 && neighs >= 5
                seats[k][2] = 0
                changes = true
            end
        end

        for k in keys(seats)
            seats[k][1] = seats[k][2]
        end
        #drawSeats(seats)
        
        if !changes
            break
        end
    end

    println("🎄🎅 Part 2: $(sum([v[1] for v in values(seats)]))")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 11        ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
@time part1(inputs)
inputs = loadInput()
@time part2(inputs)

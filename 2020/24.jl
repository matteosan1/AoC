include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "input_24.txt"
    lines::Vector{String} = readInput(filename) 
    directions_regex = r"e|se|sw|w|nw|ne"
    tiles = Dict{Complex{Int}, Int}() 
    for l in lines
        matches = (m.match for m in eachmatch(directions_regex, l))
        directions = map(x -> dirs[x], matches)
        tiles[sum(directions)] = 1
    end
    return lines
end

function part1(instructions::Vector{String}, dirs::Dict{String, Complex{Int}})
    grid = Dict{Complex{Int}, Int}()

    for ins in instructions
        pos = Complex{Int}(0, 0)
        i = 1
        while i <= length(ins)
            if ins[i] == 'n' || ins[i] == 's'
                d = ins[i:i+1]
                i += 2
            else
                d = string(ins[i])
                i += 1
            end
            pos += dirs[d]
        end

        if haskey(grid, pos)
            grid[pos] = 1 - grid[pos]
        else
            grid[pos] = 1
        end
    end
    
    println("🎄 Part 1: $(sum(values(grid)))")
    return grid
end

function addGrid(grid::Dict{Complex{Int}, Int}, new_grid::Dict{Complex{Int}, Int}, dirs::Dict{String, Complex{Int}})
    for (k, v) in grid
        neighs = [k+d for d in values(dirs)]
        for n in neighs
            if !haskey(grid, n)
                new_grid[n] = 0
            end
        end
    end
    merge!(grid, new_grid)
    empty!(new_grid)
end

function part2(grid::Dict{Complex{Int}, Int}, dirs::Dict{String, Complex{Int}})
    new_grid = Dict{Complex{Int}, Int}()
    addGrid(grid, new_grid, dirs)
    to_flip = Dict{Complex{Int}, Int}()
    for _ in 1:100
        for k in keys(grid)
            val = 0
            for n in [k+d for d in values(dirs)]
                # val += get!(grid, n, 0)
                if haskey(grid, n)
                    val += grid[n]
                else
                    new_grid[n] = 0
                end
            end
            if (grid[k] == 1 && (val == 0 || val > 2)) || (grid[k] == 0 && val == 2)
                to_flip[k] = 1 - grid[k]
            end
        end
        merge!(grid, to_flip)
        merge!(grid, new_grid)
        empty!(to_flip)
        empty!(new_grid)
    end
    println("🎄🎅 Part 2: $(sum(values(grid)))")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 24        ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

dirs = Dict{String, Complex{Int}}("ne"=>1-1im, "nw"=>-1-1im, "se"=>1+1im, 
                                  "sw"=>-1+1im, "e"=>2+0im, "w"=>-2+0im)

inputs = loadInput()
@time grid = part1(inputs, dirs)
@time part2(grid, dirs)

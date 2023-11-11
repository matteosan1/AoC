module AoCUtils

    export readInput, readInputWithBlank, readGrid, drawTextFromGrid

    function readGrid(filename)
        lines = readInput(filename)
        grid = zeros(Int, length(lines[1]), length(lines))

        for y in eachindex(lines)
            for x in eachindex(lines[1])
                grid[x, y] = parse(Int, lines[y][x])
            end
        end

        return grid
    end

    function readInput(filename)
        file = open(filename)
        lines = readlines(file)
        
        inputs = []
        for l in lines
            if l != ""
                push!(inputs, l)
            end
        end

        return inputs
    end

    function readInputWithBlank(filename)
        file = open(filename)
        lines = readlines(file)
        
        inputs = []
        for l in lines
            push!(inputs, l)
        end

        return inputs
    end

    function drawTextFromGrid(grid::Vector{Int}, dims::Tuple{Int, Int}=nothing)
        if !isnothing(dims)
            grid = reshape(grid, dims[1], dims[2])
        end

        xmax, ymax = size(grid)
        for y in 1:ymax
            for x in 1:xmax
                if grid[x, y] == 0
                    print("▒")
                else
                    print("▓")
                end
            end
            println()
        end
    end

end

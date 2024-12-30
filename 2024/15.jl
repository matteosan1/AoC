dirs = Dict('^'=>complex(0,-1), '>'=>complex(1,0), '<'=>complex(-1,0), 'v'=>complex(0,1))

# FIXME GIRA MA DA IL NUMERO SBAGLIATO

function loadInput(filename, part=1)
    lines = readlines(filename)

    grid = Dict()
    instructions = ""
    start = nothing

    for (y, line) in enumerate(lines)
        if line == "" continue end
        if line[1] != '#'
            instructions *= line
        else
            if part == 2
                for (x, c) in enumerate(line)
                    if c == '#'
                        grid[Complex(x, y)] = 1
                        grid[Complex(x+1, y)] = 1 
                    elseif c == '.'
                        grid[Complex(x, y)] = 0
                        grid[Complex(x+1, y)] = 0
                    elseif c == '@'
                        start = Complex(x, y)
                        grid[Complex(x, y)] = 0
                        grid[Complex(x+1, y)] = 0
                    elseif c == 'O'
                        grid[Complex(x, y)] = 3
                        grid[Complex(x+1, y)] = 4
                    end
                    x += 1
                end
            else
                for (x, c) in enumerate(line)
                    if c == '#'
                        grid[Complex(x, y)] = 1
                    elseif c == '.'
                        grid[Complex(x, y)] = 0
                    elseif c == '@'
                        start = Complex(x, y)
                        grid[Complex(x, y)] = 0
                    elseif c == 'O'
                        grid[Complex(x, y)] = 3
                    end
                end
            end
        end
    end

    return grid, instructions, start
end

function move(pos, grid, dir)
    new_pos = pos + dir
    if grid[new_pos] == 3
        move(new_pos, grid, dir)
    elseif grid[new_pos] == 0
        grid[new_pos] = grid[pos]
        grid[pos] = 0
        return new_pos
    else 
        return pos
    end
end

function GPS(grid)
    gps = 0
    for g in keys(grid)
        if grid[g] == 3
            gps += real(g) + imag(g)*100
        end
    end
    return gps
end
    
function part1(grid, instructions, start)
    for i in instructions
        start = move(start, grid, dirs[i])
    end
    score = GPS(grid)
    #draw(grid, start)
    println("🎄 Part 1: $(Int(score))")
end

function move2(pos, grid, dir)
    new_pos = [p + dir for p in pos]

    if dir == -1im || dir == 1im
        if grid[new_pos[1]] == 3 || grid[new_pos[1]] == 4
            return move2(new_pos, grid, dir)
        end
    else
        new_new_pos = Complex{Float64}[]
        for p in new_pos
            if grid[p] == 3
                push!(new_new_pos, p)
                push!(new_new_pos, p + 1im)
            elseif grid[p] == 4
                push!(new_new_pos, p)
                push!(new_new_pos, p - 1im)
            elseif grid[p] == 1
                return pos[1] 
            end
        end
        new_new_pos = unique(new_new_pos) 
        if !isempty(new_new_pos)
            return move2(new_new_pos, grid, dir)
        end
    end

    if all(grid[p] == 0 for p in new_pos)
        for p in pos
            grid[p] = 0
        end
        for p in new_pos
            grid[p] = grid[pos[1]]
        end
    end

    return pos[1]
end

function part2(grid, instructions, start)
    for i in instructions
        start = move2([start], grid, dirs[i])
    end
    score = GPS(grid)
    #draw(grid, start, 2)
    println("🎄🎅 Part 2: $(score)")
end

function main()
    title = "Day 15: Warehouse Woes"
    sub = "❄ "^(length(title)÷2 + 2)
    
    println()
    println(" $title ")
    println(sub)
    
    inputs = loadInput("input_15.txt")
    @time part1(inputs...)
    inputs = loadInput("input_15.txt", 2)
    @time part2(inputs...)
end

main()
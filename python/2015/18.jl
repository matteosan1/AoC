function part1()
    lim = 100
    tsteps = 100
    f = open("instructions18a.txt", "r")
    #f = open("prova.txt", "r")
    lines = readlines(f)

    grid = Array{Int8}(undef, lim, lim)

    for x in 1:lim
        for y in 1:lim
            if lines[y][x] == '.'
                grid[y, x] = 0
            elseif lines[y][x] == '#'
                grid[y, x] = 1
            end
        end
    end

    for steps in 1:tsteps
        new_grid = Array{Int8}(undef, lim, lim)
        for x in 1:lim
            for y in 1:lim
                val = 0
                for dx in -1:1
                    for dy in -1:1
                        if dx == 0 && dy == 0
                            continue
                        end 
                        if 1 <= x+dx <= lim && 1 <= y+dy <= lim
                            val += grid[y+dy, x+dx]
                        end
                    end
                end
                if grid[y, x] == 1
                    if val == 2 || val == 3
                        new_grid[y, x] = 1
                    else
                        new_grid[y, x] = 0
                    end
                elseif grid[y, x] == 0
                    if val == 3
                        new_grid[y, x] = 1
                    else
                        new_grid[y, x] = 0
                    end
                end
            end
        end
        grid = new_grid
    end
    println("🎅 $(sum(grid))")
end

function part2()
    lim = 100
    tsteps = 100
    f = open("instructions18a.txt", "r")
    #f = open("prova.txt", "r")
    lines = readlines(f)

    grid = Array{Int8}(undef, lim, lim)

    for x in 1:lim
        for y in 1:lim
            if lines[y][x] == '.'
                grid[y, x] = 0
            elseif lines[y][x] == '#'
                grid[y, x] = 1
            end
        end
    end
    grid[1, 1] = 1
    grid[lim, lim] = 1
    grid[1, lim] = 1
    grid[lim, 1] = 1

    for steps in 1:tsteps
        new_grid = Array{Int8}(undef, lim, lim)
        for x in 1:lim
            for y in 1:lim
                val = 0
                for dx in -1:1
                    for dy in -1:1
                        if dx == 0 && dy == 0
                            continue
                        end 
                        if 1 <= x+dx <= lim && 1 <= y+dy <= lim
                            val += grid[y+dy, x+dx]
                        end
                    end
                end
                if grid[y, x] == 1
                    if val == 2 || val == 3
                        new_grid[y, x] = 1
                    else
                        new_grid[y, x] = 0
                    end
                elseif grid[y, x] == 0
                    if val == 3
                        new_grid[y, x] = 1
                    else
                        new_grid[y, x] = 0
                    end
                end
            end
        end
        grid = new_grid
        grid[1, 1] = 1
        grid[lim, lim] = 1
        grid[1, lim] = 1
        grid[lim, 1] = 1    
    end
    println("🎄 $(sum(grid))")
end


part1()
part2()
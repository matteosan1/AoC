function part1()
    f = open("instructions6a.txt", "r")
    lines = readlines(f)

    grid = Array{Int8}(undef, 1000, 1000)

    for l in lines
        cmds = split(l)
        
        if cmds[1] == "toggle"
            c1, c2 = parse.(Int, split(cmds[2], ","))
            c3, c4 = parse.(Int, split(cmds[4], ","))
            grid[c1:c3,c2:c4] = ones(c3-c1+1,c4-c2+1) - grid[c1:c3,c2:c4]
        elseif cmds[1] == "turn"
            c1, c2 = parse.(Int, split(cmds[3], ","))
            c3, c4 = parse.(Int, split(cmds[5], ","))
            if cmds[2] == "on"
                grid[c1:c3, c2:c4] .= 1
            else
                grid[c1:c3, c2:c4] .= 0
            end
        end
    end

    println("🎅 ", sum(grid))
end

function part2()
    f = open("instructions6a.txt", "r")
    lines = readlines(f)

    grid = Array{Int8}(undef, 1000, 1000)

    for l in lines
        cmds = split(l)
        
        if cmds[1] == "toggle"
            c1, c2 = parse.(Int, split(cmds[2], ","))
            c3, c4 = parse.(Int, split(cmds[4], ","))
            grid[c1:c3,c2:c4] .+= 2
        elseif cmds[1] == "turn"
            c1, c2 = parse.(Int, split(cmds[3], ","))
            c3, c4 = parse.(Int, split(cmds[5], ","))
            if cmds[2] == "on"
                grid[c1:c3, c2:c4] .+= 1
            else
                grid[c1:c3, c2:c4] .-= 1
                grid[grid .< 0] .= 0
            end
        end
    end

    println("🎄 ", sum(grid))
end

part1()
part2()
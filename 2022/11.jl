include("utils.jl")
using .AoCUtils

function draw(cave)
    xmax, ymax = size(cave)
    for y in 1:ymax
        for x in 1:xmax
            val = cave[x, y] > 9 ? "X" : cave[x, y]
            print(val)
        end
        println()
    end
end

function part1()
    lines = AoCUtils.readInput("input_11.txt")

    xmax = length(lines[1])
    ymax = length(lines)
    cave = Array{Int}(undef, (xmax, ymax))
    for y in 1:ymax
        cave[:, y] = parse.(Int, split(lines[y], ""))
    end

    moves = [(x,y)->(x+1, y), (x,y)->(x-1, y), (x,y)->(x, y+1), (x,y)->(x, y-1),
             (x,y)->(x+1, y+1), (x,y)->(x-1, y-1), (x,y)->(x-1, y+1), (x,y)->(x+1, y-1)]

    #draw(cave)
    #println()
    total_fires = 0
    steps = 100
    for s in 1:steps
        cave .+= 1
        while true
            fires = false
            for x in 1:xmax
                for y in 1:ymax
                    if cave[x, y] > 9
                        cave[x, y] = -1
                        total_fires += 1
                        fires = true
                        for m in moves
                            p_new = m(x, y)
                            if 1 <= p_new[1] <= xmax && 1 <= p_new[2] <= ymax
                                if cave[p_new...] >= 0
                                    cave[p_new...] += 1
                                end
                            end
                        end
                    end
                end
            end

            if !fires
                break
            end
        end
        cave[cave .== -1] .= 0

        #draw(cave)
        #println()
    end

    println("🎄 Part 1: $(total_fires)")
end

function part2()
    lines = AoCUtils.readInput("input_11.txt")

    xmax = length(lines[1])
    ymax = length(lines)
    cave = Array{Int}(undef, (xmax, ymax))
    for y in 1:ymax
        cave[:, y] = parse.(Int, split(lines[y], ""))
    end

    moves = [(x,y)->(x+1, y), (x,y)->(x-1, y), (x,y)->(x, y+1), (x,y)->(x, y-1),
             (x,y)->(x+1, y+1), (x,y)->(x-1, y-1), (x,y)->(x-1, y+1), (x,y)->(x+1, y-1)]

    #draw(cave)
    #println()

    steps = 1
    while true
        cave .+= 1
        while true
            fires = false
            for x in 1:xmax
                for y in 1:ymax
                    #println(x, y)
                    if cave[x, y] > 9
                        #println("fire ", x , " " , y, " ", cave[3, 3])
                        cave[x, y] = -1
                        fires = true
                        for m in moves
                            p_new = m(x, y)
                            if 1 <= p_new[1] <= xmax && 1 <= p_new[2] <= ymax
                                if cave[p_new...] >= 0
                                    cave[p_new...] += 1
                                end
                            end
                        end
                    end
                end
            end

            if !fires
                break
            end
        end
        cave[cave .== -1] .= 0

        if (sum(cave) == 0)
            break
        else
            steps += 1
        end
        #draw(cave)
        #println()
    end

    println("🎄🎅  Part 2:$(steps)")
end

part1()
part2()
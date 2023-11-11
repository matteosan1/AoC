include("utils.jl")
using .AoCUtils

function viable_pairs()
    nodes = Dict() #size, used, avail

    x = 0
    y = 0
    xmax  = 38
    ymax = 28
    lines = readLines("input_22.txt")
    for l in lines[3:end]
        parts = split(l)
        nodes[(x, y)] = (parse(Int, parts[2][1:end-1]), parse(Int, parts[3][1:end-1]), parse(Int, parts[4][1:end-1]))
        y += 1
        if y == 28
            y = 0
            x += 1
        end
    end

    pairs = []
    for y in 0:ymax-1
        for x in 0:xmax-1
            m = (x, y)
            for y1 in 0:ymax-1
                for x1 in 0:xmax-1
                    n = (x1, y1)
                    if n == m
                        continue
                    end
                    if nodes[m][2] != 0
                        if nodes[n][3] > nodes[m][2]
                            push!(pairs, [m, n])
                        end
                    end
                end
            end
        end
    end

    println("🎄 $(length(pairs))")
end

function part2()
    nodes = Dict() #size, used, avail

    x = 0
    y = 0
    xmax  = 38
    ymax = 28
    lines = readLines("input_22.txt")
    for l in lines[3:end]
        parts = split(l)
        nodes[(x, y)] = (parse(Int, parts[2][1:end-1]), parse(Int, parts[3][1:end-1]), parse(Int, parts[4][1:end-1]))
        y += 1
        if y == 28
            y = 0
            x += 1
        end
    end

    pairs = []
    for y in 0:ymax-1
        for x in 0:xmax-1
            m = (x, y)
            if m == (xmax-1, 0)
                print("G")
                continue
            end
            if m == (0, 0)
                print("!")
                continue
            end
            if nodes[m][2] == 0
                print("_")
            elseif nodes[m][1] < 100
                print(".")
            else
                print("#")
            end
        end                        
        println()
    end
    println("🎁🎄 Part 2: by hand")
end 

viable_pairs()
part2()

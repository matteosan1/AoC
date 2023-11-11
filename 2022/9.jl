include("utils.jl")
using .AoCUtils

function part1()
    lines = AoCUtils.readInput("input_9.txt")

    xmax = length(lines[1])
    ymax = length(lines)
    cave = Array{Int}(undef, (xmax, ymax))
    for y in 1:ymax
        cave[:, y] = parse.(Int, split(lines[y], ""))
    end

    moves = [(x,y)->(x+1, y), (x,y)->(x-1, y), (x,y)->(x, y+1), (x,y)->(x, y-1)]

    low_points = []
    risk = 0
    for y in 1:ymax
        for x in 1:xmax
            floor = cave[x, y]
            lower = 0
            neigh = 0
            for m in moves
                (x1, y1) = m(x, y)
                if 1 <= y1 <= ymax && 1 <= x1 <= xmax
                    neigh += 1
                    if cave[x1, y1] > floor 
                        lower+= 1
                    end
                end
            end

            if lower == neigh
                push!(low_points, (x, y))
                risk += floor + 1
            end
        end
    end

    println("🎄 Part 1: $(risk)")
    return low_points, cave
end

function part2(low_points, cave)
    moves = [(x,y)->(x+1, y), (x,y)->(x-1, y), (x,y)->(x, y+1), (x,y)->(x, y-1)]
    xmax, ymax = size(cave)

    s = []
    for p in low_points
        visited = []
        queue = [p]
        while length(queue) != 0
            check = pop!(queue)
            if (check in visited)
                continue
            end
            push!(visited, check)

            for m in moves
                p_new = m(check...)
                if 1 <= p_new[2] <= ymax && 1 <= p_new[1] <= xmax
                    if cave[p_new...] != 9 && !(p_new in visited)
                        push!(queue, p_new)
                    end
                end
            end
        end

        push!(s, length(visited))
    end

    println("🎄🎅 Part 2: $(reduce((x,y)->x*y, sort(s)[end-2:end]))")
end

low_points, cave = part1()
part2(low_points, cave)
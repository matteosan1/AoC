include("utils.jl")
using .AoCUtils: readInput, HeapDict, draw_array

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

function loadInput()
    lines = readInput("prova.txt")#input_15.txt")

    xmax = length(lines[1])
    ymax = length(lines)
    chitons = Array{Int}(undef, (xmax, ymax))
    for y in 1:ymax
        chitons[:, y] = parse.(Int, split(lines[y], ""))
    end
    return chitons
end

function findPath(chitons)
    moves = [(x,y)->(x+1, y), (x,y)->(x-1, y), (x,y)->(x, y+1), (x,y)->(x, y-1)]
    
    xmax = size(chitons)[1]
    ymax = size(chitons)[2]

    start = (1, 1)
    shortest = ones(Int, xmax, ymax) * -1
    shortest[start...] = 0
    que = HeapDict((start, 0))
    visited = Set()

    steps = 0
    while length(que) != 0
        node, dist = popfirst!(que)
        push!(visited, node)
        for m in moves
            neigh = m(node...)
            if 1 <= neigh[1] <= xmax && 1 <= neigh[2] <= ymax && !(neigh in visited)
                new_dist = shortest[node...] + chitons[neigh...]
                if new_dist < shortest[neigh...] || shortest[neigh...] == -1
                    shortest[neigh...] = new_dist
                    que[neigh] = new_dist
                end
            end
        end
    end

    return shortest
end

function part1(chitons)
    shortest = findPath(chitons)

    println("🎄 Part 1: $(shortest[end][end])")
    draw_array(chitons)
end

function part2(chitons)
    a = zeros(Int, size(chitons)[1]*5, size(chitons)[2]*5)
    for i in 0:4
        x0 = 1 + i*size(chitons)[1]
        x1 = (i+1)*size(chitons)[1]
        for j in 0:4
            y0 = 1 + j*size(chitons)[1]
            y1 = (j+1)*size(chitons)[1]
            a[y0:y1, x0:x1] = chitons .+ (i+j)
        end
    end

    a[a .> 9] .%= 9

    shortest = findPath(transpose(a))
    println("🎄🎅 Part 2: $(shortest[end][end])")
end

chitons = loadInput()
part1(chitons)
part2(chitons)
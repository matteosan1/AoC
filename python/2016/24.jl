include("utils.jl")
using .AoCUtils
using Combinatorics

function bfs(pair, points, cm)
    start = points[pair[1]]
    target = points[pair[2]]
    visited = Dict()
    steps = 0
    current = Dict(start=>nothing)

    while true
        new_pos = Dict()
        for (c, prec) in current
            if haskey(visited, c)
                if visited[c][2] > steps
                    visited[c] = (prec, steps)
                end
            else
                visited[c] = (prec, steps)
                for s in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    pos = (c[1] + s[1], c[2] + s[2])
                    if 0 < pos[1] <= size(cm)[1] && 0 < pos[2] <= size(cm)[2] && cm[pos[1], pos[2]] != 1 
                        if !haskey(new_pos, pos)
                            new_pos[pos] = c
                        end
                    end
                end
            end
        end
                
        current = new_pos
        if haskey(visited, target)
            return visited[target][2]
        end
        steps += 1
    end
end

function calc(lines)
    xmax = length(lines[1])
    ymax = length(lines)
    cm = zeros(Int, xmax, ymax)
    points = Dict()

    for y in 1:ymax
        for x in 1:xmax
            if lines[y][x] == '#'
                cm[x, y] = 1
            elseif isnumeric(lines[y][x])
                points[parse(Int, lines[y][x])] = (x, y)
            end
        end
    end

    distances = Dict(i=>Dict() for i in eachindex(points))
    for c in combinations(0:length(points)-1, 2)
        distance = bfs(c, points, cm)
        distances[c[1]][c[2]] = distance
        distances[c[2]][c[1]] = distance
    end
    println(distances)
    min_dists = [1e10, 1e10]
    for p in permutations(1:length(points)-1)
        alle = insert!(copy(p), 1, 0)
        retour = push!(copy(alle), 0)
        paths = [alle, retour]
        for i in 1:2
            dist = sum([distances[paths[i][j]][paths[i][j+1]] for j in 1:length(paths[i])-1])
            if dist < min_dists[i]
                min_dists[i] = dist
            end
        end
    end

    println("🎄 $(min_dists[1])")
    println("🎁🎄 $(min_dists[2])")
end

lines = AoCUtils.readLines("input_24.txt")
calc(lines)

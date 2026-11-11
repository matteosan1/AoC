using Combinatorics

function part1()
    f = open("instructions9a.txt", "r")
    lines = readlines(f)

    distances = Dict{String, Dict{String, Int32}}()

    for l in lines
        items = split(l, " ")
        d = parse(Int32, items[end])
        f = items[1]
        t = items[3]
        if haskey(distances, f)
            distances[f][t] = d
        else
            distances[f] = Dict(t => d)
        end

        if haskey(distances, t)
            distances[t][f] = d
        else
            distances[t] = Dict(f => d)
        end
    end 

    min_distance = 1e8
    max_distance = 0
    k = collect(keys(distances))
    for p in unique(permutations(k))
        dist = 0
        for i in 1:length(p)-1
            dist += distances[p[i]][p[i+1]]
        end
        if dist < min_distance
            min_distance = dist
        end
    
        if dist > max_distance
            max_distance = dist
        end
    end
    
    println("🎅 ", min_distance)
    println("🎄 ", max_distance)
end

part1()
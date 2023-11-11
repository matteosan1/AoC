include("utils.jl")
using .AoCUtils

using DataStructures

struct Disk
    name::String
    weight::Int
    disks::Array{String}
    Disk(name, weight, line) = new(name, weight, strip.(split(line, ",")))
end

function show(io::IO, disk::Disk)
    print("$(disk.name) $(disk.weight) $(disk.disks)")
end

function findWeight(towers, t, level=0)
    if level != 0
        w = towers[t].weight
    end

    if towers[t].disks[1] != ""
        level += 1
        for d in towers[t].disks
            w += findWeight(towers, d, level)[1]
        end
    else
        if level == 0
            level = -1
        end
        w = towers[t].weight
    end
    return w, level
end

function part1(towers)
    supported = []
    for t in keys(towers)
        append!(supported, towers[t].disks)
    end
    supported = Set(supported)
    
    start = pop!(setdiff(Set(keys(towers)), supported))
 
    println("🎄 $(start)")
end

function load()
    towers = Dict()
    lines = AoCUtils.readLines("input_7.txt")
    for l in lines
        if startswith(l, "###")
            break
        end
        parts = split(l, "->")
        name, weight = split(parts[1])
        weight = parse(Int, weight[2:end-1])
        if length(parts) == 2
            d = Disk(name, weight, parts[2])
        else
            d = Disk(name, weight, "")
        end
        #show(d)
        towers[name] = d
    end

    return towers
end

function part2(towers)
    weights = dict()
    toweight = []
    h = heapq()
    
    heapq.heappush(toweight, start)

    while length(toweight) != 0
        t = heapq.heappop(toweight)
        if towers[t].disks[1] != ""
            w, l = findWeight(towers, t)
        weights[t] = (towers[t].disks, w)
        for d in towers[t].disks
            heapq.heappush(toweight, d)
        end

    # diff = nothing
    # suspect = None
    # for (k, v) in weights
    #     temp = Counter([weights[t][1] for t in v[0] if t in weights])
    #     if length(temp) > 1
    #         wrong_weight = [k for (k,v) in temp if v == 1][0]
    #         right_weight = [k for (k,v) in temp if v != 1][0]
    #         diff = right_weight - wrong_weight
    #         suspect = [t for t in v[0] if t in weights and weights[t][1] == wrong_weight][0]
    #     end
    # end
            
    # println("🎁🎄 $(suspect) $(towers[suspect].weight) $diff)")
end

towers = load()
part1(towers)
part2(towers)

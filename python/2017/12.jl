include("utils.jl")
using .AoCUtils
using DataStructures

function run()
    connections = Dict()
    lines = AoCUtils.readLines("input_12.txt")
    for l in lines
        l = split(l, "<->")
        connections[parse(Int, l[1])] = parse.(Int, split(l[2], ","))
    end

    all_progs = sort(collect(keys(connections)))
    groups = []
    while length(all_progs) != 0
        progs = MutableBinaryMinHeap{Int}([])
        push!(progs, all_progs[1])
        group = Set()
        while length(progs) != 0
            p = pop!(progs)
            for candidate in connections[p]
                if !(candidate in group)
                    push!(progs, candidate)
                end
            end
            push!(group, p)
        end
        push!(groups, (group, length(group)))
        for g in group
            filter!(x->x!=g, all_progs)
        end
    end
    println("🎄 $(groups[1][2])")
    println("🎁🎄 $(length(groups))") 
end

run()

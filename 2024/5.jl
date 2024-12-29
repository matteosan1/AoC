using Statistics

function loadInput(filename::String)
    lines = readlines(filename)
    orderings = [parse.(Int, split(l, "|")) for l in lines if occursin("|", l)]
    updates = [parse.(Int, split(l, ",")) for l in lines if occursin(",", l)]
    return orderings, updates
end

function part1(orderings::Vector{Vector{Int}}, updates::Vector{Vector{Int}})
    mid_page = 0
    ordered = Int[]
    for (iu, upd) in enumerate(updates)
        is_ordered = true
        for x in 1:(length(upd) - 1)
            if !in([upd[x], upd[x + 1]], orderings)
                is_ordered = false
                break
            end
        end
        if is_ordered
            push!(ordered, iu)
            mid_page += upd[div(length(upd), 2)+1]
        end
    end
    println("🎄 Part 1: $mid_page")
    return ordered
end

function part2(orderings::Vector{Vector{Int}}, updates::Vector{Vector{Int}}, ordered::Vector{Int})
    mid_page = 0
    for (iu, upd) in enumerate(updates)
        if iu in ordered
            continue
        end
        new_orderings = filter(o -> o[1] in upd && o[2] in upd, orderings)
        rank = Dict(u => 0 for u in upd)
        for o in new_orderings
            rank[o[2]] += 1
        end
        sorted_keys = sort(collect(keys(rank)), by=x -> rank[x])
        mid_page += sorted_keys[length(sorted_keys) ÷ 2+1] 
    end
    println("🎄🎅 Part 2: $mid_page")
end

function main()
    title = "Day 5: Print Queue"
    sub = "❄ "^(length(title)÷2 + 2)

    println()
    println(" $title ")
    println(sub)

    inputs = loadInput("input_5.txt")
    @time ordered = part1(inputs...)
    @time part2(inputs..., ordered)
end

main()
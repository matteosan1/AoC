include("utils.jl")
using .AoCUtils: readInputWithBlank

function loadInput()
    filename = "input_16.txt"
    lines = readInputWithBlank(filename)
    rules = Dict{String, Vector{Int}}()
    myticket = Int[]
    tickets = Vector{Vector{Int}}()
    phase = 1
    for l in lines
        if l == ""
            phase += 1
            continue
        elseif l == "your ticket:" || l == "nearby tickets:"
            continue
        end
        if phase == 1
            regexp = r"([\w\s]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)"
            m = match(regexp, l)
            rules[string(m[1])] = (parse.(Int, [m[2], m[3], m[4], m[5]]))
        elseif phase == 2
            myticket = parse.(Int, split(l, ","))
        elseif phase == 3
            push!(tickets, parse.(Int, split(l, ",")))
        end
    end
    return rules, myticket, tickets
end

function part1(rules::Dict{String, Vector{Int}}, tickets::Vector{Vector{Int}})
    invalid = 0
    it = 1
    while it <= length(tickets)
        remove = false
        for x in tickets[it]
            if all([!(v[1] <= x <= v[2] || v[3] <= x <= v[4]) for v in values(rules)])
                invalid += x
                remove = true
            end
        end
        if remove
            deleteat!(tickets, it)
        else
            it += 1
        end
    end
    println("🎄 Part 1: $(invalid)")
end

function part2(rules::Dict{String, Vector{Int}}, myticket::Vector{Int64}, tickets::Vector{Vector{Int64}})    
    push!(tickets, myticket)
    col_names = Dict{Int, Vector{String}}()
    for column in 1:length(tickets[1])
        for (k, v) in rules
            if all([(v[1] <= t[column] <= v[2] || v[3] <= t[column] <= v[4]) for t in tickets])
                if !haskey(col_names, column)
                    col_names[column] = [k]
                else
                    push!(col_names[column], k)
                end
            end
        end
    end
    
    while true
        change = false
        for k in keys(col_names)
            if length(col_names[k]) == 1
                for v in values(col_names)
                    if length(v) > 1
                        filter!(x->x!=col_names[k][1], v)
                        change = true
                    end
                end
            end
        end
        if !change
            break
        end
    end
   
    val = prod([myticket[k] for (k, v) in col_names if startswith(first(v), "departure")])
    println("🎄🎅 Part 2: $(val)")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 16        ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

rules, myticket, tickets = loadInput()
@time part1(rules, tickets)
@time part2(rules, myticket, tickets)

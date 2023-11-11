include("utils.jl")
using .AoCUtils

function valuesTo(l, value, idx)
    if !haskey(l, idx)
        l[idx] = Array{Int}(undef, 0)
    end

    push!(l[idx], value)
    sort!(l[idx])
end

function run(lines, part)
    bots = Dict{Int, Array{Int}}()
    outputs = Dict{Int, Array{Int}}()

    while true
        new_lines = []
        for l in lines
            if startswith(l, "value")
                args = split(l, " ")
                value = parse(Int, args[2])
                bot = parse(Int, args[end])
                valuesTo(bots, value, bot)
            elseif startswith(l, "bot")
                args = split(l, " ")
                bot = parse(Int, args[2])
                if haskey(bots, bot) && length(bots[bot]) == 2
                    low = parse(Int, args[7])
                    if args[6] == "output"
                        valuesTo(outputs, bots[bot][1], low)
                    else
                        valuesTo(bots, bots[bot][1], low)
                    end

                    high = parse(Int, args[end])
                    if args[end - 1] == "output"
                        valuesTo(outputs, bots[bot][2], high)
                    else
                        valuesTo(bots, bots[bot][2], high)
                    end
                else
                    push!(new_lines, l)
                end
            end
        end

        if part == 1
            for (k, v) in bots
                if v == [17, 61]
                    println("🎄 $k")
                    return
                end
            end
        end

        if length(new_lines) != 0
            lines = new_lines
        else
            break
        end
    end

    println("🦌 $(outputs[0][1]*outputs[1][1]*outputs[2][1])")
end

lines = readLines("input_10.txt")
run(lines, 1)
run(lines, 2)
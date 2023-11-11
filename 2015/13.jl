using Combinatorics

function readInput(part)
    if part == 1
        filename = "instructions13a.txt"
    else
        filename = "instructions13b.txt"
    end

    f = open(filename, "r")
    lines = readlines(f)

    happiness = Dict{Union{String, SubString}, Any}()

    for l in lines
        items = split(l, " ")
        coeff = 1
        if items[3] == "lose"
            coeff = -1
        end
        name = items[end][1:end-1]
        val = parse(Int, items[4])
        if haskey(happiness, items[1])
            happiness[items[1]][name] = coeff * val
        else
            happiness[items[1]] = Dict(name => coeff * val)
        end
    end
    happinesses = []

    for p in permutations(collect(keys(happiness)), length(happiness))
        happyness = 0
        for f in 1:length(p)-1
            happyness += happiness[p[f]][p[f+1]] + happiness[p[f+1]][p[f]]
        end
        happyness += happiness[p[length(p)]][p[1]] + happiness[p[1]][p[length(p)]]
        append!(happinesses, happyness)
    end

    if part == 1
        println("🎅 ", maximum(happinesses))
    else
        println("🎄 ", maximum(happinesses))
    end
end 

readInput(1)
readInput(2)
using Combinatorics

struct Sue
    idx::String
    properties::Dict{String, Int}
end

function readInput()
    sues = Vector{Sue}()
    f = open("instructions16a.txt", "r")

    lines = readlines(f)
    for l in lines
        name = split(l, ": ")[1]
        items = split(l, ", ")
        vals = Dict(x[end-1]=>parse(Int, x[end]) for x in split.(items, " "))
        push!(sues, Sue(name, vals))
    end       
    return sues
end

function MFCSAM(sues::Vector{Sue}, outcome)
    remaining = Vector{Sue}()
    for s in sues
        right = true
        for (k, v) in outcome
            if haskey(s.properties, k)
                if s.properties[k] != v
                    right = false
                    break
                end
            end
        end

        if right
            push!(remaining, s)
        end
    end
    println("🎅 $(remaining[1])")
end

function MFCSAM_v2(sues::Vector{Sue}, outcome)
    remaining = Vector{Sue}()
    for s in sues
        right = true
        for (k, v) in outcome
            if haskey(s.properties, k)
                if k == "cats:" || k == "trees:"
                    if s.properties[k] <= v
                        right = false
                        break
                    end
                elseif k == "pomeranians:" || k == "goldfish:"
                    if s.properties[k] >= v
                        right = false
                        break
                    end
                else
                    if s.properties[k] != v
                        right = false
                        break
                    end
                end
            end
        end

        if right
            push!(remaining, s)
        end
    end
    println("🎄 $(remaining[1])")
end

outcome = Dict("children:"=> 3, "cats:"=>7, "samoyeds:"=>2, "pomeranians:"=>3,
               "akitas:"=>0, "vizslas:"=>0, "goldfish:"=>5, "trees:"=>3,
               "cars:"=>2, "perfumes:"=>1)

sues = readInput()
MFCSAM(sues, outcome)
MFCSAM_v2(sues, outcome)
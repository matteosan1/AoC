include("utils.jl")
using .AoCUtils

function selectIP(lines)
    ips = []
    for i in eachindex(lines)
        push!(ips, parse.(Int, split(lines[i], "-")))
    end

    sort!(ips)
    blocked = []
    for parts in ips
        if length(blocked) == 0
            push!(blocked, parts)
        else
            inserted = false
            for (i, b) in enumerate(blocked)
                if b[1]-1 <= parts[1] <= b[2]+1
                    if parts[2] > b[2]
                        blocked[i] = [b[1], parts[2]]
                    end
                    inserted = true
                    break
                elseif b[1]-1 <= parts[2] <= b[2]+1
                    if parts[1] < b[1]
                        blocked[i] = [parts[1], b[2]]
                    elseif parts[1] < b[1] && parts[2] > b[2]
                        blocked[i] = parts
                    end
                    inserted = true
                    break
                end
            end

            if !inserted
                push!(blocked, parts)    
            end
        end  
    end
    println("🎄 $(blocked[1][2]+1)")

    allowed = 4294967296
    for b in blocked
       allowed -= b[2] - b[1] + 1
    end

    println("🎁🎄 $(allowed)")
end

lines = readLines("input_20.txt")
selectIP(lines)
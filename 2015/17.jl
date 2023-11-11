using Combinatorics

function readInput()
    bottles = Vector{Int}()
    f = open("instructions17a.txt", "r")
    
    lines = readlines(f)
    for l in lines
        push!(bottles, parse(Int, l))
    end       
    return bottles
end

function check(bottles::Vector{Int}, vol::Int)
    combs = Dict{Int,Int}()
    
    for mask in 1:1<<length(bottles)
        p = [d for (i,d) in enumerate(bottles) if (mask & (1<<(i-1))) > 0]
        if sum(p) == vol
            if haskey(combs, length(p))
                combs[length(p)] += 1
            else
                combs[length(p)] = 1
            end
        end
    end

    println("🎅 $(sum(values(combs)))")
    println("🎄 $(combs[minimum(keys(combs))])")
end

bottles = readInput()
check(bottles, 150)

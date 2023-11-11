include("utils.jl")
using .AoCUtils

function loadInput()
    lines = readInput("input_12.txt")
    segments = Dict()
    for l in lines
        b, e = split(l, "-")
        if haskey(segments, b)
            push!(segments[b], e)
        else
            segments[b] = [e]
        end

        if haskey(segments, e)
            push!(segments[e], b)
        else
            segments[e] = [b]
        end
    end
    return segments
end

function part1(segments)
    paths = []
    queue = [["start", n] for n in segments["start"]]
    while length(queue) != 0
        q = pop!(queue)
        for n in segments[q[end]]
            if islowercase(n[1]) && (n in q)
                continue
            end
            new_q = push!(copy(q), n)
            if n == "end"
                push!(paths, new_q)
            else
                push!(queue, new_q)
            end
        end
    end

    println("🎄 $(length(paths))")
end


function part2(segments)
    paths = []
    queue = [(["start", n], false) for n in segments["start"]]
    while length(queue) != 0
        q = pop!(queue)
        for n in segments[q[1][end]]
            if n == "start"
                continue
            end

            new_q = push!(copy(q[1]), n)
            if n == "end"
                push!(paths, new_q)
                continue
            end

            if islowercase(n[1]) 
                if !(n in q[1])  
                    push!(queue, (new_q, q[2]))
                elseif (n in q[1]) && !q[2]
                    push!(queue, (new_q, true))
                end
            else
                push!(queue, (new_q, q[2]))
            end
        end
    end
    println("🎄🎅 $(length(paths))")
end

segments = loadInput()
part1(segments)
part2(segments)

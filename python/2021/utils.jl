module AoCUtils

export readInput, HeapDict, draw_array

function readInput(filename)
    file = open(filename)
    lines = readlines(file)
    
    inputs = []
    for l in lines
        if l != ""
            push!(inputs, l)
        end
    end

    return inputs
end

function Base.isless(a::Tuple{Tuple, Int64}, b::Tuple{Tuple, Int64})
    if a[2] < b[2]
        return true
    else
        return false
    end
end

mutable struct HeapDict{T}
    values::Vector{Tuple{T, Int}}
end

function HeapDict(val::Tuple{Any, Int})
    v = Vector{Tuple{Any, Int}}()
    push!(v, val)

    return HeapDict(v)
end

function Base.setindex!(h::HeapDict, val, key)
    push!(h, (key, val))
end

function Base.push!(h::HeapDict, val::Tuple)
    push!(h.values, val)
    sort!(h.values)
end

function Base.pop!(h::HeapDict)
    return pop!(h.values)
end

function Base.popfirst!(h::HeapDict)
    return popfirst!(h.values)
end

function Base.getindex(h::HeapDict, idx::Tuple)
    i = findfirst(x->x[1]==idx, h.values)
    return h.values[i][2]
end

function Base.length(h::HeapDict)
    return length(h.values)
end

# function printPath(cm, paths, start, stop)
#     path = [stop]
#     pos = stop
#     neighs = [(x,y)->(x+1, y), (x,y)->(x-1, y), (x,y)->(x, y+1), (x,y)->(x, y-1)]
#     xmax = size(paths)[1]
#     ymax = size(paths)[2]
#     while pos != start
#         neis = [(pos[1] + n[1], pos[2] + n[2]) for n in neighs if 1 <= pos[1]+n[1] <= xmax && 1 <= pos[2]+n[2] <= ymax]
#         m = 100000000
#         p = nothing
#         for n in neis
#             if n != path[end] && paths[(n[1], n[2])] < m
#                 p = n
#                 m = paths[(n[1], n[2])]
#             end
#         end
#         pos = p
#         push!(path, p)
#     end

#     printArray(cm, path)#, bcolors.BOLD)
# end

function draw_array(cm)# points, color=bcolors.OKGREEN)
    # if isnothing(points)
    #     for y in range(cm.shape[1]):
    #         for x in range(cm.shape[0]):
    #             print (int(cm[x, y]), end="")
    #         print ("")
    # else:
    #points = list(map(tuple, points))
    xmax = size(cm)[1]
    ymax = size(cm)[2]
    for y in 1:ymax
        for x in 1:xmax
            #if (x,y) in points:
            #        print (color + str(int(cm[x, y])) + bcolors.ENDC, end="")
            #    else:
            printstyled(cm[x, y], color=:green)
#                bcolors.GREY + str(int(cm[x, y])) + bcolors.ENDC, end="")
        end
        println()
    end
end

end
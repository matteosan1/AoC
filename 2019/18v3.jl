using DataStructures

function readMap(filename)
    lines = open(filename) do f
        [l for l in readlines(f)]
    end
   
    dungeon = Dict{Tuple{Int, Int}, Char}()
    start = (0, 0)
    theKeys = Dict{Char, Tuple{Int, Int}}()
    
    for (y, l) in enumerate(lines)
        for (x, c) in enumerate(l)
            if c == '@' || 'a' <= c <= 'z'
                start = (x-1, y-1)
                theKeys[c] = (x-1, y-1)
            elseif c == '#'
                continue
            end
            dungeon[(x-1,y-1)] = c
        end
    end
    
    return start, dungeon, theKeys
end

function BFS(start::Tuple{Int, Int},
             target::Tuple{Int, Int},
             dungeon::Dict{Tuple{Int, Int}, Char})
    
    queue = [(start, 0, [], [])]
    dirX = (-1, 0, 0, 1)
    dirY = (0, -1, 1, 0)
    visited = Set{Tuple{Int, Int}}()
    K = Dict{Char, Float64}()
    C = Dict{Char, Tuple}()
    
    while !isempty(queue)
        coord, steps, gkeys, ckeys = popfirst!(queue)
        if coord in visited
            continue
        end

        push!(visited, coord)
        if 'a' <= dungeon[coord] <= 'z'            
            push!(ckeys, dungeon[coord])
        end

        if coord == target
            #if length(ckeys) > 1 && length(gkeys) == 0
            #    steps = Inf
            #end
            K = steps
            C = (gkeys, ckeys)
            break
        end
        

        for i in 1:4
            dx = coord[1] + dirX[i]
            dy = coord[2] + dirY[i]
            if (dx, dy) in keys(dungeon)
                new_coord = (dx, dy)
                new_gkeys = copy(gkeys)
                new_ckeys = copy(ckeys)
                if 'A' <= dungeon[new_coord] <= 'Z' &&
                    !(lowercase(dungeon[new_coord]) in ckeys)
                    push!(new_gkeys, lowercase(dungeon[new_coord]))
                end
                    
                push!(queue, (new_coord, steps+1, new_gkeys, new_ckeys))
            end
        end
    end
    
    return K, C
end

function popmin!(queue::Vector{Tuple})
    idx = reduce((x,y) -> y[2][1] < x[2][1] ? y : x, enumerate(queue))
    println(idx)
    return popat!(queue, idx[1])
end

function dijkstra(proximity::Dict, constraints::Dict, nkeys::Int)
    
    queue = Vector{Tuple}() # distance, key, collected_keys
    push!(queue, (0, '@', Set(), Set()))
    #visited = Set{Char}()

    while !isempty(queue)
        d, node, gkeys, fetched_k = popmin!(queue)
        println("node gkeys ", node, " ", gkeys, " ", fetched_k)
        
        if node in fetched_k
            continue
        end

        #for k in fetched_k
        #    push!(visited,  k)
        #end
        #println(visited)
       
        if length(gkeys) == nkeys-1
            println("FINE ", d)
            return
        end
        
        for (target, steps) in pairs(proximity[node])
            if steps == Inf
                continue
            end
            println(constraints[node][target], " ", node, " ", target)
            needed_k, fetched_k = constraints[node][target]
            println(gkeys, " ", Set(needed_k), issubset(Set(needed_k), Set(gkeys)))
            if (issubset(Set(needed_k), Set(gkeys)))
                println(target, " ", steps)
                new_keys = Set(copy(gkeys))
                for k in fetched_k
                    push!(new_keys, k)
                end
                println("new keys ", new_keys)
                push!(queue, (d+steps, target, new_keys, fetched_k))
            end
        end
        #println(queue)
    end
end

function runv3()
    start, dungeon, mykeys = readMap("input_18.txt")

    constraints = Dict(ch=>Dict() for ch in keys(mykeys))
    proximity = Dict(ch=>Dict() for ch in keys(mykeys))
    
    for k in keys(mykeys)
        for k1 in keys(mykeys)
            if k != k1 && k1 != '@'
            #if k == '@' && k1 == 'b'
                proximity[k][k1], constraints[k][k1] = BFS(mykeys[k],
                                                           mykeys[k1],
                                                           dungeon)
            end
        end
    end
    for (k, v) in pairs(proximity)
        println(k, " ", v)
    end
    
    for (k, v) in pairs(constraints)
        for (k1, v1) in pairs(v)
            println(k, " ", k1, " ", v1)
        end
    end
    dijkstra(proximity, constraints, length(mykeys))
    
end

runv3()

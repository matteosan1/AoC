using DataStructures

function readMap(filename)
    lines = open(filename) do f
        [l for l in readlines(f)]
    end
   
    dungeon = Dict{Tuple{Int, Int}, Char}()
    start = (0, 0)
    theKeys = Dict{Int, Tuple{Int, Int}}()
    
    for (y, l) in enumerate(lines)
        for (x, c) in enumerate(l)
            if c == '@' || 'a' <= c <= 'z'
                start = (x-1, y-1)
                #theKeys[keyidx(c)] = (x-1, y-1)
                theKeys[c] = (x-1, y-1)
            elseif c == '#'
                continue
            end
            dungeon[(x-1,y-1)] = c
        end
    end
    
    return start, dungeon, theKeys
end

#b = 0          # The empty bitset :)
#b |= 1 << i    # Set
#b & 1 << i     # Test
#b &= ~(1 << i) # Reset
#b ^= 1 << i    # Flip i
#b = ~b         # Flip all

function isdoor(ch::Char)
    return 'A' <= ch <= 'Z'
end

function keyidx(ch::Char)
    if ch == '@'
        return 1
    return Int(codepoint(ch))-Int(codepoint('a')) + 2
end

function dooridx(ch::Char)
    return Int(codepoint(ch))-Int(codepoint('A')) + 2
end

function has_key(visited::Int, ch::Char)
    return (visited & (1<<dooridx(ch))) != 0
end

function BFS(start::Tuple{Int, Int},
             dungeon::Dict{Tuple{Int, Int}, Char},
             proximity::Matrix{Float64},
             constraints::Matrix{Tuple})
    
    queue = [(start, 0, [])]
    dirX = (-1, 0, 0, 1)
    dirY = (0, -1, 1, 0)
    visited = Set{Tuple{Int, Int}}()
   
    while !isempty(queue)
        coord, steps, gkeys = popfirst!(queue)
        if coord in visited
            continue
        end
        push!(visited, coord)
        if 'a' <= dungeon[coord] <= 'z' && coord != start
            collected_keys = (1<<keyidx(dungeon[coord]))
            for (k, v) in pairs(K)
                if v[2] == gkeys && v[1] < steps
                    delete!(K, k)
                    collected_keys |= v[3]
                end
            end
            #K[keyidx(dungeon[coord])] = (steps, gkeys, collected_keys)
            proximity[keyidx[dungeon[start]]][keyidx[dungeon[coord]]] = steps
            constraints[keyidx[dungeon[start]]][keyidx[dungeon[coord]]] = (gkeys, collected_keys)
        end
       
        for i in 1:4
            dx = coord[1] + dirX[i]
            dy = coord[2] + dirY[i]
            if (dx, dy) in keys(dungeon)
                new_coord = (dx, dy)
                #if start_label == -1
                #    if isdoor(dungeon[new_coord])
                #        println(dungeon[new_coord], " ", gkeys, " ", dooridx(dungeon[new_coord]))
                #    end
                #end
                if isdoor(dungeon[new_coord]) && ((gkeys & (1<<dooridx(dungeon[new_coord]))) == 0 || gkeys == 0)
                    #if start_label == -1
                    #    println(new_coord, " ", gkeys, " ", dungeon[new_coord], " ", dooridx(dungeon[new_coord]))
                    #end

                    new_keys = gkeys | (1 << dooridx(dungeon[new_coord]))
                else
                    new_keys = gkeys
                end
                
                push!(queue, (new_coord, steps+1, new_keys))
            end
        end
    end
    
    return K
end

function popmin!(queue::Vector{Tuple})
    idx = reduce((x,y) -> y[2][1] < x[2][1] ? y : x, enumerate(queue))
    println(idx)
    return popat!(queue, idx[1])
end

function bits(x)
    return collect(x>>i & 1 for i in 0:sizeof(x)-1)
end

function dijkstra(map::Dict, nkeys::Int)
    
    allKeys = nkeys#(1 << nkeys) - 1
    queue = Vector{Tuple}() # distance, key, collected_keys
    push!(queue, (0, -1, 0, 0))
    dist = Set{Int}()

    while !isempty(queue)
        d, node, gkeys, fetched_k = popmin!(queue)
        println("d, node gkeys", d, node, gkeys)
        
        if node in dist
            continue
        end

        bs =  bits(fetched_k)
        println(bs)
        for (i, b) in enumerate(bs)
            if b==1
                push!(dist,  i-1)
            end
        end
        println(dist)
       
        if gkeys == allKeys
            println("FINE ", d)
            return
        end

        for (i, (delta, needed_k, fetched_k)) in pairs(map[node])
            println("testing ", i, " ", delta, " ", gkeys)
            println("checks ", needed_k, " ", gkeys&needed_k, " ", fetched_k)
            if (gkeys & needed_k == needed_k || needed_k == 0) #&& !(i in dist)
                new_keys = (gkeys | needed_k ) | (fetched_k)
                println("new keys ", new_keys)
                push!(queue, (d+delta, i, new_keys, fetched_k))
            end
        end
        println(queue)
    end
end

#function dijkstra(map, nkeys::Int)
#    
#    allKeys = (1 << nkeys) - 1
#    queue = Vector{Tuple}()
#    push!(queue, (0, (-1, 0)))
#    #enqueue!(queue, (0, (-1, 0)))
#    dist = Dict{Tuple, Int}()
#    minimum  = 100000
#
#    while !isempty(queue)
#        d, node = popmin!(queue)
#        #println(d, node)
#        if haskey(dist, node) #&& dist[node] <= d
#            continue
#        end
#        dist[node] = d
#        #println(dist)
#       
#        u, S = node
#        println("u-S ", u, " ", S)
#        if S == allKeys && d < minimum
#            minimum = d
#        end
#
#        for (v, (w, T)) in pairs(map[u])
#            println("v-w-T ", v, " ", w, " ", T)
#            if ((T & S) != 0 || S == 0) && (S & v) == 0
#                S |= (1 << v)
#                println("newS ", S)
#                #enqueue!(queue, (d+w, (v, S)))
#                push!(queue, (d+w, (v, S)))
#            end
#        end
#        println(queue)
#    end
#    println(minimum)
#    
#end

function dijkstra_std(map::Matrix{Float64}, start::Int)
    queue = Vector{Tuple}()
    push!(queue, (0, 1))
    dist = Vector{Int}()

    while !isempty(queue)
        d, node = popmin!(queue)
        
        #if node in dist
        #    continue
        #end
        #push!(dist, node)

        if node == 5
            println("FINE ", d)
            return
        end

        for (i, t) in enumerate(map[node, :])
            if t != Inf && !(i in dist)
                push!(queue, (d+t, i))
            end
        end
    end
end

function runv2()
    start, dungeon, mykeys = readMap("input_18.txt")
    #println(mykeys)
    proximity = zeros(Float64, length(mykeys), length(mykeys))#Dict()
    proximity = fill(proximity, Inf)
    constraints = [(0,0) for i in 1:length(mykeys)^2]
    constraints = reshape(constraints, length(mykeys), length(mykeys))

    #map = Dict(ch=>Dict() for ch in keys(mykeys))
    for k in keys(mykeys)
        for (t, v) in pairs(BFS(mykeys[k], dungeon, proximity, constraints))
            map[k][t] = v
        end
    end
    #println(map)
    #dijkstra(map, length(mykeys))
end

function test()
    map::Matrix{Float64} = [Inf  7    9 Inf Inf  14
                            Inf Inf 10  15 Inf Inf
                            Inf Inf Inf  11 Inf   2
                            Inf Inf Inf Inf   6 Inf
                            Inf Inf Inf Inf Inf   9
                            Inf Inf Inf Inf Inf Inf]
    
    start = 1
    dijkstra_std(map, start)
end

#@
#
#@a
#         @abce @abced 70
#    @abc
#@ab      @abcd 42,3,15
#
#    @abcd 42,3,11 bloccato perche` c gia` visitato
 
#(1, (8, 1, 3))
#d, node gkeys813
#[-1, 0, 1]
#testing 0 6 3
#checks 1 1
#new keys 3
#testing 4 4 3
#checks 4 0
#testing 5 10 3
#checks 28 0
#
#
#testing d steps=34 keys=1+2
#checks k=3 keys&k=3
#new keys 11
#Tuple[(14, 0, 3), (42, 3, 11)]
#
#
#3 => Dict(0 => (28, 2), 4 => (38, 7), 5 => (44, 31), 2 => (24, 0), 1 => (34, 3))
#1 => Dict(0 => (6, 1), 4 => (4, 4), 5 => (10, 28), 3 => (34, 3))

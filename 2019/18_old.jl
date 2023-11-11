using DataStructures

mutable struct Coordinate
    x::Int
    y::Int
    steps::Int
    fetched_keys::Int #BitSet()
end

function checkUpper(c::Char)
    if 65 <= codepoint(c) <= 90
        return true
    else
        return false
    end
end

function checkUpper(c::Int)
    if 65 <= c <= 90
        return true
    else
        return false
    end
end

function checkLower(c::Int)
    if 97 <= c <= 122
        return true
    else
        return false
    end
end

function readMap(filename)
    lines = open(filename) do f
        [l for l in readlines(f)]
    end
    
    dungeon = Dict{Tuple{Int, Int}, Int}()
    start = Coordinate(0, 0, 0, 0)
    theKeys = Dict{Char, Coordinate}()
    
    for (y, l) in enumerate(lines)
        for (x, c) in enumerate(l)
            if c == '#'
                dungeon[(x-1,y-1)] = 1
            elseif c == '.'
                dungeon[(x-1,y-1)] = 0
            elseif c == '@'
                start = Coordinate(x-1, y-1, 0, 0)
                dungeon[(x-1,y-1)] = 0
            else
                if !checkUpper(c)
                    theKeys[c] = Coordinate(x-1, y-1, 0, 2^(Int(codepoint(c))-97))
                end
                dungeon[(x-1,y-1)] = Int(codepoint(c))
            end
        end
    end
    return length(lines[1])-1, length(lines)-1, dungeon, start, theKeys
end

function checkInMap(x::Int, y::Int, xmax::Int, ymax::Int)
    return 0 <= x <= xmax && 0 <= y <= ymax
end

function checkKey(x::Int, fetched::Int)
    #println("checkkey ", x, " ", fetched)
    if fetched & 2^x == 2^x
        return true
    else
        return false
    end
end

#b = 0          # The empty bitset :)
#b |= 1 << i    # Set
#b & 1 << i     # Test
#b &= ~(1 << i) # Reset
#b ^= 1 << i    # Flip i
#b = ~b         # Flip all


function BFS_by_key(xmax::Int, ymax::Int, dungeon,
                    start::Coordinate,
                    target::Coordinate)
    
    repeated = Set{Tuple}()
    dirX = (-1, 0, 0, 1)
    dirY = (0, -1, 1, 0)
    q = Vector{Coordinate}()
    push!(q, start)
    
    while !isempty(q)
        curr = popfirst!(q)
        #println(curr)
        auxFetched = curr.fetched_keys
        
        for i in 1:4
            x = curr.x + dirX[i]
            y = curr.y + dirY[i]

            if x == target.x && y == target.y
                return Coordinate(x, y, curr.steps + 1, auxFetched+2^(dungeon[(x,y)]-97))
            end
                        
            if (!checkInMap(curr.x, curr.y, xmax, ymax)) ||
                dungeon[(x, y)] == 1 || (x, y) in repeated
                continue
            end

            #if checkUpper(dungeon[(x, y)])
            #    println((x, y), dungeon[(x, y)], checkKey(dungeon[(x, y)]-65, auxFetched), auxFetched)
            #end
            if checkUpper(dungeon[(x, y)]) && !checkKey(dungeon[(x, y)]-65, auxFetched)
                continue
            end
            
            if checkLower(dungeon[(x, y)]) && !checkKey(dungeon[(x, y)]-97, auxFetched)
                auxFetched += 2^(dungeon[(x,y)]-97)
            end
            
            #println((x,y) in repeated)
            if !((x, y) in repeated)
                push!(q, Coordinate(x, y, curr.steps + 1, auxFetched))
                push!(repeated, (x, y))
            end
        end
    end
end

#function BFS(xmax::Int, ymax::Int,
#             dungeon, start::Coordinate, nkeys::Int)
#    #xmax = maximum([x[0] for x in dungeon.keys()])
#    #ymax = maximum([x[1] for x in dungeon.keys()])
#    
#    repeated = Set{Tuple}()
#    dirX = (-1, 0, 0, 1)
#    dirY = (0, -1, 1, 0)
#    q = Vector{Coordinate}()
#    #curr = Coordinate()
#    push!(q, start)
#    
#    while !isempty(q)
#        curr = popfirst!(q)
#        println(curr)
#        auxVisited = curr.visited
#        
#        if auxVisited == (2^nkeys)-1
#            return curr.steps
#        end
#        
#        for i in 1:4
#            x = curr.x + dirX[i]
#            y = curr.y + dirY[i]
#            
#            if (!checkInMap(curr.x, curr.y, xmax, ymax)) || dungeon[(x, y)] == 1 || (x, y, curr.visited) in repeated
#                continue
#            end
#
#            if checkUpper(dungeon[(x, y)]) && !checkKey(dungeon[(x, y)]-65, auxVisited)
#                continue
#            end
#            
#            if checkLower(dungeon[(x, y)])
#                auxVisited += 2^(dungeon[(x,y)]-97)
#            end
#            
#
#            if !((x, y, auxVisited) in repeated)
#                push!(q, Coordinate(x, y, curr.steps + 1, auxVisited))
#                push!(repeated, (x, y, auxVisited))
#            end
#            
#            #if str(dungeon[(x, y)]).islower():
#            #    auxVisited.remove(dungeon[(x, y)])
#        end
#    end
#end

function keyFromCoordinates(coord::Coordinate, theKeys::Dict{Char, Coordinate})
    for (k, v) in pairs(theKeys)
        if coord.x == v.x && coord.y == v.y
            return k
        end
    end

    return '@'
end

function run()
    xmax, ymax, dungeon, start, theKeys = readMap("input_18.txt")
    #proximity = Dict{Char, Vector{Tuple{Char, Int}}}()
    #proximity['@'] = Vector{Tuple{Char,

    paths = Dict{Char, Vector{Coordinate}}()#Vector{Vector{Coordinate}}()
    starts = [start]
    queue = collect(keys(theKeys))

    while length(starts) > 0
    #for i in 1:4
        new_starts = Vector{Coordinate}()
        
        for aStart in starts
            start_key = keyFromCoordinates(aStart, theKeys)
            println("start ", start_key)
            temp = Vector{Coordinate}()
            for q in queue
                println("queue ", q)
                if q == start_key
                    continue
                end
                coord = BFS_by_key(xmax, ymax, dungeon, aStart, theKeys[q])
                if !isnothing(coord)
                    println("found")
                    push!(temp, coord)
                    new_start = theKeys[q]
                    new_start.fetched_keys = coord.fetched_keys
                    if !haskey(paths, q)
                        push!(new_starts, new_start)
                    end
                    #println(new_start)
                end
            end
            if start_key == 'a'
                println("temp ", temp)
            end
            if isnothing(start_key)
                paths['@'] = temp
            else
                paths[start_key] = temp
            end
            #push!(paths, temp)
        end
        starts = new_starts
    end

    for (k, v) in pairs(paths)
        for c in v
            println(k, " ", keyFromCoordinates(c, theKeys), c.steps)
        end
    end

    
end

run()

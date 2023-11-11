
function findcubic(input, x, y)
    r = x*x + 3*x + 2*x*y + y + y*y + input
    bin = string(r, base=2)
    c = count(c->c=='1', bin)
    if c%2 == 0
        return 0
    else
        return 1
    end
end

function draw(target, visited, room)
    path = [target]
    prec = target
    while true
        if !isnothing(visited[prec][1])
            push!(path, visited[prec][1])
            prec = visited[prec][1]
        else
            break
        end 
    end

    for y in 0:45
        for x in 0:45
            if haskey(room, (x, y))
                if (x, y) in path
                    printstyled("O"; color= :red)
                elseif room[(x, y)] == 0
                    print(".")
                else
                    print("#")
                end
            else
                print(" ")
            end
        end
        println()
    end
    println()
end

function minpath(part=1)
    input = 1362
    start = (1, 1)
    target = (31, 39)
    visited = Dict()
    steps = 0
    current = Dict(start=>nothing)
    room = Dict((1,1)=>0)

    while true
        new_pos = Dict()
        for (c, prec) in current
            if haskey(visited, c)
                if visited[c][2] > steps
                    visited[c] = (prec, steps)
                end
            else
                visited[c] = (prec, steps)
                for s in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    pos = (c[1] + s[1], c[2] + s[2])
                    if pos[1]>= 0 && pos[2]>=0
                        if !haskey(room, pos)
                            room[(pos[1], pos[2])] = findcubic(input, pos...)
                        end
                        if room[(pos[1], pos[2])] != 1
                            if !haskey(new_pos, pos)
                                new_pos[pos] = c
                            end
                        end
                    end
                end
            end
        end
                    
        current = new_pos
        if haskey(visited, target)
            println("🎄 steps: $(visited[target][2])")
            draw(target, visited, room)
            break
        end
        steps += 1
        if part == 2 && steps == 51
            println("🎁🎄$(length(visited))")
            break
        end
    end
end

minpath()
minpath(2)

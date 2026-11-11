using MD5, DataStructures

function compress(selectors, dirs="UDLR")
    results = []
    i = 1
    # next = iterate(selectors)
    # while next !== nothing
    #     println(next)
    #     if next == 1
    #         push!(results, dirs[i])
    #     end
    #     i += 1
    # end
    for (i, s) in enumerate(selectors)
        if s
            push!(results, dirs[i])
        end
    end

    return results
end

moves = Dict('U'=>(x, y)->(x, y - 1),
             'D'=>(x, y)->(x, y + 1),
             'L'=>(x, y)->(x - 1, y),
             'R'=>(x, y)->(x + 1, y))

function doors(path, input)
    results = []
    s = input * path
    #return (parse(Int, x, base=16) > 10 for x in bytes2hex(md5(s))[1:4])
    for x in bytes2hex(md5(s))[1:4]
        push!(results, parse(Int, x, base=16) > 10)
    end
    return results
end

function bfs(start, target, input)
    paths = []
    queue = Queue{Any}()
    enqueue!(queue, (start, [start], ""))
    while length(queue)>0
        (x, y), path, dirs = dequeue!(queue)
        for dir in compress(doors(dirs, input))
            next = moves[dir](x, y)
            nx, ny = next
            if !(0 <= nx < 4 && 0 <= ny < 4)
                continue
            elseif next == target
                push!(paths, dirs * dir)
            else
                enqueue!(queue, (next, path, dirs * dir))
            end
        end
    end
    return paths
end

function run()
    input = "vwbaicqe"

    paths = bfs((0, 0), (3, 3), input)
    println("🎄 $(paths[1])")
    println("🎁🎄 $(length(paths[end]))")
end

run()
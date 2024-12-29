dirs = Dict(0=>Complex(0, -1), 1=>Complex(1, 0), 2=>Complex(0, 1), 3=>Complex(-1, 0))

function loadInput(filename::String)
    lines = readlines(filename)
    starts = []
    map = Dict{Complex, Int}()
    for y in eachindex(lines)
        for x in eachindex(lines[y])
            if lines[y][x] == '.'
                map[Complex(x, y)] = 0
            elseif lines[y][x] == '0'
                push!(starts,  Complex(x, y))
                map[Complex(x, y)] = parse(Int, lines[y][x])
            else
                map[Complex(x, y)] = parse(Int, lines[y][x])
            end
        end
    end
    return map, starts
end
    
function part1(map, starts)
    score = 0
    for start in starts
        queue = [(start, 0)]
        visited = [start]
        pos = start
        while length(queue) > 0
            pos = pop!(queue)
            push!(visited, pos[1])
            if pos[2] == 9
                score += 1
            end

            for i in 0:3
                npos = pos[1] + dirs[i]
                if npos in keys(map) && !(npos in visited)
                    if (map[npos] - pos[2]) == 1
                        push!(queue, (npos, map[npos]))
                    end
                end
            end
        end
    end

    println("🎄 Part 1:  $(score)")
end

function part2(map, starts)
    rate = Dict{Complex, Int}()
    for start in starts
        queue = [(start, 0)]
        pos = start
        while length(queue) > 0
            pos = pop!(queue)
            if pos[2] == 9
                rate[pos[1]] = get(rate, pos[1], 0) + 1
            end
            for i in 0:3
                npos = pos[1] + dirs[i]
                if npos in keys(map)
                    if (map[npos] - pos[2]) == 1
                        push!(queue, (npos, map[npos]))
                    end
                end
            end
        end
    end

    println("🎄🎅 Part 2: $(sum(values(rate)))")
end

function main()
    title = "Day 10: Hoof It"
    sub = "❄ "^(length(title)÷2 + 2)
    
    println()
    println(" $title ")
    println(sub)
    
    inputs = loadInput("input_10.txt")
    @time part1(inputs...)
    @time part2(inputs...)
end

main()
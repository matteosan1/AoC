movements = Dict(0=>Complex(0, -1), 1=>Complex(1, 0),
                 2=>Complex(0, 1), 3=>Complex(-1, 0))

# FIXME OPTIMIZE PART 2 ????????

function loadInput(filename::String)
    lines = readlines(filename)

    area = Dict{Complex, Int}()
    start = nothing
    for y in eachindex(lines)
        for x in eachindex(lines[y])
            if lines[y][x] == '.'
                area[Complex(x, y)] = 0
            elseif lines[y][x] == '^'
                area[Complex(x, y)] = 0
                start = Complex(x, y)
            elseif lines[y][x] == '#'
                area[Complex(x, y)] = 1
            end
        end
    end
    return  area, start
end

function part1(area, start)
    face = 0
    pos = start
    distincts = Set([pos])
    try
        while true
            if area[pos + movements[face]] == 1
                face = (face + 1) % 4
            else
                pos += movements[face]
                push!(distincts, pos)
            end
        end
    catch
    end
    println("🎄 Part 1: $(length(distincts))")
    return distincts
end

function part2(area, start, path)
    blocks = []
    delete!(path, start)
    for p in path
        if p in blocks
            continue
        end
        area[p] = 1
        face = 0
        pos = start
        turns = Set([])
        isloop = false
        try
            while true
                if area[pos+movements[face]] == 1
                    face = (face+1)%4
                    if (pos, face) in turns
                        isloop = true
                        break
                    end
                    push!(turns, (pos, face))
                else
                    pos += movements[face]
                end
            end
        catch
        end

        if isloop
            push!(blocks, p)
        end
        area[p] = 0
    end
    println("🎄🎅 Part 2: $(length(blocks))")
end

function main()
    title = "Day 6: Guard Gallivant"
    sub = "❄ "^(length(title)÷2 + 2)

    println()
    println(" $title ")
    println(sub)

    inputs = loadInput("input_6.txt")

    @time path = part1(inputs...)

    # ENDC = "\033[0m"
    # BOLD = "\033[1m"
    # RED = "\033[0;31;40m"
    
    # for y in 1:130
    #     for x in 1:130
    #         if Complex(x, y) in path
    #             print(RED*"."*ENDC)
    #         elseif inputs[1][Complex(x, y)] == 0
    #             print(".")
    #         else
    #             print(BOLD*"#"*ENDC)
    #         end
    #     end
    # println("")
    # end
    
    @time part2(inputs..., path)
end

main()
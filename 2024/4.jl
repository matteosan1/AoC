ALL_DIRECTIONS = Dict(0=>Complex(0, 1), 1=>Complex(1, 1), 2=>Complex(1, 0),
                  3=>Complex(1, -1), 4=>Complex(0, -1), 5=>Complex(-1 ,-1),
                  6=>Complex(-1, 0), 7=>Complex(-1, 1))

diagonal_pairs = ((1, 3), (7, 5), (1, 7), (3, 5))

function loadInput(filename::String)
    lines = readlines(filename)
    xwords = Dict{Complex, Char}()
    for y in eachindex(lines)
        for x in eachindex(lines[y])
            xwords[Complex(x, y)] = lines[y][x]
        end
    end
    return xwords
end

function find_word(xwords, pos, dir, word)
    all(get(xwords, pos + (i-1)*dir, ' ') == word[i] for i in eachindex(word))
end

function part1(xwords, word="XMAS")
    occurrencies = 0
    for pos in keys(xwords)
        if xwords[pos] == word[1]
            for dir in values(ALL_DIRECTIONS)
                occurrencies += Int(find_word(xwords, pos, dir, word))                    
            end
        end
    end
    println("🎄 Part 1: $occurrencies")
end

function part2(xwords, word="MAS")
    occurrencies = 0
    for mid_pos in keys(xwords) 
        if xwords[mid_pos] == word[2] 
            for (dir1, dir2) in diagonal_pairs
                occurrencies += find_word(xwords, mid_pos-ALL_DIRECTIONS[dir1], ALL_DIRECTIONS[dir1], word) && 
                                find_word(xwords, mid_pos-ALL_DIRECTIONS[dir2], ALL_DIRECTIONS[dir2], word)
            end
        end
    end
    println("🎄🎅 Part 2: $occurrencies")
end

function main()
    title = "Day 4: Ceres Search"
    sub = "❄ " ^(length(title) ÷ 2 + 2)

    println()
    println(" $title ")
    println(sub)

    inputs = loadInput("input_4.txt")

    @time part1(inputs)
    @time part2(inputs)
end

main()
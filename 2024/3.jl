function loadInput(filename::String)
    readlines(filename)
end

function part1(memory)
    re = r"mul\((\d{1,3}),(\d{1,3})\)"
    tot = 0
    for mem in memory
        for match in eachmatch(re, mem)
            tot += prod(parse.(Int, match.captures))
        end
    end
    println("🎄 Part 1: $tot")
end

function part2(memory)
    re = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    enabled = true
    tot = 0
    for mem in memory
        for match in eachmatch(re, mem)
            m = match.match
            if m == "do()"
                enabled = true
            elseif m == "don't()"
                enabled = false
            else
                if enabled
                    tot += prod(parse.(Int, match.captures))
                end
            end
        end
    end
    println("🎄🎅 Part 2: $tot")
end

function main()
    title = "Day 3: Mull It Over"
    sub = "❄ " ^(length(title) ÷ 2 + 2)

    println()
    println(" $title ")
    println(sub)

    inputs = loadInput("input_3.txt")

    @time part1(inputs)
    @time part2(inputs)
end

main()

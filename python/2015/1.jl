function readFile(part=1)
    f = open("instructions1a.txt", "r")
    lines = readlines(f)

    floor = 0
    for (i, l) in enumerate(lines[1])
        #println(l)
        if l == '('
            floor = floor + 1
        elseif l == ')'
            floor = floor - 1
        end
        if part == 2
            if floor == -1
                println("🎅 ", i)
                exit()
            end
        end
    end

    println("🎄", floor)
end

readFile(1)
readFile(2)

function part1()
    f = open("instructions8a.txt", "r")
    lines = readlines(f)

    lines = [r"\xa8br\x8bjr\""]
    real_char = 0
    mem_char = 0
    for (il, l) in enumerate(lines)
        real_char += length(l)

        #l = replace(l, "\\" => "0")
        #l = replace(l, "\"" => "0")
        println(l)
        index = 1
        # while !isnothing(findnext(l, "\\x", index))
        #     index = findnext(l, "\\x", index)
        #     c = l[index[1]:index[2]+2]
        #     println(c)
        #     replace!(l, c, "0")
        #     index = index[2]+3
        # end
        mem_char += length(l)
    end

    println(mem_char)
    println(real_char)
end

part1()
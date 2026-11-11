function part1()
    f = open("instructions5a.txt", "r")
    lines = readlines(f)

    function vowels(s::String)
        v = "aeiou"
        return count(c->(c in v), s)
    end

    function bad_couples(s::String)
        coups = ["ab", "cd", "pq", "xy"]
        return sum(occursin.(coups, s))
    end

    function pairs(s::String)
        for i in 1:length(s)-1
            if s[i] == s[i+1]
                return true
            end
        end 

        return false
    end

    nice = 0
    for l in lines
        if bad_couples(l) == 0 && vowels(l) >= 3 && pairs(l)
            nice += 1
        end
    end

    println("🎅 $nice")
end

function part2()
    f = open("instructions5a.txt", "r")
    lines = readlines(f)

    function double_pairs(s::String)
        for ic in 1:length(s)-3
            pair = s[ic:ic+1]
            if occursin(pair, s[ic+2:end])
                return true
            end
        end

        return false
    end

    function pairs(s::String)
        for i in 1:length(s)-2
            if s[i] == s[i+2]
                return true
            end
        end 

        return false
    end

    nice = 0
    for (i,l) in enumerate(lines)
        if pairs(l) && double_pairs(l)
            nice += 1
        end
    end

    println("🎄 $nice")
end

part1()
part2()

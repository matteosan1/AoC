function part1()
    f = open("instructions3a.txt", "r")
    lines = readlines(f)

    pos = (0, 0)
    presents = Any[pos]
    for l in lines[1]
        if l == '>'
            pos = (pos[1] + 1, pos[2])
        elseif l == '<'
            pos = (pos[1] - 1, pos[2])
        elseif l == '^'
            pos = (pos[1], pos[2] + 1)
        elseif l == 'v'
            pos = (pos[1], pos[2] - 1)
        end
        a = length(findall(x->x==pos, presents))
        if a == 0
            push!(presents, pos)
        end
    end

    println("🎅 ", length(presents))
end

function part2()
    f = open("instructions3a.txt", "r")
    lines = readlines(f)

    index = 1
    pos = [(0, 0), (0, 0)]
    presents = Any[pos[1]]
    for l in lines[1]
        index += 1
        if index == 3
            index = 1
        end

        if l == '>'
            pos[index] = (pos[index][1] + 1, pos[index][2])
        elseif l == '<'
            pos[index] = (pos[index][1] - 1, pos[index][2])
        elseif l == '^'
            pos[index] = (pos[index][1], pos[index][2] + 1)
        elseif l == 'v'
            pos[index] = (pos[index][1], pos[index][2] - 1)
        end
        a = length(findall(x->x==pos[index], presents))
        if a == 0
            push!(presents, pos[index])
        end
    end

    println("🎄",  length(presents))
end

part1()
part2()

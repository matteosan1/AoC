include("utils.jl")
using .AoCUtils

function clean_data(lines)
    sides = []
    for l in lines
        if l != ""
            push!(sides, [parse(Int, strip(item)) for item in split(strip(l), " ") if item != ""])
        end
    end

    return sides
end

function impossible_triangle(lines)
    combs = [(1, 2, 3), (3, 1, 2), (2, 3, 1)]
    possible = 0
    for l in lines
        ok = true
        for c in combs
            if l[c[1]] + l[c[2]] <= l[c[3]]
                ok = false
                break
            end
        end
        if ok
            possible += 1
        end
    end

    println("🎅 $possible")
end

function column_triangle(lines)
    combs = [(0, 1, 2), (2, 0, 1), (1, 2, 0)]
    possible = 0
    for col in 1:3
        for il in 1:3:length(lines)
            ok = true
            for c in combs
                if lines[il+c[1]][col] + lines[il+c[2]][col] <= lines[il+c[3]][col]
                    ok = false
                    break
                end
            end
            if ok
                possible += 1
            end
        end
    end

    println("🎄 $possible")
end

lines = clean_data(readLines("input_3.txt"))
impossible_triangle(lines)
column_triangle(lines)
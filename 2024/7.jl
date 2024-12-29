function loadInput(filename::String)
    lines = readlines(filename)

    results = []
    operations = []
    for l in lines
        oper = parse.(Int, split(split(l, ": ")[2], " "))
        push!(operations, oper)
        push!(results, parse(Int, split(l, ": ")[1]))
    end
    return results, operations
end

function solve(result, total, oper, ri, ops)
    if result == total && ri == length(oper)
        return total
    elseif ri == length(oper)
        return 0
    elseif total > result
        return 0
    else
        res = solve(result, total + oper[ri+1], oper, ri+1, ops)
        if res == result
            return result
        end

        res = solve(result, total * oper[ri+1], oper, ri+1, ops)
        if result == res
            return result
        end

        if ops == 3
            return solve(result, parse(Int64, string(total) * string(oper[ri+1])), oper, ri+1, ops)
        else
            return 0
        end
    end
end

function part1(results, operations)
    println("🎄 Part 1:  $(sum(solve(results[i], operations[i][1], operations[i], 1, 1) for i in eachindex(results)))")
end

function part2(results, operations)
    println("🎄🎅 Part 2: $(sum(solve(results[i], operations[i][1], operations[i], 1, 3) for i in eachindex(results)))")
end

function main()
    title = "Day 7: Bridge Repair"
    sub = "❄ "^(length(title)÷2 + 2)

    println()
    println(" $title ")
    println(sub)

    inputs = loadInput("input_7.txt")

    @time part1(inputs...)
    @time part2(inputs...)
end

main()
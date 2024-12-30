
function loadInput(filename::String)::Tuple{Vector{Vector{Int8}}, Vector{Vector{Int8}}}
    lines = readlines(filename)

    locks::Vector{Vector{Int8}} = []
    key::Vector{Vector{Int8}} = []
    
    for l in 1:8:length(lines)
        if lines[l][1] == '#'
            temp = [0 for _ in eachindex(lines[l])]
            for i in l+1:l+6
                for j in eachindex(lines[i])
                    temp[j] += if lines[i][j] == '#' 1 else 0 end
                end
            end
            push!(locks, temp)
        else
            temp = [0 for _ in eachindex(lines[l])]
            for i in l+1:l+5
                for j in eachindex(lines[i])
                    temp[j] += if lines[i][j] == '#' 1 else 0 end
                end
            end
            push!(key, temp)
        end
    end
    return locks, key
end

function part1(locks::Vector{Vector{Int8}}, key::Vector{Vector{Int8}})
    matches = 0
    for lock in locks
        for k in key
            if all(x -> x <= 5, k+lock)
                matches += 1
            end
        end
    end
    println("🎄 Part 1: $(matches)")
end

function main()
    title = "Day 25: Code Chronicle"
    sub = "❄ "^(length(title)÷2 + 2)
    
    println()
    println(" $title ")
    println(sub)
    
    inputs = loadInput("input_25.txt")
    @time part1(inputs...)
end

main()
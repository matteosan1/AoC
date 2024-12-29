using Memoize, SparseArrays

function loadInput(filename::String)
    lines = readlines(filename)
    return parse.(Int, split(lines[1]))
end
    
@memoize function rules(s)
    if s == 0 return [1] end
    oom = trunc(Int, log10(s)+1)
    if oom != 0 && oom % 2 == 0
        s1 = s÷10^(oom/2)
        s2 = s - s1*10^(oom/2)
        return  [Int(s1), Int(s2)]
    else
        return  [Int(s*2024)]
    end
end

function optimized_blinking(vect, blinks)
    new_vect = SparseVector(Int[], Int[], 0, maximum(keys(vect))) 

    for _ in 1:blinks
        new_vect = SparseVector(
            vcat(keys(new_vect), [k for (k, _) in vect for s in rules(k)]...), 
            vcat(values(new_vect), [v for (k, v) in vect for s in rules(k)]...),
            length(new_vect) + length(vect) * length(rules(first(keys(vect)))) 
        )
    end

    return sum(values(new_vect))
end

function blinking(vect, blinks)
    for _ in 1:blinks
        new_vect = Dict{Int, Int}()
        for (stone, i) in vect
            s = rules(stone)
            for item in s
                new_vect[item] = get(new_vect, item, 0) + i
            end
        end
        vect = new_vect
    end
    return sum(values(vect))
end
  
function part1(stones)
    length = 0
    for stone in stones
        length += blinking(Dict(stone => 1), 25)
    end
    println("🎄 Part 1:  $(length)")
end

function part2(stones)
    length = 0
    for stone in stones
        length += optimized_blinking(Dict(stone => 1), 75)
    end
    println("🎄🎅 Part 2: $(length)")
end

function main()
    title = "Day 11: Plutonian Pebbles"
    sub = "❄ "^(length(title)÷2 + 2)
    
    println()
    println(" $title ")
    println(sub)
    
    inputs = loadInput("input_11.txt")
    @time part1(inputs)
    @time part2(inputs)
end

main()
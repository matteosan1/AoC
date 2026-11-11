include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "prova.txt"
    #filename = "input_14.txt"
    lines = readInput(filename)
    return lines
end

function part1(instructions)
    memory = Dict()
    current_mask = nothing
    for i in instructions
        if startswith(i, "mask")
            m = split(i, " = ")[end]
            current_mask = Dict()
            for (it, bit) in enumerate(m)
                if bit != 'X'
                    current_mask[it] = parse(Int, bit)
                end
            end
        else
            regexp = r"mem\[(\d+)\] = (\d+)"
            m = match(regexp, i)
            addr = parse(Int, m[1])
            value = digits(parse(Int, m[2]), base=2, pad=36) |> reverse
            for (k, v) in current_mask
                value[k] = v
            end
            memory[addr] = parse(Int, join(value), base=2)
        end
    end    
    println("🎄 Part 1: $(sum(values(memory)))")
end

function part2(instructions)
    memory = Dict()
    current_mask = []
    for i in instructions
        if startswith(i, "mask")
            m = split(i, " = ")[end]
            current_mask = [Dict()]
            for (it, bit) in enumerate(m)
                if bit != 'X'
                    for c in current_mask
                        c[it] = parse(Int, bit)
                    end
                else
                    new_mask = []
                    for c in current_mask
                        c[it] = 0
                        nm = deepcopy(c)
                        nm[it] = 1
                        push!(new_mask, nm)
                    end
                    append!(current_mask, new_mask)
                end
            end
            for c in current_mask
                println(c[1], " ", c[2])
            end
        # else
        #     regexp = r"mem\[(\d+)\] = (\d+)"
        #     m = match(regexp, i)
        #     addr = parse(Int, m[1])
        #     value = digits(parse(Int, m[2]), base=2, pad=36) |> reverse
        #     for (k, v) in current_mask
        #         value[k] = v
        #     end
        #     memory[addr] = parse(Int, join(value), base=2)
        end
    end    

    #println("🎄🎅 Part 2: $()")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 14         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
@time part1(inputs)
@time part2(inputs)

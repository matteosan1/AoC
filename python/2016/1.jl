include("utils.jl")
using .AoCUtils

function move(ins)
    pos::Complex = 0+0im
    direction::Complex = 0+1im
    records = []
    record = true
    
    for i in ins
        steps = parse(Int, i[2:length(i)])
        if i[1] == 'L'
            direction *= 1im
        else
            direction *= -1im
        end

        for s in 1:steps
            pos += direction
            if pos in records
                println("🎄Part 2: $(abs(real(pos)) + abs(imag(pos)))")
                record = false
            else
                if record
                    append!(records, pos)
                end
            end
        end
    end
    println("🎄Part 1: $(abs(real(pos)) + abs(imag(pos)))")
end

line = readSingleLine("input_1.txt")
move(split(line, ", "))


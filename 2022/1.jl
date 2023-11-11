include("utils.jl")
using .AoCUtils

function delta(inputs)
    c = 0
    for i in range(2, length(inputs))
        var = (inputs[i] - inputs[i-1])/inputs[i-1]
        if var > 0
            c = c + 1
        end
    end

    return c
end

function delta_rolling(inputs)
    ulim = Int64(length(inputs) - length(inputs)%3+1)
    deltas = []
    for i in 2:ulim
        append!(deltas, inputs[i-1]+inputs[i]+inputs[i+1])
    end
    return delta(deltas)
end

function delta2(inputs)
    increases(x) = diff(x) .> 0
    return (inputs |> increases |> sum)
end

function delta_rolling2(input)
    windows(x, w) = [view(x, i:(i+w-1)) for i in 1:(length(x)-w+1)]
    increases(x) = diff(x) .> 0

    (windows(input, 3)
    |> x -> map(sum, x)
    |> increases
    |> sum)
end

lines = readInput("input_1.txt")
inputs = []
for i in 1:length(lines)
    append!(inputs, parse(Int64, lines[i]))
end

tstart = time()
println("🎄 Part 1: ", delta(inputs))
println("🎄 Part 2: ", delta_rolling(inputs))
println(time()-tstart)

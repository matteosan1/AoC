include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    function parse_bus((idx, bus))
        if bus != "x"
            return (offset=idx-1, id=parse(Int, bus))
        end
        return missing
    end

    filename = "input_13.txt"
    lines = readInput(filename)
    n = parse(Int, lines[1])
    bus_parts = split(lines[2], ",")
    parsed = parse_bus.(enumerate(bus_parts))
    return n, collect(skipmissing(parsed))
end

function part1(t0::Int, buses::Vector{NamedTuple{(:offset, :id), Tuple{Int64, Int64}}})
    depart, id = minimum(map(b -> (b.id - t0 % b.id, b.id), buses))
    println("🎄 Part 1: $(id*depart)")
end

function chineseremainder(n::Vector{Int}, a::Vector{Int})
    Π = prod(n)
    mod(sum(ai * invmod(Π ÷ ni, ni) * (Π ÷ ni) for (ni, ai) in zip(n, a)), Π)
end

function part2(buses::Vector{NamedTuple{(:offset, :id), Tuple{Int64, Int64}}})
    modulos = map(b -> b.id, buses)
    remainders = map(b -> b.id - b.offset, buses)
    crt = chineseremainder(modulos, remainders)

    println("🎄🎅 Part 2: $(crt)")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 13        ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

t0, buses = loadInput()
@time part1(t0, buses)
@time part2(buses)

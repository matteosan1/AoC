function loadInput(filename::String)
    lines = readlines(filename)

    antennas = Dict{Char, Vector{Complex}}()
    for y in eachindex(lines)
        for x in eachindex(lines[y])
            if lines[y][x] != '.' && lines[y][x] != '#'
                if haskey(antennas, lines[y][x])
                    push!(antennas[lines[y][x]], Complex(x, y))
                else
                    antennas[lines[y][x]] = [Complex(x, y)]
                end
            end
        end
    end

    xmax = length(lines[1])
    ymax = length(lines)
    return antennas, xmax, ymax
end

function part1(antennas, xmax, ymax)
    antinodes = Set([])
    for poss in values(antennas)
        for i in 1:length(poss)-1
            for j in i+1:length(poss)
                dpos = poss[j] - poss[i]
                for c in [-1, 2]
                    an = poss[i]+c*dpos
                    if real(an) >= 1 && real(an) <= xmax && imag(an) >= 1 && imag(an) <= ymax
                        push!(antinodes, an)
                    end
                end
            end
        end
    end
    println("🎄 Part 1:  $(length(antinodes))")
end

function addNode(antinodes, pos, dp, xmax, ymax)
    push!(antinodes, pos)
    c = 1
    while true
        np = pos + c*dp
        if real(np)<1 || real(np) > xmax || imag(np) < 1 || imag(np) > ymax
            break
        end
        push!(antinodes, np)
        c += 1
    end
end

function part2(antennas, xmax, ymax)
    antinodes = Set([])
    for poss in values(antennas)
        for i in 1:length(poss)-1
            for j in i+1:length(poss)
                addNode(antinodes, poss[i], poss[j] - poss[i], xmax, ymax)
                addNode(antinodes, poss[i], -poss[j] + poss[i], xmax, ymax)
            end
        end
    end
    println("🎄🎅 Part 2: $(length(antinodes))")
end

function main()
    title = "Day 8: Resonant Collinearity"
    sub = "❄ "^(length(title)÷2 + 2)

    println()
    println(" $title ")
    println(sub)

    inputs = loadInput("input_8.txt")

    @time part1(inputs...)
    @time part2(inputs...)
end

main()
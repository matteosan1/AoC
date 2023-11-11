function run()
    t = time()
    lines = open("input_3.txt") do f
        [parse(Int, l, base=2) for l in readlines(f)]
    end

    val = ratingCalc(lines, "oxy")
    val *= ratingCalc(lines, "co2")
    println("🎄🎅 Part 2: ", val)
    println(time()-t)
end

function mostCommon(col::Int, inputs::Vector{Int}, type::String)
    n = count([i & 2^col == 2^col for i in inputs])
    
    if type == "oxy"
        if n >= length(inputs)//2
            return 2^col
        else
            return 0
        end
    else
        if n < length(inputs)//2
            return 2^col
        else
            return 0
        end
    end
end

function ratingCalc(lines::Vector{Int}, t::String)
    rating = 0
    tmp_lines = lines
    col = 11
    while length(tmp_lines) > 1
        mc = mostCommon(col, tmp_lines, t)
        tmp_lines = [t for t in tmp_lines if t & 2^col == mc]
        col -= 1
    end
    
    return tmp_lines[1]
end

run()

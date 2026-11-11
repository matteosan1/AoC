function load(draws::Vector{Int8}, boards::Vector{Matrix{Int8}})
    f = open("input_4.txt")
    lines = readlines(f)
    i = 1
    while i < length(lines)
        if i == 1
            append!(draws, parse.(Int8, split(lines[i], ",")))
        elseif lines[i] != ""
            b = zeros(Int8, 5, 5)
            for j in 0:4
                b[:, j+1] .= parse.(Int8, split(lines[i+j]))
            end
            push!(boards, b)
            i += 4
        end
        i += 1
    end
end

function checkWin(checks::Vector{Matrix{Int8}})
    won = Int8[]
    for (i,c) in enumerate(checks)
        for x in 1:5
            if c[x, :] == ones(5) || c[:, x] == ones(5)
                push!(won, i)
                break
            end
        end
    end

    return won
end
        
function run(part::Int)
    draws = Int8[]
    boards = Matrix{Int8}[]
    load(draws, boards)
    checks = [zeros(Int8, 5, 5) for i in 1:length(boards)] 
    last = 0
    for d in draws
        for (i, b) in enumerate(boards)
            c = findall(x->x==d, b)
            if !isempty(c) > 0
                checks[i][c] .= 1
            end
        end
        
        won = checkWin(checks)
        for w in won
            last = sum(boards[w][checks[w].==0])*d
            if part == 1
                println(last)
                return
            end
        end
        deleteat!(checks, won)
        deleteat!(boards, won)
    end

    if part == 2
        println(last)
        return
    end
end

run(2)

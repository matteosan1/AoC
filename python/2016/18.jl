include("utils.jl")
using .AoCUtils

function safe(line, steps)
    c = count(c->c=='.', line)
    for s in 1:steps
        newline = ""
        for i in eachindex(line)
            if i == 1
                if (line[i] == '^' && line[i+1] == '^') || (line[i+1] == '^')
                    newline *= '^'
                else
                    newline *= '.'
                end
            elseif i == length(line)
                if (line[i] == '^' && line[i-1] == '^') || (line[i-1] == '^')
                    newline *= '^'
                else
                    newline *= '.'
                end
            else
                if (line[i] == '^' && line[i-1] == '^' && line[i+1] == '.') || 
                (line[i] == '^' && line[i-1] == '.' && line[i+1] == '^') ||
                (line[i-1] == '^' && line[i] == '.' && line[i+1] == '.') ||
                (line[i+1] == '^' && line[i] == '.' && line[i-1] == '.')
                    newline *= '^'
                else
                    newline *= '.'
                end
            end
        end
        c += count(c->c=='.', newline)
        line = newline
    end 
    println("🎁🎄 $c")
end

lines = readLines("input_18.txt")
safe(lines[1], 39)
safe(lines[1], 399999)


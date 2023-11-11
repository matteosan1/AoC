include("utils.jl")
using .AoCUtils

function removeJunk(line)
    new_line = ""
    i = 1
    while i <= length(line)
        if line[i] == '!'
            i += 2
        else
            new_line *= line[i]
            i += 1
        end
    end
    return new_line
end

function removeGarbage(line)
    new_line = ""
    i = 1
    ngarbage = 0
    while i <= length(line)
        if line[i] == '<'
            ngarbage += 1
            v = findfirst(c->c=='>', line[i:end])
            i += v
        else
            new_line *= line[i]
            i += 1
        end
    end
    println("🎁🎄 $(length(line) - length(new_line) - ngarbage*2)")
    return new_line
end

function findGroup(line, nest=0, score=0)
    i = 1
    while i <= length(line)
        if line[i] == '{'
            nest += 1
            off, nest, score = findGroup(line[i+1:end], nest, score)
            i += off
        elseif line[i] == '}'
            score += nest
            nest -= 1
            i += 1
            return i, nest, score
        else
            i += 1
        end
    end
    return i, nest, score
end
   
function run()
    lines = AoCUtils.readLines("input_9.txt")
    for l in lines
        l = removeGarbage(removeJunk(l))
        println("🎄 $(findGroup(l)[3])")
    end
end

run()
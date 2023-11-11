module AoCUtils

export readInput, readSingleLine, readLines

function readLines(filename)
    file = open(filename)
    lines = readlines(file)
    
    return lines
end

function readInput(filename)
    file = open(filename)
    lines = readlines(file)
    
    inputs = []
    for l in lines
        if l != ""
            append!(inputs, l)
        end
    end

    return inputs
end

function readSingleLine(filename)
    file = open(filename)
    line = readline(file)

    return line
end
end


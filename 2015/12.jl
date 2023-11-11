using JSON

function counter(obj, c, part)

    if typeof(obj) == Dict{String, Any}
        if part == 2 && "red" in values(obj)
            return c
        end
        for (k, v) in obj
            c = counter(v, c, part)
        end
    elseif typeof(obj) == Vector{Any}
        for i in obj
            c = counter(i, c, part)
        end 
    elseif typeof(obj) == String
        return c
    elseif typeof(obj) == Int64 
        c += obj
    end 

    return c 
end

function readFile(part)
    abacus = JSON.parsefile("instructions12a.txt")

    tot = counter(abacus, 0, part)

    if part == 1
        println("🎅 ", tot)
    else
        println("🎄 ", tot)
    end
end

readFile(1)
readFile(2)

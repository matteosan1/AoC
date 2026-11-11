include("utils.jl")
using .AoCUtils

register = Dict("a"=>0, "b"=>0, "c"=>0, "d"=>0)

function check_str2(a)
    return tryparse(Float64, a) !== nothing
end

function parseArg(arg)
    if check_str2(arg)
        return parse(Int, arg)
    else
        return register[arg]
    end
end

function compiler(lines)
    cline = 1
    while true
        l = lines[cline]
        if startswith(l, "cpy")
            args = split(l, " ")[2:end]
            register[args[2]] = parseArg(args[1])
            cline += 1
        elseif startswith(l, "inc")
            arg = split(l, " ")[end]
            register[arg] += 1
            cline += 1
        elseif startswith(l, "dec")
            arg = split(l, " ")[end]
            register[arg] -= 1
            cline += 1
        elseif startswith(l, "jnz")
            args = split(l, " ")[2:end]
            if parseArg(args[1]) != 0
                cline += parse(Int, args[2])
            else
                cline += 1
            end
        end
        #println(cline)
        if cline < 1 || cline >length(lines)
            break
        end
    end

    println("🎅 $(register["a"])")
end

lines = readLines("input_12.txt")

compiler(lines)
register["c"] = 1
compiler(lines)

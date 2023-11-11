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
    stdout = []
    N = 0
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
                cline += parseArg(args[2])
            else
                cline += 1
            end
        elseif startswith(l, "sum")
            args = split(l, " ")[2:end]
            register[args[1]] += parseArg(args[2])
            cline += 1
        elseif startswith(l, "fac")
            args = split(l, " ")[2:end]
            register[args[1]] = factorial(parseArg(args[2]))
            cline += 1
        elseif startswith(l, "mlt")
            args = split(l, " ")[2:end]
            register[args[1]] = parseArg(args[2]) * parseArg(args[3])
            cline += 1
        elseif startswith(l, "out")
            N += 1
            args = split(l, " ")[2:end]
            push!(stdout, parseArg(args[1]))
            if N == 10
                if all(stdout .== [0,1,0,1,0,1,0,1,0,1])
                    return true
                else
                    return false
                end
            end
            cline += 1    
        elseif startswith(l, "tgl")
            arg = parseArg(split(l, " ")[2])
            if  1 <= cline + arg <= length(lines)
                tgl_line = lines[cline + arg]
                if startswith(tgl_line, "tgl")
                    lines[cline + arg] = replace(tgl_line, "tgl"=>"inc")
                elseif startswith(tgl_line, "inc")
                    lines[cline + arg] = replace(tgl_line, "inc"=>"dec")
                elseif startswith(tgl_line, "dec")
                    lines[cline + arg] = replace(tgl_line, "dec"=>"inc")
                elseif startswith(tgl_line, "cpy")
                    lines[cline + arg] = replace(tgl_line, "cpy"=>"jnz")
                elseif startswith(tgl_line, "jnz")
                    lines[cline + arg] = replace(tgl_line, "jnz"=>"cpy")
                end
            end
            cline += 1
        end

        if cline < 1 || cline >length(lines)
            break
        end
    end

    println("🎅 $(register["a"])")
end

lines = AoCUtils.readLines("input_25.txt")
for i in 1:500
    register["a"] = i
    if compiler(lines)
        println("🎅🛷 $(i)")
        break
    end 
end

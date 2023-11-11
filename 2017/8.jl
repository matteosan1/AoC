include("utils.jl")
using .AoCUtils

import Base: ==, >=, <=, >, <

function check(r::Dict{String, Int}, label)
    if !haskey(r, label)
        r[label] = 0
    end
end 

function inc(r::Dict{String, Int}, label, val)
    check(r, label)
    r[label] += val
end

function dec(r::Dict{String, Int}, label, val)
    check(r, label)
    r[label] -= val
end

function ==(r::Dict{String, Int}, label, val)
    check(r, label)
    if r[label] == val
        return true
    end
    return false
end

function >=(r::Dict{String, Int}, label, val)
    check(r, label)
    if r[label] >= val
        return true
    end
    return false
end

function <=(r::Dict{String, Int}, label, val)
    check(r, label)
    if r[label] <= val
        return true
    end
    return false
end

function >(r::Dict{String, Int}, label, val)
    check(r, label)
    if r[label] > val
        return true
    end
    return false
end

function <(r::Dict{String, Int}, label, val)
    check(r, label)
    if r[label] < val
        return true
    end
    return false
end

function neq(r::Dict{String, Int}, label, val)
    check(r, label)
    if r[label] != val
        return true
    end
    return false
end

function test()
    max_val = 0
    lines = AoCUtils.readLines("input_8.txt")
    registry = Dict{String, Int}()

    for l in lines
        parts = split(l, " if ")
        cmd = split(parts[1])
        cond = split(parts[2])
        cond[2] = replace(cond[2], "!="=>"neq")

        operator = getfield(Main, Symbol(cond[2]))
        if operator(registry, cond[1], parse(Int, cond[3]))
            action = getfield(Main, Symbol(cmd[2]))
            action(registry, cmd[1], parse(Int, cmd[3]))
        end
        if maximum(values(registry)) > max_val
            max_val = maximum(values(registry))
        end
    end

    println("🎄 $(maximum(values(registry)))")
    println("🎁🎄 $(max_val)")
end

test()
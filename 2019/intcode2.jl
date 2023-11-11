module IntCodeUtils

using OffsetArrays
export IntCode, run

struct IntCode
    intcode::Dict{Int, Int}
    input::Vector{Int}
    output::Vector{Int}
    relative_base::Vector{Int}
    pointer::Vector{Int}
    isalive::Vector{Bool}
end

function IntCode(code::Dict{Int, Int})
    return IntCode(copy(code), Int[], Int[], [0], [0], [true])
end

function modeAndCode(value::Int)
    code = value % 100
    modes = [0, 0, 0]
    i = 2
    while 10^i < value
        modes[i-1] = (value ÷ 10^i) % 10
        i += 1
    end
    return code, modes 
end

function getval(i::IntCode, offset::Int, mode::Int)
    p = i.pointer[1] + offset
    if mode == 1
        return get(i.intcode, p, 0)
    elseif mode == 0
        return get(i.intcode, i.intcode[p], 0)
    else
        return get(i.intcode, i.intcode[p] + i.relative_base[1], 0)
    end
end

function passOutput(ints::Vector{IntCode})
    for (n, i) in enumerate(ints)
        if !isempty(i.output)
            to = n == 5 ? 1 : n + 1
            val = popfirst!(i.output)
            push!(ints[to].input, val)
        end
    end
end

function nic(ints::Vector{IntCode})
    for i in ints
        if length(i.output) >= 3
            addr = popfirst!(i.output)
            X = popfirst!(i.output)
            Y = popfirst!(i.output)
            if addr == 255
                println(Y)
                return true
            end
            push!(ints[addr+1], X)
            push!(ints[addr+1], Y)
        end
    end
    return false
end

function run(ints::Vector{IntCode}; debug::Bool=false, feedback::Bool=false, blocking=true)
    p1, p2, p3 = 0, 0, 0
    while any([i.isalive[1] for i in ints])
        for i in ints 
            if !i.isalive[1]
                continue
            end
            opcode, modes = modeAndCode(get(i.intcode, i.pointer[1], 0))
            if debug
                println(opcode, modes)
            end
            if opcode == 99
                i.isalive[1] = false
                continue
            elseif opcode == 1
                p1, p2 = Int[getval(i, offset, modes[offset]) for offset in 1:2]
                if modes[3] == 2
                    p3 = i.intcode[i.pointer[1]+3] + i.relative_base[1]
                else
                    p3 = i.intcode[i.pointer[1]+3]
                end 
                if debug
                    println("1. $(p1) $(p2) $(p3)")
                end
                i.intcode[p3] = p1 + p2
                i.pointer[1] += 4
            elseif opcode == 2
                p1, p2 = Int[getval(i, offset, modes[offset]) for offset in 1:2]
                if modes[3] == 2
                    p3 = i.intcode[i.pointer[1]+3] + i.relative_base[1]
                else
                    p3 = i.intcode[i.pointer[1]+3]
                end 
                if debug
                    println("2. $(p1) $(p2) $(p3)")
                end
                i.intcode[p3] = p1 * p2
                i.pointer[1] += 4
            elseif opcode == 3
                if modes[1] == 2
                    p1 = i.intcode[i.pointer[1]+1] + i.relative_base[1]
                else 
                    p1 = i.intcode[i.pointer[1]+1]
                end
                if isempty(i.input)
                    if !blocking
                        val = -1
                    else
                        continue
                    end
                else
                    val = popfirst!(i.input)
                end
                if debug
                    println("3. $(p1) $(val)")
                end
                i.intcode[p1] = val            
                i.pointer[1] += 2
            elseif opcode == 4
                p1 = getval(i, 1, modes[1])
                if debug
                    println("4. $(p1)")
                end
                push!(i.output, p1)
                i.pointer[1] += 2
            elseif opcode == 5
                p1, p2 = Int[getval(i, offset, modes[offset]) for offset in 1:2]
                if debug
                    println("5. $(p1) $(p2)")
                end
                if p1 != 0
                    i.pointer[1] = p2
                else
                    i.pointer[1] += 3
                end
            elseif opcode == 6
                p1, p2 = Int[getval(i, offset, modes[offset]) for offset in 1:2]
                if debug
                    println("6. $(p1) $(p2)")
                end
                if p1 == 0
                    i.pointer[1] = p2
                else
                    i.pointer[1] += 3
                end
            elseif opcode == 7
                p1, p2 = Int[getval(i, offset, modes[offset]) for offset in 1:2]
                if modes[3] == 2
                    p3 = i.intcode[i.pointer[1]+3] + i.relative_base[1]
                else
                    p3 = i.intcode[i.pointer[1]+3]
                end 
                if debug
                    println("7. $(p1) $(p2) $(p3)")
                end
                if p1 < p2
                    i.intcode[p3] = 1
                else
                    i.intcode[p3] = 0
                end
                i.pointer[1] += 4
            elseif opcode == 8
                p1, p2 = Int[getval(i, offset, modes[offset]) for offset in 1:2]
                if modes[3] == 2
                    p3 = i.intcode[i.pointer[1]+3] + i.relative_base[1]
                else
                    p3 = i.intcode[i.pointer[1]+3]
                end 
                if debug
                    println("8. $(p1) $(p2) $(p3)")
                end
                if p1 == p2
                    i.intcode[p3] = 1
                else
                    i.intcode[p3] = 0
                end
                i.pointer[1] += 4
            elseif opcode == 9
                p1 = getval(i, 1, modes[1]) 
                if debug
                    println("pointer: ", i.pointer[1]+1, " ", modes[1])
                    println("9. $(p1)")
                end
                i.relative_base[1] += p1
                i.pointer[1] += 2
            else
                throw(DomainError(opcode, "No valid opcode."))
            end
        end
        #if nic(ints)
        #    return
        #end
        if feedback
            passOutput(ints)
        end    
    end
end
end

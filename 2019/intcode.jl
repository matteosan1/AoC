module IntCodeUtils

using OffsetArrays
export IntCode, run

struct IntCode
    #intcode::OffsetVector{Int, Vector{Int}}
    intcode::Dict{Int, Int}
    input::Vector{Int}
    output::Vector{Int}
    multiprocess::Bool
    channel_in::Union{Nothing, Channel{Int}}
    channel_out::Union{Nothing, Channel{Int}}
    #pointer::Int
    relative_base::Vector{Int}
end

function IntCode(code::Dict{Int, Int}, multiprocess::Bool=false,
                 channel_in::Union{Nothing, Channel{Int}}=nothing, 
                 channel_out::Union{Nothing, Channel{Int}}=nothing)
    #intcode = Dict{Int, Int}()
    #for i in eachindex(code)
    #    intcode[i-1] = code[i]
    #end
    #intcode = OffsetVector(code, -1)
    return IntCode(code, Int[], Int[],
                   multiprocess, channel_in, channel_out, [0])
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

function getval(i::IntCode, p::Int, mode::Int)
    if mode == 1
        return get(i.intcode, p, 0)
    elseif mode == 0
        return get(i.intcode, i.intcode[p], 0)
    else
        return get(i.intcode, i.intcode[p] + i.relative_base[1], 0)
    end
end

function run(code::IntCode, debug::Bool=false, blocking=true)
    pointer = 0
    p1, p2, p3 = 0, 0, 0
    while true
        opcode, modes = modeAndCode(get(code.intcode, pointer, 0))
        #println(opcode, modes)
        if opcode == 99
            if code.multiprocess
                put!(code.channel_out, -99)
            end
            break
        elseif opcode == 1
            p1, p2 = Int[getval(code, pointer + i, modes[i]) for i in 1:2]
            if modes[3] == 2
                p3 = code.intcode[pointer+3] + code.relative_base[1]
            else
                p3 = code.intcode[pointer+3]
            end 
            if debug
                println("1. $(p1) $(p2) $(p3)")
            end
            code.intcode[p3] = p1 + p2
            pointer += 4
        elseif opcode == 2
            p1, p2 = Int[getval(code, pointer + i, modes[i]) for i in 1:2]
            if modes[3] == 2
                p3 = code.intcode[pointer+3] + code.relative_base[1]
            else
                p3 = code.intcode[pointer+3]
            end 
            if debug
                println("2. $(p1) $(p2) $(p3)")
            end
            code.intcode[p3] = p1 * p2
            pointer += 4
        elseif opcode == 3
            if modes[1] == 2
                p1 = code.intcode[pointer+1] + code.relative_base[1]
            else 
                p1 = code.intcode[pointer+1]
            end
            if code.multiprocess
                if !blocking 
                    if isready(code.channel_in)
                        val = take!(code.channel_in)
                    else
                        val = -1
                    end
                else
                    val = take!(code.channel_in)
                end
            else
                val = pop!(code.input)
            end 
            if debug
                println("3. $(p1) $(val)")
            end
            code.intcode[p1] = val            
            pointer += 2
        elseif opcode == 4
            p1 = getval(code, pointer + 1, modes[1])
            println("4. $(p1)")
            if code.multiprocess
                put!(code.channel_out, p1)
            end
            push!(code.output, p1)
            #println(p1)
            pointer += 2
        elseif opcode == 5
            p1, p2 = Int[getval(code, pointer + i, modes[i]) for i in 1:2]
            if debug
                println("5. $(p1) $(p2)")
            end
            if p1 != 0
                pointer = p2
            else
                pointer += 3
            end
        elseif opcode == 6
            p1, p2 = Int[getval(code, pointer + i, modes[i]) for i in 1:2]
            if debug
                println("6. $(p1) $(p2)")
            end
            if p1 == 0
                pointer = p2
            else
                pointer += 3
            end
        elseif opcode == 7
            p1, p2 = Int[getval(code, pointer + i, modes[i]) for i in 1:2]
            if modes[3] == 2
                p3 = code.intcode[pointer+3] + code.relative_base[1]
            else
                p3 = code.intcode[pointer+3]
            end 
            if debug
                println("7. $(p1) $(p2) $(p3)")
            end
            if p1 < p2
                code.intcode[p3] = 1
            else
                code.intcode[p3] = 0
            end
            pointer += 4
        elseif opcode == 8
            p1, p2 = Int[getval(code, pointer + i, modes[i]) for i in 1:2]
            if modes[3] == 2
                p3 = code.intcode[pointer+3] + code.relative_base[1]
            else
                p3 = code.intcode[pointer+3]
            end 
            if debug
                println("8. $(p1) $(p2) $(p3)")
            end
            if p1 == p2
                code.intcode[p3] = 1
            else
                code.intcode[p3] = 0
            end
            pointer += 4
        elseif opcode == 9
            p1 = getval(code, pointer + 1, modes[1]) 
            if debug
                println("pointer: ", pointer+1, " ", modes[1])
                println("9. $(p1)")
            end
            #println("relative base ", p1)
            code.relative_base[1] += p1
            pointer += 2
        else
            throw(DomainError(opcode, "No valid opcode."))
        end
    end
end
end

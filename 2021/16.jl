include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    lines = readInput("prova.txt")
    return lines[1]
end

function convertChar(msg, l, reminder)
    val = parse.(Int, msg[offset:offset+l-1], base=2)
    println(val)
    #reminder += 4 - length(bitstring(val))
    offset += l
    return val
end

function part1(msg)

    msg = bitstring.(parse.(Int, collect(msg), base=16))
    msg = join([m[end-3:end] for m in msg])

    offset = 1
    while true
        version = parse(Int, msg[offset:offset+2], base=2)
        offset += 3
        typ = parse(Int, msg[offset:offset+2], base=2)
        offset += 3
        bitlost = 2
        if typ == 4
            literal = ""
            n_subpkt = 0
            while true
                subtyp = msg[offset]
                offset += 1
                literal *= msg[offset:offset+3]
                offset += 4
                n_subpkt += 1
                if subtyp == '0'
                    println(parse(Int, literal, base=2))
                    break
                end
            end
            bitlost += 4 - (n_subpkt*5 % 4)
        else
            lenght_type = parse(Int, msg[offset], base=2)
            offset += 1
            bitlost += 3
            if lenght_type == 0
                subpkt_length = parse(Int, msg[offset:offset+14], base=2)
                offset += 15
                println(subpkt_length)
                bitlost += 1
                # lettura pacchetto
                offset += subpkt_length
                bitlost += (4 - (subpkt_length % 4))
            else 
                n_subpkt = parse(Int, msg[offset:offset+10], base=2)
                offset += 11
                for i in 1:n_subpkt
                    subpkt = parse(Int, msg[offset:offset+10], base=2)
                    offset += 11
                end
                bitlost += (4 - (11 % 4))*(n_subpkt+1)
            end
        end
        println(bitlost)
        offset += bitlost
        #delta = 4 - (bit_total % 4)
        println(offset, length(msg))
        if  offset > length(msg)
            break
        end
    end
end

msg = loadInput()
part1(msg)
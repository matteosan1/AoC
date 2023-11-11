include("utils.jl")
using .AoCUtils

function isless(a::Tuple{Char, Int}, b::Tuple{Char, Int}) 
    if a[2] < b[2] || (a[2] == b[2] && a[1] > b[1])
        return true
    else
        return false
    end
end

function real_rooms(lines)
    good_rooms = []
    tot = 0
    for l in lines
        letters = join(split(l, "-")[1:end-1], "")
        id = parse(Int, l[end-9:end-7])
        decoy = l[end-5:end-1]
        counts = Vector{Tuple}()
        for c in Set(letters)
            push!(counts, (c, count(x->x==c, letters)))
        end

        sort!(counts, rev=true)
        mydecoy = join([c[1] for c in counts[1:5]], "")
        if mydecoy == decoy
            push!(good_rooms, (l[1:end-11], id))
            tot += id
        end
    end
    println("🦌 $tot")

    for (room, id) in good_rooms
        new_room = ""
        for c in room
            if c != '-'
                new_room *= Char(((Int(codepoint(c)) - 97) + id)%26 + 97)
            else
                new_room *= " "
            end
        end
        if new_room == "northpole object storage"
            println("⛄ $(new_room): $id")
            return
        end
    end
end

lines = readLines("input_4.txt")
real_rooms(lines)
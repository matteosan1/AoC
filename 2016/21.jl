include("utils.jl")
using .AoCUtils
using Combinatorics
    
function scramble(lines, p)
    s = collect(p)
    for l in lines
        args = split(l)
        if startswith(l, "swap position")
            p1 = parse(Int, args[3]) + 1
            p2 = parse(Int, args[end]) + 1
            s[p1], s[p2] = s[p2], s[p1]
        elseif startswith(l, "swap letter")
            temp = join(s)
            s = collect(replace(replace(replace(temp, args[3]=>"*"), args[end]=>args[3]), "*"=>args[end]))
        elseif startswith(l, "reverse positions")
            p1 = parse(Int, args[3])+1
            p2 = parse(Int, args[end])+1
            s[p1:p2] = reverse(s[p1:p2])
        elseif startswith(l, "rotate based")
            idx = findfirst(c->c==only(args[end]), s)-1
            if idx >= 4
                idx += 2
            else
                idx += 1
            end
            s = circshift(s, idx)
        elseif startswith(l, "rotate")
            params = parse(Int, args[3])
            if args[2] == "left"
                s = circshift(s, -params)
            else
                s = circshift(s, params)
            end
        elseif startswith(l, "move")
            p1 = parse(Int, args[3])+1
            p2 = parse(Int, args[end])+1
            c = s[p1]
            deleteat!(s, p1)
            insert!(s, p2, c)
        end
    end
    return join(s)
end

function unscramble(lines)
    pwd = "fbgdceah"
    s = collect("abcdefgh")
    for p in permutations(s)
        scram = scramble(lines, p)
        if scram == pwd
            println("🎅🎄 $(join(p))")
            break
        end
    end
end

lines = readLines("input_21.txt")
s = "abcdefgh"
pwd = scramble(lines, s)
println("🎄 $(pwd)")
unscramble(lines)
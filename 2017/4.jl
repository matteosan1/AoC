include("utils.jl")
using .AoCUtils

using Combinatorics

function check(lines)
    c = 0
    for l in lines
        pwds = split(l)
        temp = Set(pwds)
        if length(pwds) == length(temp)
            c += 1
        end
    end

    println("🎄 $c")
end

function check2(lines)
    c = 0
    for l in lines
        pwds = split(l)
        temp = Set(pwds)
        if length(pwds) == length(temp)
            ok = true
            for pwd in pwds
                for c in permutations(pwd, length(pwd))
                    c = join(c)
                    if c == pwd
                        continue
                    end
                    if c in pwds
                        ok = false
                        break
                    end
                end
                if !ok
                    break
                end
            end
            if ok
                c += 1
            end
        end
    end

    println("🎄 $c")
end

lines = AoCUtils.readLines("input_4.txt")
check2(lines)
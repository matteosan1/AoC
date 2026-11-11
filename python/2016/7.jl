include("utils.jl")
using .AoCUtils

function lookForAbba(s)
    for i in 0:length(s)-4
        if s[i+1] == s[i+4] && s[i+2] == s[i+3]
            return true
        else
            return false
        end
    end
end

function abba(lines)
    tls = 0
    for l in lines
        ok = true
        idxo = findall("[", l)
        idxc = findall("]", l)
        for i in eachindex(idxo)
            if lookForAbba(l[idxo[i].start+1:idxc[i].start-1])
                ok = false
                break
            end
        end
        if !ok 
            continue
        end
        ok = false
        for i in 1:length(idxo)+1
            #println(i)
            if i == 1
                start = 1
                stop = idxo[i].start-1
            elseif i == length(idxo)+1
                start = idxc[end].start+1
                stop = length(l)
            else
                start = idxc[i-1].start+1
                stop = idxo[i].start-1
            end
            if lookForAbba(l[start:stop])
                ok = true
                break
            end
        end

        if ok
            tls += 1
        else
            println(l)
        end
    end

    println(tls)
end


lines = AoCUtils.readLines("input_7.txt")
abba(lines)
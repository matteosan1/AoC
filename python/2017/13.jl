include("utils.jl")
using .AoCUtils

function load_scanners()
    scanners = Dict()

    lines = AoCUtils.readLines("input_13.txt")
    for l in lines
        l = parse.(Int, split(l, ":"))
        scanners[l[1]] = l[2] - 1
    end

    return scanners
end

function part1(scanners)
    pos = Dict([k=>[0,1] for k in keys(scanners)])
    curLay = 0
    damage = 0
    for i in 0:maximum(keys(scanners))+1
        curLay = i
        if haskey(scanners, i) && pos[i][1] == 0
            damage += i*(scanners[i]+1)
            #print ("caught ", i, pos[i][0])
        end
        for (k, v) in pos
            if pos[k][1] == scanners[k]
                pos[k] = [scanners[k], -1]
            elseif pos[k][1] == 0
                pos[k] = [0,1]
            end
            pos[k][1] += pos[k][2]
        end
    end
    println("🎄 $(damage)")
end

function part2(scanners)
    function scannerPos(picos, r, delay)
        #println("num ", picos+delay+1)
        #println("den ", (r-1)*2)
        return (picos+delay+1)%(r*2)
    end
    
    delay = 0
    while true
        #print (delay)
        goon = false
        for i in sort(collect(keys(scanners)))
            if scannerPos(i, scanners[i], delay-1) == 0
                goon = true
                break
            end
        end
        if !goon
            break    
        end
        delay += 1
    end

    println("🎁🎄 $(delay)")
end

scanners = load_scanners()
part1(scanners)
part2(scanners)


function compute(input)
    curLoc = 0+0im
    numSteps = 1
    sz = 1
    left = 1
    curStep = 0
    curDir = 1im
    count = 1

    vals = Dict(curLoc=>count)
    while vals[curLoc] < input
        numSteps += 1
        curStep += 1
        curLoc += curDir
        if curStep == sz
            if left == 1
                left -= 1
                curDir *= 1im
            else
                left = 1
                curDir *= 1im
                sz += 1
            end
            curStep = 0
        end
        count += 1
        vals[curLoc] = count
    end

    println("🎄 $(abs(real(curLoc)) + abs(imag(curLoc)))")
end

function compute_v2(input)
    curLoc = 0+0im
    numSteps = 1
    sz = 1
    left = 1
    curStep = 0
    curDir = 1im
    last_s = 0

    vals = Dict(curLoc=>1)
    while vals[curLoc] <= input
        numSteps += 1
        curStep += 1
        curLoc += curDir
        if curStep == sz
            if left == 1
                left -= 1
                curDir *= 1im
            else
                left = 1
                curDir *= 1im
                sz += 1
            end
                
            curStep = 0
        end
        
        s = 0
        for p in Iterators.product([-1, 0, 1], [-1, 0, 1])
            if p == (0, 0)
                continue
            end
            coord = curLoc + complex(p...)
            if haskey(vals, coord)
                s += vals[coord]
            end
        end
        vals[curLoc] = s
        last_s = s
    end

    println("🎁🎄 $(last_s)")
end

input = 368078

compute(input)
compute_v2(input)
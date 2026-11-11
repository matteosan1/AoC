function checkHouses(h, goal::Int)
    i::Int = 1
    while true
        if h[i] >= goal
            println(i)
            break
        end
        i += 1
    end    
end

function presents(limit::Int, goal::Int)
    t = time()
    houses_a = [0 for i in 1:limit]
    houses_b = [0 for i in 1:limit]
    
    for elf in 1:limit
        for val in elf:elf:limit
            houses_a[val] += 10*elf
        end
        for val in elf:elf:(elf+1)*50
            if val > limit
                break
            end
            houses_b[val] += 11*elf
        end
    end
    
    checkHouses(houses_a, goal)
    checkHouses(houses_b, goal)
    #println(houses_a)
    println(time()-t)
end

const BIG_NUM = 1000000
const goal = 34000000

presents(BIG_NUM, goal)




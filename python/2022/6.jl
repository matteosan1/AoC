function run(part)
    ages = open("input_6.txt") do f
        parse.(Int16, split(readline(f), ","))
    end

    fishes = Dict(i=>0 for i in -1:8)
    for a in ages
        fishes[a] += 1
    end

    if part == 1
        days = 80
    else
        days = 256
    end
    
    for t in 1:days
        for i in 0:8
            fishes[i-1] = fishes[i]
        end
        fishes[8] = fishes[-1]
        fishes[6] += fishes[-1]
        fishes[-1] = 0
    end
    if part == 1
        println("🎄 $(sum(values(fishes)))")
    else
        println("🎄🎅 $(sum(values(fishes)))")
    end
end

run(1)
@time run(2)

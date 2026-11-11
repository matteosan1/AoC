function position(t, sectors, offset)
    return (t+offset)%sectors == 0
end

function run(discs)
    delay = 0
    while true
        state = [position(delay+i+1, s, o) for (i, (s,o)) in enumerate(discs)]
        delay += 1
        if all(state)
            println("🎁🎄 $delay")
            break
        end
    end
end

run([(17, 1), (7, 0), (19, 2), (5, 0), (3, 0), (13, 5)])
run([(17, 1), (7, 0), (19, 2), (5, 0), (3, 0), (13, 5), (11, 0)])
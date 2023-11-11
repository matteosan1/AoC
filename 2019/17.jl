function part1(step::Int, cycles, target)
    state = [0]
    idx = 0
    for i in 1:cycles
        mod = (idx+step)%length(state)+1
        idx = mod==0 ? length(state) : mod
        state = insert!(state, idx, i)
    end

    idx = findfirst(x->x==target, state)
    println("🎄 $(state[idx-3:idx+4])")
end

function part2(step::Int, cycles)
    # since 0 is always last it is enough to check who is first
    # in the sequence
    # also the first element will change every time 
    # (step + idx)%current_length == 0

    idx = 0
    val = 0
    for i in 1:cycles
        idx = (idx+step)%i + 1
        if idx == 1
            val = i
        end
    end
    println("🎁🎄 $(val)")
end

part1(382, 2017, 2017)
part2(382, 50000000)

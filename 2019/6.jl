function allocate(part=1)
    mems = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"

    banks = parse.(Int, split(mems))
    old = [banks]
    cycles = [0]
    size = length(banks)
    steps = 0
    last_new_bank = []
    while true
        start = findfirst(x->x==maximum(banks), banks)
        new_bank = copy(banks)
        offset = start
        for i in 1:banks[start]
            new_bank[start] -= 1
            offset += 1
            offset = offset%size==0 ? size : offset%size
            new_bank[offset] += 1
        end

        steps += 1
        if !(new_bank in old)
            push!(old, new_bank)
            push!(cycles, steps)
        else
            last_new_bank = new_bank
            break
        end
        banks = new_bank
    end

    if part == 1
        println("🎄 $(steps)")
    else
        idx = findfirst(x->x==last_new_bank, old)
        println("🎁🎄 $(steps-cycles[idx])")
    end
end

allocate()
allocate(2)
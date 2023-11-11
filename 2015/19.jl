function readInput()
    f = open("instructions19a.txt", "r")
    #f = open("prova.txt", "r")
    lines = readlines(f)

    reactions = Vector{Tuple{SubString, SubString}}()
    for l in lines[1:end-1]
        if l == ""
            continue
        end
        items = split(l, " => ")
        push!(reactions, (items[1], items[2]))
    end
    molecule = lines[end]

    return reactions, molecule
end

function calibration(m, reacts)
    mols = Set{String}()

    for r in reacts
        idx = findall(r[1], m)
        for i in idx
            new_m = m[1:i.start-1] * r[2] * m[i.stop+1:end]
            push!(mols, new_m)
        end
    end

    println("🎅 $(length(mols))")
end

reacts, m = readInput()
calibration(m, reacts)

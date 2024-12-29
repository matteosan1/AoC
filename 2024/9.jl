function loadInput(filename::String)
    return readlines(filename)[1]
end

function part1(disk)
    fragments = []
    try
        for i in 1:2:length(disk)
            append!(fragments, ((i-1)÷2)*ones(Int, parse(Int, disk[i])))
            append!(fragments, -1*ones(Int, parse(Int, disk[i+1])))
        end
    catch
    end

    idx_rvs = length(fragments)
    for idx in eachindex(fragments)
        if fragments[idx] == -1
            fragments[idx] = fragments[idx_rvs]
            fragments[idx_rvs] = -1
            idx_rvs -= 1
            while fragments[idx_rvs] == -1
                idx_rvs -= 1
            end
        end
        if idx == idx_rvs
            break
        end
    end
    checksum = sum([(i-1)*fragments[i] for i in 1:idx_rvs])
    println("🎄 Part 1:  $(checksum)")
end

mutable struct Fragment
    id::Int
    length::Int
end

function checksum(f::Fragment, idx::Int)
    return sum(f.id * (idx + i - 2) for i in 1:f.length)
end

function toString(f::Fragment)
    s = ""
    for _ in 1:f.length
        s *= if f.id == -1 "." else string(f.id) end
    end
    return s
end

function part2(disk::String)
    fragments = Vector{Fragment}()
    for i in eachindex(disk)
        id = if (i-1) % 2 == 0 ((i-1)÷2) else -1 end
        push!(fragments, Fragment(id, parse(Int, disk[i])))
    end
    #for f in fragments print(toString(f)) end
    i = length(fragments)
    while i > 0
        if fragments[i].id != -1 && fragments[i].length != 0
            j = 1
            while j <= length(fragments)
                if j == i break end
                if fragments[j].id == -1
                    if fragments[j].length >= fragments[i].length
                        if fragments[j].length > fragments[i].length
                            old_length = fragments[j].length
                            fragments[j].id = fragments[i].id
                            fragments[j].length = fragments[i].length
                            insert!(fragments, j + 1, Fragment(-1, old_length - fragments[i].length))
                            i += 1
                        else
                            fragments[j].id = fragments[i].id
                        end
                        fragments[i].id = -1
                        break
                    end
                end
                j += 1
            end
        end
        i -= 1
        #println()
        #for f in fragments print(toString(f)) end
    end

    c = 0
    j = 1
    for f in fragments
        if f.id != -1
            c += checksum(f, j)
        end
        j += f.length
    end
    println("🎄🎅 Part 2: $c")
end

function main()
    title = "Day 9: Disk Fragmenter"
    sub = "❄ "^(length(title)÷2 + 2)
    
    println()
    println(" $title ")
    println(sub)
    
    inputs = loadInput("input_9.txt")
    @time part1(inputs)
    @time part2(inputs)
end

main()
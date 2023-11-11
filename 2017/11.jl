include("utils.jl")
using .AoCUtils

function run()
    lines = AoCUtils.readLines("input_11.txt")
    dirs = split(lines[1], ",")

    move = Dict("s"=>a->(a[1], a[2]+1),
                "n"=>a->(a[1], a[2]-1),
                "se"=>a->a[1] % 2 == 0 ? (a[1]+1, a[2]) : (a[1]+1, a[2]+1),
                "sw"=>a->a[1] % 2 == 0 ? (a[1]-1, a[2]) : (a[1]-1, a[2]+1),
                "ne"=>a->a[1] % 2 == 0 ? (a[1]+1, a[2]-1) : (a[1]+1, a[2]),
                "nw"=>a->a[1] % 2 == 0 ? (a[1]-1, a[2]-1) : (a[1]-1, a[2]))

    max_dist = 0
    pos = (0,0)
    dist = 0
    for d in dirs
        pos = move[d](pos)
        dist = abs(pos[2]) + abs(pos[1]) - abs(pos[1]) ÷ 2
        if dist > max_dist
            max_dist = dist
        end
    end

    println("🎄 $(dist)")
    println("🎁🎄 $(max_dist)")
end

run()
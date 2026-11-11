include("utils.jl")
using .AoCUtils: readInput
using Plots

function loadInput()
    filename = "prova.txt"
    filename = "input_18.txt"
    lines = readInput(filename)
    cubes = []
    for l in lines
        push!(cubes, parse.(Int, split(l, ",")))
    end 
    #println(cubes)
    return cubes
end

function manhattan_distance(x, y)
    return sum(abs.(x .- y))
end

function find_surface(cubes)
    surface = 0
    for i in eachindex(cubes)
        faces = 6
        for j in eachindex(cubes)
            if i == j
                continue
            end
            if manhattan_distance(cubes[i], cubes[j]) == 1
                faces -= 1
            end
        end
        surface += faces
    end
    return surface
end

function part1(cubes)
    surface = find_surface(cubes)
    println("🎄 Part 1: $(surface)")
end

function part2(cubes, ext_surface)
    ext = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    trapped = 0
    ext_cub = Set([])
    for c in cubes
        for e in ext
            new_c = c .+ e
            if !(new_c in cubes)
                push!(ext_cub, new_c)
            end
        end
    end
    ext_cub = collect(ext_cub)

    trapped = []
    for i in eachindex(ext_cub)
        faces = 6
        for j in eachindex(cubes)
            delta = abs.(ext_cub[i] .- cubes[j])
            if 1 <= sum(delta) <= 2 && count(x->x==0, delta) == 2 
            #if manhattan_distance(ext_cub[i], cubes[j]) == 1
                faces -= 1
            end
        end
        if faces == 0
            println(ext_cub[i])
            push!(trapped, ext_cub[i])
        end
    end
    println(length(trapped))
    println(find_surface(trapped))

    x = [t[1] for t in trapped]
    y = [t[2] for t in trapped]
    z = [t[3] for t in trapped]
    scatter(x, y, z)

    #println("🎄🎅 Part 2: $()")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 18        ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

cubes = loadInput()
@time surface = part1(cubes)
@time part2(cubes, surface)

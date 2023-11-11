include("utils.jl")
using .AoCUtils
using Combinatorics

struct Particle
    n::Int
    p::Vector{Int}
    v::Vector{Int}
    a::Vector{Int}    
end

function modulo(p::Particle, type::String)
    if type == "a"
        return sqrt(p.a[1]^2 + p.a[2]^2 + p.a[3]^2)
    elseif type == "v"
        return sqrt(p.v[1]^2 + p.v[2]^2 + p.v[3]^2)
    else
        return sqrt(p.p[1]^2 + p.p[2]^2 + p.p[3]^2)
    end
end

function move(p::Particle)
    for i in 1:3
        p.v[i] += p.a[i]
        p.p[i] += p.v[i]
    end

    return p
end

function distance(p::Particle, type::String)
    distance::Int = 0
    for i in 1:3
        if type == "a"
            distance += abs(p.a[i])
        elseif type == "v"
            distance += abs(p.v[i])
        elseif type == "p"
            distance += abs(p.p[i])
        end
    end
    
    return distance
end

function load()
    particles = Vector{Particle}()
    lines = AoCUtils.readLines("input_20.txt")

    for (i, l) in enumerate(lines)
        parts = split(l, ">,")
        p = [parse(Int, x) for x in  split(parts[1][4:end], ",")]
        v = [parse(Int, x) for x in  split(parts[2][5:end], ",")]
        a = [parse(Int, x) for x in  split(parts[3][5:end-1], ",")]
        push!(particles, Particle(i-1, p, v, a))
    end

    part1_alt(particles)
    part2(particles)
end

function part1_alt(particles::Vector{Particle})
    sort!(particles, by=p->distance(p, "a"))
    println("🎄Part 1: $(particles[1].n)")
end

function part1(particles::Vector{Particle})
    for t in 1:1000
        for p in particles
            move(p)
        end
    end
    sort!(particles, by=p->distance(p, "p"))
    println("🎄Part 1: $(particles[1].n)")
end

function part2(particles::Vector{Particle})
    for t in 1:1000
        for p in particles
            move(p)
        end

        collide = []
        combinations_x = combinations([i for i in 1:length(particles)], 2)
        for c in combinations_x
            if (particles[c[1]].p == particles[c[2]].p)
                append!(collide, particles[c[1]].n)
                append!(collide, particles[c[2]].n)
            end            
        end

        if length(collide) > 0
            filter!(p->!(p.n in collide), particles)
        end
    end
    println("🎁🎄Part 2: $(length(particles))")
end

load()

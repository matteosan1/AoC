mutable struct Reindeer
    name::String
    speed::Int32
    energy::Int32
    recover::Int32
    km::Int32
    state::Int16
    points::Int32
end

function Reindeer(n, s, e, r)
    return Reindeer(n, s, e, r, 0, 0, 0)
end

function print(x::Reindeer)
    println(x.name, " - ", x.km, " - ", x.points)
end

function run(x::Reindeer)
    if x.state < 0
        x.state += 1
        if x.state == 0
            x.state = x.energy
        end
    else
        x.state -= 1
        x.km += x.speed
        if x.state == 0
            x.state = -x.recover
        end
    end
end

function scoring(reindeers::Vector{Reindeer})
    m = maximum([r.km for r in reindeers])
    indices = findall(x->x.km == m, reindeers)
    for i in indices
        reindeers[i].points += 1
    end

    return reindeers
end

function readInput()
    reindeers = Vector{Reindeer}()
    f = open("instructions14a.txt", "r")
    lines = readlines(f)
    for l in lines
        d = split(l, " ")
        r = Reindeer(d[1], parse(Int, d[4]), parse(Int, d[7]), parse(Int, d[end-1]))
        push!(reindeers, r)
        #println(reindeers[end])
    end       
    return reindeers
end

function part1(reindeers, time)    
    for t in 1:time+1
        for r in reindeers
            run(r)
        end 
    end 

    kms = maximum([r.km for r in reindeers])
    winner = findfirst(x->x.km==kms, reindeers)
    println("🎅 ", reindeers[winner])
end

function part2(reindeers, time)    
    for t in 1:time+1
        for r in reindeers
            run(r)
        end 
        reindeers = scoring(reindeers)
    end 
    
    for r in reindeers
        print(r)
    end
end

time = 100
r = readInput()
part1(r, time)
r = readInput()
part2(r, time)
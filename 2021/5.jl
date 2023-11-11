struct Point
    x::Int16
    y::Int16
end

struct Vent
    a::Point
    b::Point
    slope::Int64
end

function Vent(v::Vector{Tuple{Int16, Int16}})
    if v[1][1] <= v[2][1]
        a = Point(v[1][1], v[1][2])
        b = Point(v[2][1], v[2][2])
    else
        b = Point(v[1][1], v[1][2])
        a = Point(v[2][1], v[2][2])
    end
    
    if (v[1][1]-v[2][1]) == 0
        slope = 1e10
    else
        slope = (v[1][2]-v[2][2])//(v[1][1]-v[2][1])
    end

    if !(slope == 0 || slope == 1.0e10 || abs(slope) == 1)
        println(slope)
        println("Problema")
        exit()
    end
    
    Vent(a, b, slope)
end

function load(filename::String)
    transform(x) = [Tuple(parse.(Int16, i)) for i in split.(split(x, " -> "), ",")]
    vents::Vector{Vent} = open(filename) do f
        [transform(p) |> Vent for p in readlines(f)]
    end
end

function intersect(map::Matrix{Int8}, v::Vent)
    if v.slope == 0
        for x in v.a.x:v.b.x
            map[x+1, v.a.y+1] += 1
        end
    elseif v.slope == 1e10
        for y in min(min(v.a.y, v.b.y)):max(max(v.a.y, v.b.y))          
            map[v.a.x+1, y+1] += 1
        end
    else
        for (i, x) in enumerate(min(min(v.a.x, v.b.x)):max(max(v.a.x, v.b.x)))
            map[x+1, v.a.y+(i-1)*v.slope+1] += 1
        end
    end
end

function run(part)
    vents = load("input_5.txt")
    if part == 1
        filter!((v)->(abs(v.slope) != 1), vents)
    end
    
    xmax = max([v.b.x for v in vents]...)
    ymax = max([max(v.a.y, v.b.y) for v in vents]...)

    map = zeros(Int8, xmax+1, ymax+1)

    for v in vents
        p = intersect(map, v)
    end

    if part == 1
        println("🎄 $(count((i)->i>=2, map))")
    else
        println("🎄🎅 $(count((i)->i>=2, map))")
    end
end

run(1)

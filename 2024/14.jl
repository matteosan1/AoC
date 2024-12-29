using Statistics

function loadInput(filename::String)
    lines = readlines(filename)
    xmax, ymax = 101, 103
    #xmax, ymax = 11, 7

    robots = []
    vels = []
    for l in lines
        push!(robots, Complex(parse.(Int, split(split(split(l)[1], "=")[2], ","))...))
        push!(vels, Complex(parse.(Int, split(split(split(l)[2], "=")[2], ","))...))
    end
    return robots, vels, xmax, ymax
end
      
function quadrants(robots, xmax, ymax)
    quadrants = [0, 0, 0, 0]
    for r in robots
        if real(r) < xmax÷2
            if imag(r) < ymax÷2
                quadrants[1] += 1
            elseif imag(r) > ymax÷2
                quadrants[2] += 1
            end
        elseif real(r) > xmax÷2
            if imag(r) < ymax÷2
                quadrants[3] += 1
            elseif imag(r) > ymax÷2
                quadrants[4] += 1
            end
        end
    end
    return quadrants
end

function draw(ps, xmax, ymax)
    for y in 0:ymax-1
        for x in 0:xmax-1
            pos = Complex(x, y)
            if pos in ps
                print('X')
            else
                print('.')
            end
        end
        println("")
    end
end

# def mean_distance_to_centroid(robots, distance=manhattan_dist) -> float:
#     centroid = np.mean(robots)
#     return np.mean([distance(r, centroid) for r in robots])

# def part2_bis(robots, vels, xmax, ymax):
#     seconds = 10403 # found when the starting position is found again
#     minimum = (-1, float("inf"))
#     for second in range(1, seconds):
#         for i in range(len(robots)):
#             npos = complex(robots[i]+vels[i])
#             robots[i] = complex(npos.real%xmax, npos.imag%ymax)
#         dist = mean_distance_to_centroid(robots)
#         if dist < minimum[1]:
#             minimum = (second, dist)
#     print (f"🎄🎅 Part 2: {minimum}", end='')

function python_mod(x::Int, y::Int)
    if y == 0
        error("Division by zero")
    end
    r = x % y
    return r + (r < 0 && y > 0 ? y : 0)
end

function part1(robots, vels, xmax, ymax)
    for i in eachindex(robots)
        npos = robots[i] + vels[i]*100
        robots[i] = Complex(python_mod(Int(real(npos)), xmax), python_mod(Int(imag(npos)), ymax))
    end
    #draw(robots, xmax, ymax)
    μ = prod(quadrants(robots, xmax, ymax))
    println("🎄 Part 1:  $(μ)")
end

function part2(robots, vels, xmax, ymax)
    seconds = 10403 # found when the starting position is found again
    stds = (-1, Inf, Inf) 
    
    for second in 1:seconds
        for i in 1:length(robots)
            npos = robots[i] + vels[i]
            robots[i] = Complex(python_mod(Int(real(npos)), xmax), python_mod(Int(imag(npos)), ymax))
        end
    
        std_x = std(real.(robots))
        std_y = std(imag.(robots))
    
        if std_x <= stds[2] && std_y <= stds[3]
            stds = (second, std_x, std_y)
        end
    end
    println("🎄🎅 Part 2: $(stds[1])")    
end

function main()
    title = "Day 14: Restroom Redoubt"
    sub = "❄ "^(length(title)÷2 + 2)
    
    println()
    println(" $title ")
    println(sub)
    
    inputs = loadInput("input_14.txt")
    @time part1(inputs...)
    inputs = loadInput("input_14.txt")
    @time part2(inputs...)
end

main()
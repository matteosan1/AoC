dirs = Dict(0=>Complex(0, -1), 1=>Complex(1, 0), 2=>Complex(0, 1), 3=>Complex(-1, 0))

full_dirs = Dict(0 => 0im - 1im, 2 => 1 + 0im, 4 => 0im + 1im, 6 => -1 + 0im,
                       1 => 1 - 1im,  # NE 
                       3 => 1 + 1im,  # SE
                       5 => -1 + 1im, # SW
                       7 => -1 - 1im  # NW
                       ) 

function loadInput(filename::String)
    lines = readlines(filename)
    gardens = Dict{Complex, Char}()
    for y in eachindex(lines)
        for x in eachindex(lines[y])
            gardens[Complex(x, y)] = lines[y][x]
        end
    end
    get_regions(gardens)
end

function floodfill(gardens, pos, region, visited)
    if !(pos in visited)
        push!(visited, pos)
        push!(region, pos)
        for d in values(dirs)
            new_pos = pos + d
            if get(gardens, new_pos, ' ') == gardens[pos]
                floodfill(gardens, new_pos, region, visited)
            end
        end
    end
    region
end

function get_regions(gardens)
    visited = Set([])
    [floodfill(gardens, pos, Set([]), visited) for pos in keys(gardens) if !(pos in visited)]
end
  
function part1(regions)
    cost = 0
    for region in regions
        area = length(region)
        perimeter = 0
        for spot in region
            for d in values(dirs)
                perimeter += Int(!(spot+d in region))
            end
        end
        cost += area*perimeter
    end
    println("🎄 Part 1:  $(cost)")
end

function count_corners(pos, region, adjacent)
    for (i, d) in full_dirs
        if pos + d in region
            adjacent[i+1] = true 
        else
            adjacent[i+1] = false
        end
    end

    corners = 0

    if (!adjacent[1] && !adjacent[3] && !adjacent[5] && !adjacent[7]) corners += 4 end
        
    # pokey nodes (touches zone on just 1 side)
    if (adjacent[1] && !adjacent[3] && !adjacent[5] && !adjacent[7]) corners += 2 end
    if (adjacent[3] && !adjacent[1] && !adjacent[5] && !adjacent[7]) corners += 2 end
    if (adjacent[5] && !adjacent[3] && !adjacent[1] && !adjacent[7]) corners += 2 end
    if (adjacent[7] && !adjacent[3] && !adjacent[5] && !adjacent[1]) corners += 2 end

    # convex corners
    if (adjacent[5] && adjacent[3] && !adjacent[1] && !adjacent[7]) corners += 1 end
    if (adjacent[5] && adjacent[7] && !adjacent[1] && !adjacent[3]) corners += 1 end
    if (adjacent[1] && adjacent[3] && !adjacent[5] && !adjacent[7]) corners += 1 end
    if (adjacent[1] && adjacent[7] && !adjacent[5] && !adjacent[3]) corners += 1 end

    # concave corners
    if (adjacent[3] && adjacent[1]  && !adjacent[2]) corners += 1 end
    if (adjacent[3] && adjacent[5]  && !adjacent[4]) corners += 1 end
    if (adjacent[7] && adjacent[1]  && !adjacent[8]) corners += 1 end
    if (adjacent[7] && adjacent[5] && !adjacent[6]) corners +=1 end

    return corners
end

function part2(regions)
    cost = 0
    for region in regions
        area = length(region)
        perimeter = 0 
        adjacent = falses(8)
        for pos in region
            perimeter += count_corners(pos, region, adjacent)
        end
        cost += area * perimeter
    end
    println("🎄🎅 Part 2: $cost")
end

function main()
    title = "Day 12: Garden Groups"
    sub = "❄ "^(length(title)÷2 + 2)
    
    println()
    println(" $title ")
    println(sub)
    
    inputs = loadInput("input_12.txt")
    @time part1(inputs)
    @time part2(inputs)
end

main()
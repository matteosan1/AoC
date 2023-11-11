function read()
    instr = open("input_2.txt") do f
        [split(l) for l in readlines(f)]
    end

    return instr
end    
    

function drive_p1()
    horiz = 0
    depth = 0
    
    for l in read()
        if l[1] == "forward"
            horiz += parse(Int64, l[2])
        elseif l[1] == "down"
            depth += parse(Int64, l[2])
        elseif l[1] == "up"
            depth -= parse(Int64, l[2])
        end 
    end
    
    println("🎄 Part 1: ", horiz * depth)
end

function drive_p2()
    horiz = 0
    depth = 0
    aim = 0
            
    for l in read()
        if l[1] == "forward"
            horiz += parse(Int64, l[2])
            depth += aim * parse(Int64, l[2])
        elseif l[1] == "down"
            aim += parse(Int64, l[2])
        elseif l[1] == "up"
            aim -= parse(Int64, l[2])
        end 
    end
    println("🎄🎅 Part 2: ", horiz*depth)
end


drive_p1()
drive_p2()

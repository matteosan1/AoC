# Josephus Problem
# Numberphile https://www.youtube.com/watch?v=uCsD3ZGzMgE

function josephus(elves)
    b = reverse(join(digits(elves, base=2)))
    winner = parse(Int, b[2:end]*b[1], base=2)
    println("🎄 $winner")
end

function elvespresent(elves)
    i = 0
    while 3^(i+1) < elves
        i += 1
    end

    m = elves%(3^i)
    if m < 3^i  
        println("🎁🎄 $m")
    else
        println("🎁🎄 $(2*nelves - 3^(i+1))")
    end
end

elves = 3014603
josephus(elves)
elvespresent(elves)
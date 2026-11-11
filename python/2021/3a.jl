function Gamma()
    file = open("input_3.txt")
    lines = readlines(file)

    thrs = length(lines)/2
    gamma = zeros(12)
    for l in lines
        for (i, c) in enumerate(l)
            gamma[i] += parse(Int64, c)
        end
    end

    gamma_val = ""
    epsilon_val = ""
    for v in gamma
        if v > thrs
            gamma_val *= "1"
            epsilon_val *= "0"
        else
            gamma_val *= "0"
            epsilon_val *= "1"
        end
    end
    #println(gamma_val)
    #println(epsilon_val)

    gamma_val = parse(Int64, gamma_val; base=2)
    epsilon_val = parse(Int64, epsilon_val; base=2)

    println("🎄 Part 1: ", epsilon_val*gamma_val)
end

Gamma()

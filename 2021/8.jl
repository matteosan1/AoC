include("utils.jl")
using .AoCUtils

function part1()
    lines = AoCUtils.readInput("input_8.txt")

    codes = []
    numbers = []
    for l in lines
        t_codes, t_numbers = split(l, " | ")
        push!(codes, [join(sort(collect(t))) for t in split(t_codes)])
        push!(numbers, [join(sort(collect(t))) for t in split(t_numbers)])
    end

    c = 0
    for n in numbers
        for d in n
            if length(d) == 2 || length(d) == 4 || length(d) == 3 || length(d) == 7
                c += 1
            end
        end
    end
                
    println("🎄 Part 1: $(c)")
    return codes, numbers
end

function part2(codes, numbers)
    function diff(a, b)
        res = a
        for char in a
            if char in b
                res = replace(res, char=>"")
            end
        end

        return res
    end

    grand_tot = 0
    digit_map = Dict()
    for (nc, code) in enumerate(codes)
        mapping = Dict()
        nine_six = []
        last = []

        for c in code
            if length(c) == 2
                mapping[1] = c
            elseif length(c) == 4
                mapping[4] = c
            elseif length(c) == 7
                mapping[8] = c
            elseif length(c) == 3
                mapping[7] = c
            elseif length(c) == 6
                push!(nine_six, c)
            elseif length(c) == 5
                push!(last, c)
            end
        end

        digit_map[1] = diff(mapping[7], mapping[1])

        char = [diff(mapping[8], d) for d in nine_six]
        #print (char)
        for (ic, c) in enumerate(char)
            if c in mapping[1]
                digit_map[3] = c
                mapping[6] = nine_six[ic]
            elseif c in mapping[4]
                digit_map[4] = c
                mapping[0] = nine_six[ic]
            else
                digit_map[5] = c
                mapping[9] = nine_six[ic]
            end
        end
        
        #print (digit_map)
        #print (nine_six)
        
        five = diff(mapping[4], mapping[1])

        for l in last
            matches = 0
            for char in five
                if char in l
                    matches += 1
                end
            end
            if matches == 2
                mapping[5] = l
                filter!(x->x!=l, last)
                break
            end
        end
            
        if digit_map[5] in last[1]
            mapping[2] = last[1]
            mapping[3] = last[2]
        else
            mapping[3] = last[1]
            mapping[2] = last[2]
        end

        tot = 0
        for (i, n) in enumerate(numbers[nc])
            #print (n)
            for (k, v) in mapping
                #print (k, v)            
                if n == v
                    tot += k * 10**(3-i)
                end
            end
        end

        #print (tot)
        grand_tot += tot
        #break
    end
    #print (mapping)
    println("🎄🎅 Part 2: $(grand_tot)")
end

part2(part1()...)


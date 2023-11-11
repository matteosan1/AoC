using Combinatorics

function readInput()
    filename = "instructions24a.txt"
    f = open(filename, "r")
    return parse.(Int, readlines(f))
end

function solve(loads, parts=3)
    tot = sum(loads)/parts

    function hasSum(lst, sub)
       for y in range(1, length(lst))
            for x in (z for z in combinations(lst, y) if sum(z) == tot)
                if sub == 2
                    return true
                elseif sub < parts
                    return hasSum(symdiff(lst, x), sub - 1)
                elseif hasSum(symdiff(lst, x), sub - 1)
                    return reduce(*, x)
                end
            end
        end
    end
    println("🛷 $(hasSum(loads, parts))")
end

loads = readInput()
solve(loads)

solve(loads, 4)
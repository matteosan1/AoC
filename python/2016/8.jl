include("utils.jl")
using .AoCUtils

function printScreen(screen)
    s = size(screen)
    for y in 1:s[2]
        for x in 1:s[1]
            if screen[x, y] == 1
                print("#")
            else
                print(".")
            end
        end
        println("")
    end
end

function display(lines, x, y)
    screen = zeros(Int8, x, y)

    for l in lines
        if startswith(l, "rect")
            args = split(l, " ")[2]
            A, B = parse.(Int, split(args, "x"))
            screen[1:A, 1:B] .= 1
        elseif startswith(l, "rotate")
            args = split(l, " ")
            if args[2] == "row"
                row = parse(Int, split(args[3], "y=")[2]) + 1
                by = parse(Int, args[end])
                screen[:, row] = circshift(screen[:, row], by)
            elseif args[2] == "column"
                column = parse(Int, split(args[3], "x=")[2]) + 1
                by = parse(Int, args[end])
                screen[column, :] = circshift(screen[column, :], by)
            end
        end
    end
    printScreen(screen)
    println()
    println("🎅 $(sum(screen))")
end

lines = readLines("input_8.txt")
display(lines, 50, 6)

include("utils.jl")
using .AoCUtils

function code2(lines)
    digit_map = Dict{Tuple, Char}((-2, -3)=>'0', (-1, -3)=>'0', (0, -3)=>'0', (1, -3)=>'0', (2, -3)=>'0',
                                  (-2, -2)=>'0', (-1, -2)=>'0', (0, -2)=>'1', (1, -2)=>'0', (2, -2)=>'0',
                                  (-2, -1)=>'0', (-1, -1)=>'2', (0, -1)=>'3', (1, -1)=>'4', (2, -1)=>'0',
                                  (-3, 0) =>'0', (-2, 0) =>'5', (-1, 0)=>'6', (0, 0) =>'7', (1, 0) =>'8', (2, 0)=>'9', (3, 0)=>'0',
                                  (-2, 1) =>'0', (-1, 1) =>'A', (0, 1) =>'B', (1, 1) =>'C', (2, 1) =>'0',
                                  (-2, 2) =>'0', (-1, 2) =>'0', (0, 2) =>'D', (1, 2) =>'0', (2, 2) =>'0',
                                  (-2, 3) =>'0', (-1, 3) =>'0', (0, 3) =>'0', (1, 3) =>'0', (2, 3) =>'0')

    x::Int = -2
    y::Int = 0
    digits = ""
    for l in lines
        for c in l
            if c == 'U'
                if digit_map[(x, y-1)] != '0'
                    y -= 1
                end
            elseif c == 'D'
                if digit_map[(x, y+1)] != '0'
                    y += 1
                end
            elseif c == 'L'
                if digit_map[(x-1, y)] != '0'
                    x -= 1
                end
            elseif c == 'R'
                if digit_map[(x+1, y)] != '0'
                    x += 1                    
                end
            end
        end
        digits *= digit_map[(x, y)]
    end
    println("🎄Part 2: $digits")
end

function code(lines)
    digit_map = Dict{Tuple, Char}((1, 1)=>'5', (1, 0)=>'2', (1, 2)=>'8',
                                  (0, 1)=>'4', (0, 0)=>'1', (0, 2)=>'7',
                                  (2, 1)=>'6', (2, 0)=>'3', (2, 2)=>'9')

    x::Int = 1
    y::Int = 1
    digits = ""
    for l in lines
        for c in l
            if c == 'U'
                if y-1 >= 0
                    y -= 1
                end
            elseif c == 'D'                
                if y+1 <= 2
                    y += 1
                end
            elseif c == 'L'                
                if x-1 >= 0
                    x -= 1
                end
            elseif c == 'R'
                if x+1 <= 2
                    x += 1
                end
            end
        end
        digits *= digit_map[(x, y)]
    end
    println("🎄Part 1: $digits")
end

lines = readLines("input_2.txt")
code(lines)
code2(lines)

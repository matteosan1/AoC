include("utils.jl")
using .AoCUtils: readInput

#from utils import readInput, printTraj

function loadData()
    lines = readInput("input_17.txt")

    target_x = parse.(Int, split(split(split(lines[1], ",")[1], "x=")[2], ".."))
    target_y = parse.(Int, split(split(split(lines[2], ",")[1], "y=")[2], ".."))

    return target_x, target_y
end

function part1(target_x, target_y)
    good_vx = []
    for vx in 0:target_x[2]
        distance = 0
        record = ()
        for (s, i) in enumerate(vx:-1:0)
            distance += i
            if target_x[1] <= distance <= target_x[2]
                record = (s, 100000000)
            end
            if distance > target_x[2]
                if record != ()
                    record = (record[1], s)
                end
                break
            end
        end
        if record != ()
            push!(good_vx, (vx, record))
        end
    end

    println(good_vx)

    # good_vy = []
    # for vy in range(10000):
    #     distance = 0
    #     v = vy
    #     d_max_temp = 0
    #     for steps in range(1000):
    #         distance += v
    #         d_max_temp = max(distance, d_max_temp)
    #         v -= 1
    #         if target_y[0] <= distance <= target_y[1]:
    #             good_vy.append((vy, steps+1, d_max_temp))
    #             break

    # v = []
    # v0y = max(good_vy, key=lambda x: x[2])
    # print ("🎄 Part 1: {}".format(v0y[2]))
end

tgx, tgy = loadData()
part1(tgx, tgy)
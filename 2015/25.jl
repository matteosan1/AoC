
function code() 
    t_start = time()
    val::Int32 = 20151125
    x = [1, 1]
    final = [3075, 2981]
    ymax = 1
    n = 1
    while x != final
        if x[2] == 1
            x[2] = ymax + 1
            ymax = x[2]
            x[1] = 1
        else
            x[1] = x[1] + 1
            x[2] = x[2] - 1
        end
        n += 1
        val = (val * 252533) % 33554393
    end
    println(val)
    println(time() -t_start)
end

code()


function printLS(rst)
    for i in 1:length(rst)
        print(rst[i])
    end
    println()
end

function lookandsay(rst::Vector{Int})
    new_rst = Vector{Int}()
    c = 1
    for i in 1:length(rst)
        if i != length(rst) && rst[i] == rst[i+1]
            c += 1
        else
            push!(new_rst, c)
            push!(new_rst, rst[i])
            c = 1
        end
    end
    return new_rst
end

function lookandsayseq(n::Integer)
    tstart = time()
    init::String = "1321131112"
    rst = Vector{Int}()
    for i in 1:length(init)
        push!(rst, parse(Int, init[i]))
    end
    
    for i in 1:n
        rst = lookandsay(rst)
        if i == 40
            println(length(rst))
        end
    end
    tend = time()
    println(tend-tstart)
    return rst
end

println(length(lookandsayseq(50)))
#printLS(rst)


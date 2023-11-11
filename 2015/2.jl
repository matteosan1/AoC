function wrap()
    wrap = 0
    open("instructions2a.txt") do f
        for ln in eachline(f)
            (l, w, h) = parse.(Int, split(ln, "x"))
            wrap += 2*l*w + 2*l*h + 2*w*h + min(l*w, h*w, l*h)
        end
    end

    println(wrap)
end

function ribbon()
    ribbon = 0
    open("instructions2a.txt") do f
        for ln in eachline(f)
            (l, w, h) = parse.(Int, split(ln, "x"))
            ribbon += w*l*h + 2*min(l+w, h+w, l+h)
        end
    end

    println(ribbon)
end

wrap()
ribbon()
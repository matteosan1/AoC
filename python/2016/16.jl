
function checksum(a)
    csum = ""
    for i in 1:2:length(a)
        if a[i] == a[i+1]
            csum *= "1"
        else
            csum *= "0"
        end
    end

    if length(csum) % 2 == 0
        csum = checksum(csum)
    end

    return csum
end

function dojob(a, size)
    while length(a) < size
        b = replace(replace(replace(join(reverse(a)), "1"=>"2"), "0"=>"1"), "2"=>"0")
        a *= "0"*b
    end

    println("🎁🎄 $(checksum(a[1:size]))")
end

a = "11011110011011101"
dojob(a, 272)
dojob(a, 35651584)

using MD5

function bitcoin(leading=5) 
    key = "ckczppom"
    #key = "bgvyzdsv"
    solution = 0
    for i in 1:10000000
        a = bytes2hex(md5("$key$(lpad(i, 6, "0"))"))
        if a[1:leading] == lpad(0, leading, "0")
            solution = i
            break
        end
    end

    println("🎄",  solution)
end

bitcoin()
bitcoin(6)
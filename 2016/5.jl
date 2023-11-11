using MD5

function part1()
    pwd = ""
    input = "reyedfim"
    for i in 1:100000000
        hash = bytes2hex(md5(input*string(i)))
        #println(hash)
        if startswith(hash, "00000")
            pwd *= hash[6]
        end

        if length(pwd) == 8
            break
        end
    end

    println("🎅 $pwd")
end

function part2()
    pwd = ['-' for i in 1:8]
    input = "reyedfim"
    for i in 1:100000000
        hash = bytes2hex(md5(input*string(i)))
        
        if startswith(hash, "00000")
            if isnumeric(hash[6])
                idx = parse(Int, hash[6])
                if 0 <= idx <= 7 && pwd[idx+1] == '-'
                    println(hash[7])
                    pwd[idx+1] = hash[7]
                end
            end
        end

        if !any(x->x=='-', pwd)
            break
        end
    end

    println("⛄ $(join(pwd, ""))")
end

part1()
part2()
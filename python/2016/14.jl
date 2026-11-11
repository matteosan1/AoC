using MD5

function formKey(salt, i)
    return bytes2hex(md5(salt * string(i)))
end

function precomputeKeys(salt, N=30000)
    open("hashes.txt", "w") do io
        for i in 1:N
            key = bytes2hex(md5(salt * string(i)))
            for i in 1:2016
                key = bytes2hex(md5(key))
            end
            write(io, key*"\n")
        end
    end
end

function nextKeyBy5(c::Channel)
    reg5 = Regex("("*m[1]*")\\1{4,}")
    i = 0
    while i < 1000
        key = formKey(salt, idx+i)
        m = match(reg5, key)
        if !isnothing(m)
            return true
        end
        i += 1
    end

    return false
end

function findNext(salt, idx, m)
    reg5 = Regex("("*m[1]*")\\1{4,}")
    i = 0
    while i < 1000
        key = formKey(salt, idx+i)
        m = match(reg5, key)
        if !isnothing(m)
            return true
        end
        i += 1
    end

    return false
end
            
function part1(salt)
    idx = 0
    keys = []
    reg3 = r"([a-f0-9])\1{2,}"
    while true
        key = formKey(salt, idx)
        m = match(reg3, key)
        if !isnothing(m)
            if findNext(salt, idx+1, m.match)
               push!(keys, key)
            end
        end
        if length(keys) == 64
            println("🎄 $(keys[end]) $idx")
            break
        end
        idx += 1
    end
end

function part2(salt)
    if !isfile("hashes.txt")
        precomputeKeys(salt)
    end

    lines = []
    open("hashes.txt", "r") do io
        lines = readlines(io)
    end

    idx = 1
    keys = []
    reg3 = r"([a-f0-9])\1{2,}"

    while true
        key = lines[idx] #formKey(salt, idx)
        m = match(reg3, key)
        if !isnothing(m)
            reg5 = Regex("("*m[1]*")\\1{4,}")
            i = 0
            sublines = lines[idx+1:idx+1001]
            for l in sublines
                m = match(reg5, l)
                if !isnothing(m)
                    push!(keys, key)
                    break
                end
            end
        end
         if length(keys) == 64
            println("🎄 $(keys[end]) $idx")
            break
        end
        idx += 1
    end
end


salt = "jlmsuwbz"

part1(salt)
part2(salt)
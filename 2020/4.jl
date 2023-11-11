include("utils.jl")
using .AoCUtils: readInputWithBlank

function loadInput()
    filename = "input_4.txt"
    lines = readInputWithBlank(filename)
    passports = Vector{Dict{String, Any}}()
    temp = Dict()
    for l in lines
        if l == ""
            push!(passports, temp)
            temp = Dict{String, Any}()
        end
        for item in split(l)
            (k, v) = split(item, ":")
            temp[k] = v
        end
    end
    return passports
end

function checkFields(p::Dict{String, Any})
    ks = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all([k in keys(p) for k in ks])
        return true
    else
        return false
    end
end

function part1(passports::Vector{Dict{String, Any}})
    valid = 0
    for p in passports
        if checkFields(p)
            valid += 1
        end
    end
    println("🎄 Part 1: $(valid)")
end

function part2(passports::Vector{Dict{String, Any}})
    valid = 0
    for p in passports
        if !checkFields(p)
            continue
        end
        is_valid = true
        for (k, v) in p
            if haskey(p, k)
                if k == "byr"
                    val = parse(Int, v)
                    if val > 2002 || val < 1920
                        is_valid = false
                        break
                    end
                elseif k == "iyr"
                    val = parse(Int, v)
                    if val > 2020 || val < 2010
                        is_valid = false
                        break
                    end
                elseif k == "eyr"
                    val = parse(Int, v)
                    if val > 2030 || val < 2020
                        is_valid = false
                        break
                    end
                elseif k == "hgt"
                    if (v[end-1:end] != "cm" && v[end-1:end] != "in")
                        is_valid = false
                        break
                    else
                        val = parse(Int, v[1:end-2])
                        if v[end-1:end] == "in" && (val > 76 || val < 59)
                            is_valid = false
                            break
                        elseif v[end-1:end] == "cm" && (val > 193 || val < 150)
                            is_valid = false
                            break
                        end
                    end
                elseif k == "hcl"
                    if length(v) != 7 || isnothing(tryparse(Int, v[2:end], base=16))
                        is_valid = false
                        break
                    end
                elseif k == "ecl"
                    if !(v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
                        is_valid = false
                        break
                    end
                elseif k == "pid"
                    if (length(v) != 9) || isnothing(tryparse(Int, v))
                        is_valid = false
                        break
                    end
                end
            end
        end

        if is_valid
            valid +=1
        end
    end
    println("🎄🎅 Part 2: $(valid)")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 4         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
@time part1(inputs)
@time part2(inputs)

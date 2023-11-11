function part1()
    f = open("instructions7a.txt", "r")
    lines = readlines(f)

    vals = Dict{String, Int32}()
    isintstring(str) = all(isdigit(c) for c in str)

    while length(lines) != 0
        new_lines = String[]    
        for (il, l) in enumerate(lines)
            cmds = split(l, "->")
            lcmds = split(cmds[1])
            rcmds = split(cmds[2])

            #println(rcmds[1])
            try
                if length(lcmds) == 1
                    if isintstring(lcmds[1])
                        vals[rcmds[1]] = parse(Int32, lcmds[1])
                    else
                        vals[rcmds[1]] = vals[lcmds[1]]    
                    end
                elseif length(lcmds) == 2
                    if lcmds[1] == "NOT"
                        vals[rcmds[1]] = 65535 - vals[lcmds[2]]
                    end
                elseif length(lcmds) == 3
                    if lcmds[2] == "AND"
                        if isintstring(lcmds[1])
                            vals[rcmds[1]] = parse(Int32, lcmds[1]) & vals[lcmds[3]]
                        else
                            vals[rcmds[1]] = vals[lcmds[1]] & vals[lcmds[3]] 
                        end
                    elseif lcmds[2] == "OR"
                        if isintstring(lcmds[1])
                            vals[rcmds[1]] = parse(Int32, lcmds[1]) | vals[lcmds[3]]
                        else
                            vals[rcmds[1]] = vals[lcmds[1]] | vals[lcmds[3]]
                        end
                    elseif lcmds[2] == "LSHIFT"
                        vals[rcmds[1]] = vals[lcmds[1]] << parse(Int32, lcmds[3])
                    elseif lcmds[2] == "RSHIFT"
                        vals[rcmds[1]] = vals[lcmds[1]] >> parse(Int32, lcmds[3])
                    end
                end
            catch e
                push!(new_lines, l)
            end
        end
        lines = new_lines
    end
    println("🎅 ", vals["a"])
end

function part2()
    f = open("instructions7b.txt", "r")
    lines = readlines(f)

    vals = Dict{String, Int32}()
    isintstring(str) = all(isdigit(c) for c in str)

    while length(lines) != 0
        new_lines = String[]    
        for (il, l) in enumerate(lines)
            cmds = split(l, "->")
            lcmds = split(cmds[1])
            rcmds = split(cmds[2])

            #println(rcmds[1])
            try
                if length(lcmds) == 1
                    if isintstring(lcmds[1])
                        vals[rcmds[1]] = parse(Int32, lcmds[1])
                    else
                        vals[rcmds[1]] = vals[lcmds[1]]    
                    end
                elseif length(lcmds) == 2
                    if lcmds[1] == "NOT"
                        vals[rcmds[1]] = 65535 - vals[lcmds[2]]
                    end
                elseif length(lcmds) == 3
                    if lcmds[2] == "AND"
                        if isintstring(lcmds[1])
                            vals[rcmds[1]] = parse(Int32, lcmds[1]) & vals[lcmds[3]]
                        else
                            vals[rcmds[1]] = vals[lcmds[1]] & vals[lcmds[3]] 
                        end
                    elseif lcmds[2] == "OR"
                        if isintstring(lcmds[1])
                            vals[rcmds[1]] = parse(Int32, lcmds[1]) | vals[lcmds[3]]
                        else
                            vals[rcmds[1]] = vals[lcmds[1]] | vals[lcmds[3]]
                        end
                    elseif lcmds[2] == "LSHIFT"
                        vals[rcmds[1]] = vals[lcmds[1]] << parse(Int32, lcmds[3])
                    elseif lcmds[2] == "RSHIFT"
                        vals[rcmds[1]] = vals[lcmds[1]] >> parse(Int32, lcmds[3])
                    end
                end
            catch e
                push!(new_lines, l)
            end
        end
        lines = new_lines
    end
    println("🎅 ", vals["a"])
end

part1()
part2()
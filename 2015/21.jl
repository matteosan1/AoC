using Combinatorics

weapons = Dict{String, Vector{Int8}}(
    "Dagger"=>[8, 4],
    "Shortsword"=>[10, 5],
    "Warhammer"=>[25, 6],
    "Longsword"=>[40, 7],
    "Greataxe"=>[74, 8]
    )

armors = Dict{String, Vector{Int8}}(
    "Leather"=>[13, -1],
    "Chainmail"=>[31, -2],
    "Splintmail"=>[53, -3],
    "Bandedmail"=>[75, -4],
    "Platemail"=>[102, -5])

rings_p = Dict(
    "No ring"=>[0, 0],
    "Damage +1"=>[25, 1],
    "Damage +2"=>[50, 2],
    "Damage +3"=>[100, 3])

rings_m = Dict(
    "No ring"=>[0, 0],
    "Defense +1"=>[20, -1],
    "Defense +2"=>[40, -2],
    "Defense +3"=>[80, -3]
)

power_b = 109
damage_b = 8
armor_b = -2
hit_points = 100

function part1()
    res = []
    cost_min = 500
    choice = (nothing, nothing)
    rings_p_comb = collect(combinations(collect(keys(rings_p)), 2))
    push!(rings_p_comb, ["No ring", "No ring"])
    rings_m_comb = collect(combinations(collect(keys(rings_m)), 2))
    push!(rings_m_comb, ["No ring", "No ring"])

    for (k, v) in weapons
        for kr1 in rings_p_comb
            A = -(v[2]+rings_p[kr1[1]][2] + rings_p[kr1[2]][2]+armor_b)/power_b*hit_points + damage_b
            for (k1, v1) in armors
                no_ring1 = count(x->x=="No ring", kr1)
                for kr2 in rings_m_comb
                    no_ring2 = count(x->x=="No ring", kr2)
                    if no_ring2 + no_ring1 >= 2
                        if (v1[2] + rings_m[kr2[1]][2] + rings_m[kr2[2]][2]) < -A
                            cost = v[1] + rings_p[kr1[1]][1] + rings_p[kr1[2]][1] + v1[1] + rings_m[kr2[1]][1] + rings_m[kr2[2]][1]
                            if cost < cost_min
                                choice = (k, k1, kr1, kr2)
                                cost_min = cost
                            end
                        end
                    end
                end
            end
        end
    end

    println("🎅 $choice $cost_min")
end

function part2()
    function sim(choice, PP, PB, DB, AB)
        DP = weapons[choice[1]][2]
        AP = armors[choice[2]][2]
        ring1 = rings_p[choice[3][1]][2]
        ring2 = rings_p[choice[3][2]][2]
        ring3 = rings_m[choice[4][1]][2]
        ring4 = rings_m[choice[4][2]][2]

        while true
            PB -= max(1, DP + ring1 + ring2 + AB)
            if PB <= 0
                return true
            end
            PP -= max(1, DB + AP + ring3 + ring4)
            if PP <= 0
                return false
            end
        end
    end
    
    PB = 109
    DB = 8
    AB = -2
    PP = 100

    cost_max = 0
    choice = (nothing, nothing)
    rings_p_comb = collect(combinations(collect(keys(rings_p)), 2))
    push!(rings_p_comb, ["No ring", "No ring"])
    rings_m_comb = collect(combinations(collect(keys(rings_m)), 2))
    push!(rings_m_comb, ["No ring", "No ring"])

    for (ak, av) in armors
        for kr2 in rings_m_comb
            AP = av[2] + rings_m[kr2[1]][2] + rings_m[kr2[2]][2]
            no_ring1 = count(x->x=="No ring", kr2)       
            for (wk, wv) in weapons
                for kr1 in rings_p_comb
                    no_ring2 = count(x->x=="No ring", kr1)
                    if (no_ring2 + no_ring1) >= 2
                        DP = wv[2] + rings_p[kr1[1]][2] + rings_p[kr1[2]][2]
                        choice = (wk, ak, kr1, kr2)
                        if !sim(choice, PP, PB, DB, AB)
                            cost = wv[1]+rings_p[kr1[1]][1]+rings_p[kr1[2]][1]+av[1]+rings_m[kr2[1]][1]+rings_m[kr2[2]][1]
                            if cost > cost_max
                                println(choice, cost)
                                cost_max = cost
                            end
                        end
                    end
                end
            end
        end
    end
end

part1()   
part2() 

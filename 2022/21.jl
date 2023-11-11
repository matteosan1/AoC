include("../utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "input_21.txt"
    lines = readInput(filename)
    
    ingredients = String[]
    allergens = String[]
    recipes = Vector{Tuple{String, Vector{String}}}()
    real_recipes = Vector{Vector{String}}()
    for l in lines
        items = split(l, " (contains ")
        ingr = split(items[1])
        allgs = split(items[2][1:end-1], ", ")
        append!(ingredients, ingr)
        append!(allergens, allgs)
        push!(real_recipes, ingr)
        for a in allgs
            push!(recipes, (a, ingr))
        end
    end

    return unique(ingredients), unique(allergens), recipes, real_recipes
end

function part1(ingrs::Vector{String}, allgs::Vector{String},
               recipes::Vector{Tuple{String, Vector{String}}},
               real_recipes::Vector{Vector{String}})
    allgs_ingrs = Dict{String, Set{String}}()
    for a in allgs
        for (a1, i) in recipes
            if a == a1
                if haskey(allgs_ingrs, a)
                    intersect!(allgs_ingrs[a], Set(i))
                else
                    allgs_ingrs[a] = Set(i)
                end
            end
        end
    end
    
    while true
        removed = false
        for (a, i) in allgs_ingrs
            if length(i) == 1
                i = first(i)
                for (a1, i1) in allgs_ingrs
                    if a != a1 && i in i1
                        delete!(allgs_ingrs[a1], i)
                        removed = true
                    end
                end
            end
        end
 
        if !removed
            break
        end
    end

    mapped = [first(i) for i in values(allgs_ingrs)]
    not_mapped = setdiff(Set(ingrs), Set(mapped))

    val = 0
    for r in real_recipes
        for m in not_mapped
            if m in r
                val += 1
            end
        end
    end

    println("🎄 Part 1: $(val)")
    return allgs_ingrs
end

function part2(allgs_ingr::Dict{String, Set{String}})
    ing = [first(allgs_ingr[k]) for k in sort(collect(keys(allgs_ingr)))]
    println("🎄🎅 Part 2: $(join(ing, ","))")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 21        ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

ingrs, allgs, recipes, real_recipes = loadInput()
@time allgs_ingr = part1(ingrs, allgs, recipes, real_recipes)
@time part2(allgs_ingr)

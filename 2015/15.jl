using Combinatorics

struct Ingredient
    name::String
    properties::Vector{Int}
    capacity::Int
    durability::Int
    flavor::Int
    texture::Int
    calories::Int
end

function Ingredient(n, vals...)
    p = [v for v in vals]
    return Ingredient(n, p, vals...)
end

function readInput()
    ings = Vector{Ingredient}()
    f = open("instructions15a.txt", "r")
    #f = open("prova.txt", "r")
    lines = readlines(f)
    for l in lines
        println(l)
        items = split(l, ": ")
        name = items[1]
        subitems = split(items[2], ", ")
        vals = [parse(Int, x[2]) for x in split.(subitems, " ")]
        push!(ings, Ingredient(name, vals...))
    end       
    return ings
end

function recipe(partition, properties)
    scores = properties*partition
    if any(x->x<0, scores)
        return 0
    else 
        return reduce(*, properties*partition)
    end
end

function recipe2(partition, properties)
    scores = properties*partition
    if scores[end] != 500
        return 0
    end
    if any(x->x<0, scores)
        return 0
    else 
        return reduce(*, (properties*partition)[1:end-1])
    end
end

function check(ings::Vector{Ingredient}, N::Int, part=1, n_prop=4)
    props = [ings[i].properties[k] for k in 1:n_prop, i in 1:length(ings)]
    props = reshape(props, (n_prop, length(ings)))
    m = 0
    m_recipe = Nothing
    for p in partitions(N, length(ings))
        for c in permutations(p) 
            if part == 1
                score = recipe(c, props)
            else
                score = recipe2(c, props)
            end
            if score > m
                m = score
                m_recipe = c
            end
        end
    end
    
    println("🎅 $m $m_recipe")
end

ings = readInput()
check(ings, 100)
check(ings, 100, 2, 5)
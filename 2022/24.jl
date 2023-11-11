struct WithRepetitionsPermutations{T}
    a::T
    t::Int
end
 
with_repetitions_permutations(elements::T, len::Integer) where T =
    WithRepetitionsPermutations{T}(unique(elements), len)
 
Base.iteratorsize(::WithRepetitionsPermutations) = Base.HasLength()
Base.length(p::WithRepetitionsPermutations) = length(p.a) ^ p.t
Base.iteratoreltype(::WithRepetitionsPermutations) = Base.HasEltype()
Base.eltype(::WithRepetitionsPermutations{T}) where T = T
Base.start(p::WithRepetitionsPermutations) = ones(Int, p.t)
Base.done(p::WithRepetitionsPermutations, s::Vector{Int}) = s[end] > endof(p.a)
function Base.next(p::WithRepetitionsPermutations, s::Vector{Int})
    cur = p.a[s]
    s[1] += 1
    local i = 1
    while i < endof(s) && s[i] > length(p.a)
        s[i] = 1
        s[i+1] += 1
        i += 1
    end
    return cur, s
end

#=def ALU(prog, inputs):
v = {'w':0, 'x':0, 'y':0, 'z':0}
digit = 0

for line in prog:
    parts = line.split()
    cmd = parts[0]
    args = parts[1:]

    if cmd == "inp":
        v[args[0]] = inputs[digit]
        digit += 1
    elif cmd == "add":
        try:
            v[args[0]] += int(args[1])
        except ValueError:
            v[args[0]] += v[args[1]]
    elif cmd == "mul":
        try:
            v[args[0]] *= int(args[1])
        except ValueError:
            v[args[0]] *= v[args[1]]
    elif cmd == "div":
        try:
            v[args[0]] //= int(args[1])
        except ValueError:
            v[args[0]] //= v[args[1]]
    elif cmd == "mod":
        try:
            v[args[0]] %= int(args[1])
        except ValueError:
            v[args[0]] %= v[args[1]]
    elif cmd == "eql":
        try:
            val = int(args[1])
        except ValueError:
            val = v[args[1]]

        if args[0] == 'x' and val == -1:
            x = v[args[0]]
            if x >= 1 and x <= 9:
                v['w'] = x
                inputs[digit - 1] = x
                val = x
            else:
                return v, inputs

        v[args[0]] = 1 if v[args[0]] == val else 0
    else:
        raise Exception(f'Unknown cmd {cmd}')
return v, inputs


file = open("input_24.txt")
lines = readlines(file)
prog = []
for i in 1:length(lines)
    append!(prog, lines[i])
end

for i in product(range(9, 0, -1), repeat=7):
full_input = [i[0], i[1], i[2], i[3], -1, -1, i[4], -1, i[5], -1, i[6], -1, -1, -1]
res, inp = ALU(prog, full_input)

if res['z'] == 0 and -1 not in inp:
    print ("🎄 Part 1: {}".format("".join([str(i) for i in inp])))
    break

for i in product(range(1, 10), repeat=7):
full_input = [i[0], i[1], i[2], i[3], -1, -1, i[4], -1, i[5], -1, i[6], -1, -1, -1]
res, inp = ALU(prog, full_input)

if res['z'] == 0 and -1 not in inp:
    print ("🎄🎅 Part 2: {}".format("".join([str(i) for i in inp])))
    break
=#

with_repetitions_permutations(range(1, 3), 3)
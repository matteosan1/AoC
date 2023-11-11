include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "input_25.txt"
    lines = readInput(filename)

    return parse.(Int, lines)
end

function calc_loop_size(public_key::Int)
    subject_number = 7
    n = 1
    i = 0
    while true
        n = (n * subject_number) % 20201227
        if n == public_key
            return i+1
        end
        i += 1
    end
end

function calc_encryption_key(subject_number::Int, loop_size::Int)
    n = 1
    for i in 1:loop_size
        n = (n * subject_number) % 20201227
    end
    return n
end

function part1(public_key_card::Int, public_key_door::Int)
    loop_size = calc_loop_size(public_key_card)
    enc_key = calc_encryption_key(public_key_door, loop_size)

    println("🎄 Part 1: $(enc_key)")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 25        ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

public_key_card, public_key_door = loadInput()
@time part1(public_key_card, public_key_door)

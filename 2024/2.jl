using Combinatorics

function loadInput(filename::String)
    lines = readlines(filename)
    [parse.(Int64, split(l)) for l in lines]
end

function check_safe(diffs)
    if all(0 < d <= 3 for d in diffs) || all(-3 <= d < 0 for d in diffs)
        return true
    end
    false
end

function part1(reports::Vector{Vector{Int}})
    n = 0
    for report in reports
        n += check_safe([report[i]-report[i-1] for i in 2:length(report)])
    end
    println("🎄 Part 1: $n")
end

function problem_dampener(report)
    for c in combinations(report, length(report)-1)
        diffs = [c[i]-c[i-1] for i in 2:length(c)]
        if check_safe(diffs)
            return true
        end
    end
    false
end

function part2(reports)
    n = 0
    for report in reports
        diffs = [report[i]-report[i-1] for i in 2:length(report)]
        if check_safe(diffs) || problem_dampener(report)
            n += 1
        end
    end
    println("🎄🎅 Part 2: $n")
end

function main()
    title = "Day 2: Red-Nosed Reports"
    sub = "❄ " ^(length(title) ÷ 2 + 2)

    println()
    println(" $title ")
    println(sub)

    inputs = loadInput("input_2.txt")

    @time part1(inputs)
    @time part2(inputs)
end

main()

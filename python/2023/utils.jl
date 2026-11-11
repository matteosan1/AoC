module AoCUtils

using DataStructures

    export readInput, readInputWithBlank, readGrid, drawTextFromGrid

    function manhattan_distance(x::Complex{Int}, y::Complex{Int})
        return abs(real(x - y)) + abs(imag(x - y))
    end

    function readGrid(filename)
        lines = readInput(filename)
        grid = zeros(Int, length(lines[1]), length(lines))

        for y in eachindex(lines)
            for x in eachindex(lines[1])
                grid[x, y] = parse(Int, lines[y][x])
            end
        end

        return grid
    end

    function readInput(filename)
        file = open(filename)
        lines = readlines(file)
        
        inputs = []
        for l in lines
            if l != ""
                push!(inputs, l)
            end
        end

        return inputs
    end

    function readInputWithBlank(filename)
        file = open(filename)
        lines = readlines(file)
        
        inputs = []
        for l in lines
            push!(inputs, l)
        end

        return inputs
    end

    function drawTextFromGrid(grid::Vector{Int}, dims::Tuple{Int, Int}=nothing)
        if !isnothing(dims)
            grid = reshape(grid, dims[1], dims[2])
        end

        xmax, ymax = size(grid)
        for y in 1:ymax
            for x in 1:xmax
                if grid[x, y] == 0
                    print("▒")
                else
                    print("▓")
                end
            end
            println()
        end
    end

    function bfs(grid::Matrix{Int}, start::Tuple{Int, Int}, 
        goal::Tuple{Int, Int}, withtrack::Bool=false)
        starts = Vector{Tuple{Int, Int}}()
        push!(starts, start)
        return bfs(grid, starts, goal, withtrack)
    end

    function bfs(grid::Matrix{Int}, starts::Vector{Tuple{Int, Int}}, 
                 goal::Tuple{Int, Int}, withtrack::Bool=false)
        xmax, ymax = size(grid)
        shortest_visited = Inf*ones(Int, xmax, ymax)
        shortest_path_length = Inf
        queue = Queue{Tuple{Tuple{Int, Int}, Int}}()
        for s in starts
            enqueue!(queue, (s, 0))
        end
        
        while length(queue) > 0
            current_loc, steps = dequeue!(queue)
            next_steps = steps + 1
            x, y = current_loc
            shortest_visited[x, y] = steps
            if (x,y) == goal
                shortest_path_length = min(shortest_path_length, steps)
            end
            for (nx, ny) in ((x+1,y), (x-1,y), (x,y+1), (x,y-1))
                if (1 <= nx <= xmax && 1 <= ny <= ymax && grid[nx, ny] <= grid[x, y] + 1)
                    if shortest_visited[nx, ny] > next_steps
                        shortest_visited[nx, ny] = next_steps
                        enqueue!(queue, ((nx, ny), next_steps))
                    end
                end
            end
        end
        
        if withtrack
            return shortest_path_length, shortest_visited
        else
            return shortest_path_length
        end 
    end

    function getTrackFromBFS(track::Matrix{Float64}, start::Tuple{Int, Int}, goal::Tuple{Int, Int})
        path = [goal]
        pos = goal
        neighs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        xmax, ymax = size(track)
        while pos != start
            neis = [(pos[1] + n[1], pos[2] + n[2]) for n in neighs if 1 <= pos[1]+n[1] <= xmax && 1 <= pos[2]+n[2] <= ymax]
            p = nothing
            minimum = Inf
            for n in neis
                if n != path[end] && track[n[1], n[2]] < minimum
                    p = n
                    minimum = track[n[1], n[2]]
                end
            end 
            pos = p
            push!(path, p)
        end
        return path
    end    

end

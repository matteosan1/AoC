include("utils.jl")
using .AoCUtils: readInput

function loadInput()
    filename = "prova.txt"
    #filename = "input_17.txt"
    lines = readInput(filename)
    conway = Dict{NamedTuple{(:x, :y, :z), Tuple{Int64, Int64, Int64}}, Int}()

    z = 1
    for y in eachindex(lines)
        for x in eachindex(lines[1])
            if lines[y][x] == '#'
                conway[(x=x, y=y, z=z)] = 1
            end
        end
    end
    return conway
end

function part1(conway)
    for cycle in 1:6
    #     for ig, g in enumerate(grids):
#         for r in np.arange(g.shape[0]):
#             for c in np.arange(g.shape[1]):
#                 dz = (max(0, ig-1), min(ig+1, len(g)-1))
#                 xlim = (max(0, r), min(r+1, len(g.shape[0])-1))
#                 ylim = (max(0, c), min(c+1, len(g.shape[1])-1))
#                 temp = np.array(shape=(3,3,3))
    
#                 for x in dx:
#                 if z < 0 or x == g.shape[0]:
#                     continue
#                 for y in dy:
#                     if y < 0 or y == g.shape[1]:
#                         continue
#                     if x == y == z == 0:
#                         continue
    end

    #println("🎄 Part 1: $()")
end

function part2(inputs)

    #println("🎄🎅 Part 2: $()")
end

println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
println("⛄        Day 17         ⛄")
println("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

inputs = loadInput()
println(inputs)
@time part1(inputs)
@time part2(inputs)

# def printGrid(grids):
#     for ig, g in enumerate(grids):
#         print ("z={}".format(ig))
#         print (g)

# def reshape(grids):
#     grids.insert(0, np.zeros(shape=grids[0].shape))
#     grids.append(np.zeros(shape=grids[0].shape))

# # def checkEdges(grid):
# #     r = np.sum(grid[0, :, 0]) + np.sum(grid[-1, :, 0]) + np.sum(grid[-1, :, -1]) + np.sum(grid[0, :, -1]) + \
# #         np.sum(grid[:, 0, 0]) + np.sum(grid[:, -1, 0]) + np.sum(grid[:, -1, -1]) + np.sum(grid[:, 0, -1]) + \
# #         np.sum(grid[0, 0, :]) + np.sum(grid[-1, 0, :]) + np.sum(grid[-1, -1, :]) + np.sum(grid[0, -1, :])
# #     return r > 0

# def addDim(grid):
#     row = np.zeros((1, len(grid[0])))
#     col = np.zeros((grid.shape[1], 1))
#     grid = np.insert(grid, 0, row, axis=1)
#     grid = np.append(grid, col, axis=1)

#     row = np.zeros((1, len(grid[0])))
#     grid = np.insert(grid, 0, row, axis=0)
#     grid = np.append(grid, row, axis=0)
#     return grid

#     dx = np.arange(-1, 1, 1)
#     dy = np.arange(-1, 1, 1)
#     dz = np.arange(-1, 1, 1)
    
#     grids = [np.array(lines)]
#     reshape(grids)
#     #if checkEdges(grid):
#     #    grid = addDim(grid)
#     printGrid(grids)
    

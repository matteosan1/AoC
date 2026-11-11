from itertools import product
import heapq
from functools import reduce
import numpy as np

function knot_hash(s)
    # def rotate(l, pos, dir="left"):
    #     if dir == "right":
    #         l = l[-pos:] + l[:-pos]
    #     else:
    #         l = l[pos:] + l[:pos]
    #     return l
    lengths = [Int(char) for char in s]
    append!(lengths, [17, 31, 73, 47, 23])

    size = 256
    seq = collect(0:size-1)
    pos = 0
    skip = 0
    for round in 0:63
        for (i, l) in enumerate(lengths)
            seq = circshift(seq, -pos)#rotate(seq, pos, "left")
            seq = vcat(reverse(seq[1:l]), seq[l+1:end]) #)list(reversed(seq[:l])) + seq[l:]
            seq = circshift(seq, pos)#rotate(seq, pos, "right")
            pos += (l + skip)
            pos %= len(seq)
            skip += 1
        end
    end

    dense = [reduce((a,b)->a^b, seq[i:i+16]) for i in 0:16:length(seq)]
    hexa = "".join(['{0:0{1}x}'.format(c, 2) for c in dense])
    return "".join([bin(int(char, 16))[2:].zfill(4) for char in hexa])
end

function part1()
    size = 128
    cm = zeros(Int, size, size)
    root = "nbysizxe-"
    #root = "flqrgnkx-"
    for y in 0:size-1
        bin_hash = knot_hash(root+str(y))
        for (x, state) in enumerate(bin_hash)
            println(state)
            cm[x, y] = state
        end
    end

    println(sum(cm))
end
#print ("🎄Part 1: {}".format((cm==1).sum()))
#for y in range(size):
#    for x in range(size):
#        print ("{:2}".format(int(cm[x,y])), end='')
#    print ()
    
# visited = []
# groups = 0
# togo = []
# for p in product(range(size), repeat=2):
#     #print (p)
#     if p in visited:
#         continue
#     if cm[p[0], p[1]] != 0:
#         groups += 1
#         cm[p[0], p[1]] = groups
#         visited.append(p)
#         heapq.heappush(togo, p)
#         while togo != []:
#             coord = heapq.heappop(togo)
#             #print ("coord ", coord)
#             for dirs in [(0,1), (1,0), (0,-1), (-1,0)]:
#                 check = (coord[0]+dirs[0], coord[1]+dirs[1])
#                 if 0<=check[0]<size and 0<=check[1]<size:
#                     if check in visited:
#                         #print ("skip ", check)
#                         continue
#                     visited.append(check)
#                     if cm[ check[0], check[1]] != 0:
#                         #print ("check ", check)
#                         cm[check[0], check[1]] = groups
#                         heapq.heappush(togo, check)
    
# print ("🎁🎄Part 2: {}".format(groups))

# #for y in range(8):
# #    for x in range(8):
# #        if cm[x,y] == 0:
# #            print (".", end='')
# #        else:
# #            print ("{}".format(int(cm[x,y])), end='')
# #    print ()

import time
from utils import readInputWithBlank
import numpy as np

trans = [lambda x: x, 
         lambda x:np.rot90(x, 1),
         lambda x:np.rot90(x, 2),
         lambda x:np.rot90(x, 3),
         lambda x:np.flip(x, axis=1),
         lambda x:np.flip(x, axis=0),
         lambda x:np.rot90(np.flip(x, axis=1), 1),
         lambda x:np.rot90(np.flip(x, axis=1), 3)]

def loadInput():
    lines = readInputWithBlank("input_20.txt")
    tiles = {}
    tile = None
    id = None
    i = 0
    while i < len(lines):
        if lines[i].startswith("Tile"):
            id = int(lines[i][-5:-1])
            tile = np.zeros(shape=(10, 10))
            i += 1
        elif lines[i] == "" or i == len:
            tiles[id] = tile
            i += 1
        else:
            for y in range(10):
                for x in range(10):
                    if lines[i+y][x] == "#":
                        tile[x, y] = 1
            i += 10
    return tiles

def checkTile(tile, tile1, it, edge):
    if edge == 1 and all(tile[9, :] == trans[it](tile1)[0, :]):
        return True
    if edge == 3 and all(tile[0, :] == trans[it](tile1)[9, :]):
        return True
    if edge == 0 and all(tile[:, 0] == trans[it](tile1)[:, 9]):
        return True
    if edge == 2 and all(tile[:, 9] == trans[it](tile1)[:, 0]):
        return True
    return False

def drawTile(tile):
    lim = tile.shape[0]
    for y in range(lim):
        #if y != 0 and y % 10 == 0:
        #    print()        
        for x in range(lim):
            if tile[x, y] == 1:
                #if x != 0 and x % 10 == 0:
                #    print (" #", end='')
                #else:
                    print ("#", end='')                    
            else:
                #if x!= 0 and x % 10 == 0:
                #    print (" .", end='')
                #else:
                    print (".", end='')
        print()
    print()

def part1(tiles):
    image = {k:[0 for _ in range(4)] for k in tiles.keys()}
    start = list(tiles.keys())[0]
    fixed = [start]
    queue = [start]
    visited = []
    while len(queue) > 0:
        k = queue.pop()
        visited.append(k)
        for edge in range(4):
            found = False
            if image[k][edge] != 0:
                continue
            for k1 in tiles.keys():
                if k == k1:
                    continue
                if k1 in fixed:
                    if checkTile(tiles[k], tiles[k1], 0, edge):
                        image[k][edge] = k1
                        image[k1][(edge-2)%4] = k
                        found = True
                else:
                    for it in range(len(trans)):
                        if checkTile(tiles[k], tiles[k1], it, edge):
                            fixed.append(k1)
                            image[k][edge] = k1
                            image[k1][(edge-2)%4] = k
                            tiles[k1] = trans[it](tiles[k1])
                            found = True
                            break
                if found:
                    if k1 not in visited:
                        queue.append(k1)
                    break
    res = 1
    for k, v in image.items():
        if v.count(0) == 2:
           res *= k
    print ("🎄 Part 1: {}".format(res))

    size = int(np.sqrt(len(tiles)))
    for k, v in image.items():
        tiles[k] = tiles[k][1:9, 1:9]
        if v[0] == 0 and v[3] == 0:
            start = k
        
    tile = start
    block = []
    for y in range(size):
        temp = []
        for x in range(size):
            temp.append(tiles[tile])
            if x == size-1:
                block.append(temp)
                tile = start
                for i in range(y+1):
                    tile = image[tile][1]
            else:
                tile = image[tile][2]

    photo = np.block(block)
    #drawTile(photo)
    return photo

sea_monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

def part2(image):
    items = sea_monster.split("\n")
    sm = 2*np.ones(shape=(len(items[0]), len(items)))
    for y in range(len(items)):
        for x in range(len(items[0])):
            if items[y][x] == "#":
                sm[x, y] = 1

    footprint = len(sm[sm==1])
    size = image.shape
    monsters = 0
    for t in trans:
        image2 = t(image)
        for y in range(size[1] - sm.shape[1]):
            for x in range(size[0] - sm.shape[0]):
                diff = image2[x:x+sm.shape[0], y:y+sm.shape[1]] - sm
                if len(diff[diff==0]) == footprint:
                    monsters += 1

        if monsters > 0:
            print ("🎄🎅 Part 2: {}".format(len(image[image==1])-footprint*monsters))
            break


print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")
print("⛄        Day 20        ⛄")
print("⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄⛄")

tiles = loadInput()

t0 = time.time()
image = part1(tiles)
print ("Time: {:.5f}".format(time.time()-t0))

t0 = time.time()
part2(image)
print ("Time: {:.5f}".format(time.time()-t0))



import time, numpy as np

from utils import readInput

def loadInput():
    lines = readInput("input_8.txt")
    image = np.zeros(shape=(len(lines[0]),))
    nlayers = len(lines[0])//(25*6)
    for i, c in enumerate(lines[0]):
        image[i] = int(c)
    image = image.reshape(nlayers, 6, 25)
    return image

def part1(image):
    mins = (-1, float('inf'))
    for i in range(image.shape[0]):
        c = (image[i, :, :] == 0).sum()
        if c < mins[1]:
            mins = (i, c)
    print (f"ðŸŽ„ Part 1: {(image[mins[0], :, :] == 1).sum() * (image[mins[0], :, :] == 2).sum()}")

def show_image(image):
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if image[y, x] == 1:
                print ("X", end='')
            elif image[y, x] == 0:
                print (" ", end='')
        print ()
    
def part2(image):
    rendering = np.ones_like(image[0])*2
    for y in range(6):
        for x in range(25):
            for i in range(image.shape[0]):
                if image[i, y, x] != 2:
                    rendering[y, x] = image[i, y, x]
                    break
    print (f"ðŸŽ„ðŸŽ… Part 2:")
    show_image(rendering)

if __name__ == "__main__":
    title = "Day 8: Space Image Format"
    sub = "-"*(len(title)+2)

    print()
    print(f" {title} ")
    print(sub)
    
    inputs = loadInput()
    
    t0 = time.time()
    part1(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))
    
    t0 = time.time()
    part2(inputs)
    print ("Time: {:.5f}".format(time.time()-t0))

    

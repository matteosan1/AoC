pixels = []
with open("input8a.txt", "r") as f:
    line = f.readlines()

line = line[0].split("\n")[0]
for l in line:
    pixels.append(int(l))

#pixels = [1,2,3,4,5,6,7,8,9,0,1,2]
width = 25
heigth = 6

layer = 0
tot_pixel = 0
min_zero_pixel = 10000000000000
max_n1digit = 0
max_n2digit = 0
while tot_pixel != len(pixels):
    zero_pixel = 0
    n1digit = 0
    n2digit = 0
    for y in range(heigth):
        for x in range(width):
            pixel = pixels[x + y * width + layer * (width*heigth)]
            if pixel == 0:
                zero_pixel += 1
            elif pixel == 1:
                n1digit += 1
            elif pixel == 2:
                n2digit += 1
            tot_pixel += 1
    layer += 1
    if zero_pixel < min_zero_pixel:
        min_zero_pixel = zero_pixel
        max_n1digit = n1digit
        max_n2digit = n2digit

print (max_n1digit, max_n2digit, max_n1digit*max_n2digit)
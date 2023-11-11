import numpy as np
grid_sn = 9445

pls = np.zeros(shape=(301, 301))

for x in range(1, 301):
    for y in range(1, 301):
        rack_id = x + 10
        power_level = (rack_id*y + grid_sn)*rack_id
        power_level = (power_level / 100) % 10 - 5
        pls[x,y] = power_level

max_3x3_cell_id = (0,0)
max_3x3_cell = 0
max_3x3_cell_size = 0

import time
for s in range(1,301):
    print (s)
    for x in range(1, 301):
        for y in range(1, 301):
            temp = 0
            if not((x+s) > 300 or (y+s) > 300):
                temp = np.sum(pls[x:x+s,y:y+s])
                if temp > max_3x3_cell:
                    max_3x3_cell_id = (x, y)
                    max_3x3_cell = temp
                    max_3x3_cell_size = s

print (max_3x3_cell)
print (max_3x3_cell_id, max_3x3_cell_size)

            
            

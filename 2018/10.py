import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

with open("message.txt", "r") as f:
    lines = f.readlines()

points = []
velocities = [] 
for l in lines:
    p = [int(l[10:16]), int(l[18:24])]
    v = [int(l[36:38]), int(l[39:42])]
    points.append(p)
    velocities.append(v)

l = len(points)
t_min = None
min_dist = 100000000

start_time = 0
#points = [[p[0]+velocities[i][0]*start_time, p[1]+velocities[i][1]]*start_time for i,p in enumerate(points)]

for t in range(start_time, 10631):
    xmin = None
    ymin = None
    xmax = None
    ymax = None

    print "seconds " + str(t)
    for i, p in enumerate(points):
        points[i] = [p[0]+velocities[i][0], p[1]+velocities[i][1]]
        if p[0] > xmax or xmax is None:
            xmax = p[0]
        if p[1] > ymax or ymax is None:
            ymax = p[1]
        if p[0] < xmin or xmin is None:
            xmin = p[0]
        if p[1] < ymin or ymin is None:
            ymin = p[1]

    #print l, ymax - ymin
    if min_dist > (ymax - ymin):
        min_dist = ymax - ymin
        t_min = t
        
    if t>10625:
        x = [p[0] for p in points]
        y = [-p[1] for p in points]
        plt.xlim(xmin, xmax)
        plt.ylim(-ymax, -ymin)
        #plt.yticks(range(-ymax, -ymin))
        plt.scatter(x, y, s=1, c='gold', alpha=0.5)
        #plt.hist2d(x, y, bins=(2*xmax-xmin, ymax-ymin))#, c='gold', alpha=0.5)
        ax = plt.gca()
        ax.set_facecolor('black')
        plt.show()

    

from utils import readInput
import numpy as np
from numpy import cos, sin
from itertools import combinations, product

lines = readInput("test.txt")

scan = []
temp = []
for l in lines:
    if l.strip() == "":
        continue
    elif "---" in l:
        if temp != []:
            scan.append(temp)
        temp = []
    else:
        temp.append(np.array(list(map(int, l.split(",")))))

scan.append(temp)

def createMap(trans):
    xmin = min([x[0] for x in trans])
    xmax = max([x[0] for x in trans])
    ymin = min([x[1] for x in trans])
    ymax = max([x[1] for x in trans])
    zmin = min([x[2] for x in trans])
    zmax = max([x[2] for x in trans])
    map1 = np.zeros(shape=(int(xmax-xmin+1), int(ymax-ymin+1), int(zmax-zmin+1)))
    for t in trans:
        #print (t[0]-xmin, t[1]-ymin, t[2]-zmin)
        map1[int(t[0]-xmin), int(t[1]-ymin), int(t[2]-zmin)] = 1
    return map1

def compareMap(m1, m2, offset):
    print (offset)
    print (m1.shape)
    print (m2.shape)
    xmin, xmax = min(m1.shape[0], m2.shape[0]), max(m1.shape[0], m2.shape[0])
    ymin, ymax = min(m1.shape[1], m2.shape[1]), max(m1.shape[1], m2.shape[1])
    zmin, zmax = min(m1.shape[2], m2.shape[2]), max(m1.shape[2], m2.shape[2])
    print (xmin, xmax)
    print (ymin, ymax)
    print (zmin, zmax)
    
    base = np.zeros(shape=(int(xmax-xmin+1), int(ymax-ymin+1), int(zmax-zmin+1)))
    #fm1 = 
    
    
def rotate(scan, alpha, beta, gamma):
    R = np.array([[cos(alpha)*cos(beta), cos(alpha)*sin(beta)*sin(gamma) - sin(alpha)*cos(gamma), cos(alpha)*sin(beta)*cos(gamma) + sin(alpha)*sin(gamma)],
                  [sin(alpha)*cos(beta), sin(alpha)*sin(beta)*sin(gamma) + cos(alpha)*cos(gamma), sin(alpha)*sin(beta)*cos(gamma) - cos(alpha)*sin(gamma)], 
                  [-sin(beta), cos(beta)*sin(gamma), cos(beta)*cos(gamma)]])
    return [np.rint(s.dot(R)) for s in scan]

def sort(trans):
    return list(map(list, trans))#sorted(trans, key=lambda x:(x[0], x[1], x[2]))

a = (0, np.pi/2, np.pi, 3/2*np.pi)
perm = []
for p in product(a, repeat=3):
     perm.append(p)

to_do = [0]
done = []
matches = {}

while len(done) < len(scan):
    print (to_do)
    new_to_do = []
    for i in to_do:
        #for i in range(len(scan)-1):
        for j in range(len(scan)):
            if i == j:
                continue
            match = False
            print ("scanner ", i, j)
            trials = 0
            m1 = createMap(scan[i])

            for b1 in scan[i]:
            #    #print ("trials ", len(scan[i]), trials)
            #    if trials > len(scan[i]) - 12:
            #        print ("non ci possono essere 12 beacons")
            #        break
            #    m0 = sort(scan[i])
                ##            print (m0)
                for p in perm:                
                    rot_scan = rotate(scan[j], *p)
                    for b2 in rot_scan:
                        offset = b1 - b2
                        #trans = rot_scan + offset
                        m2 = createMap(rot_scan)
                        compareMap(m1, m2, offset)
                        import sys
                        sys.exit()
#            #            m1 = sort(trans)
#                        #                    #print (m0)
#                        nmatches = 0
#                        c_matches = []
#                        for im in m0:
#                            if im in m1:
#                                c_matches.append(im)
#                                #                            #print(im)
#                                nmatches += 1
#                        if nmatches >= 12:
#                            print ("nmatches ", nmatches)
#                            matches[(i, j)] = (offset, p, c_matches)
#                            match = True
#                            done.append(i)
#                            done.append(j)
#                            new_to_do.append(j)
#                            break
#
#                    if match:
#                        break
#                if match:
#                    break
#                trials += 1
#    to_do = new_to_do    
#    done = list(set(done))

#matches = {(0, 1): (np.array([   68., -1246.,   -43.]), (0, 3.141592653589793, 0)),
#           (1, 3): (np.array([  160., -1134.,   -23.]), (0, 0, 0)),
#           (1, 4): (np.array([   88.,   113., -1104.]), (1.5707963267948966, 0, 4.71238898038469)),
#           (2, 4): (np.array([1125., -168.,   72.]), (1.5707963267948966, 0, 3.141592653589793))}

done = []
common = []
ref = None
while len(done) < len(scan):
    for k, v in matches.items():
        if ref is None:
            ref = k
            done.append(k[0])
            done.append(k[1])
            #common += v[2]
        else:
            if k[1] in done:
                continue
            if k[0] == ref[1]:
                rotated = rotate([v[0]], matches[ref][1][0], matches[ref][1][1], matches[ref][1][2])
                #for b in rotated:
                print (matches[ref][0] + rotated[0])
                done.append(k[1])
            else:
                subt = (ref[1], k[1])
                

    print (done)
    break
    


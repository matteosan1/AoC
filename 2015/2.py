with open("instructions2a.txt", "r") as f:
    lines = f.readlines()

tot_surf = 0
tot_ribbon = 0
for l in lines:
    l = l.split("\n")[0]
    l, w, h = map(int, l.split("x"))
    surf = 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    tot_surf += surf

    ribbon = h*l*w + min(2*(l+w), 2*(w+h), 2*(h+l))
    tot_ribbon += ribbon
    
print (tot_surf)
print (tot_ribbon)

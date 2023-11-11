i1 = 0
i2 = 1
rec = [3, 7]

def printRec(rec, i1, i2):
    for i,r in enumerate(rec):
        if i == i1:
            print (" ("+str(r)+") ", end='')
        elif i == i2:
            print (" ["+str(r)+"] ", end='')
        else:
            print (" " + str(r) + " ", end='')
    print ()

#printRec(rec, i1, i2)
n = 2
end = "170641"
nrecipes = 10
last_ten = ""
while 1:
    new_recipe = rec[i1] + rec[i2]
    n_new_recipe = len(str(new_recipe))
    for i in str(new_recipe):
        rec.append(int(i))

    i1 = (i1 + rec[i1] + 1) % (len(rec))
    i2 = (i2 + rec[i2] + 1) % (len(rec))

    exit = False
    for i in range(n_new_recipe):
        n = n + 1
        #if n < end:
        #    print ("prima ", new_recipe)
        #if n > end:
        #    last_ten = last_ten + str(new_recipe)[i]
        #if n >= (end + nrecipes):
        #    exit = True
        #    break
        if n > len(end):
            #print ("".join(list(map(str, rec[-5:]))))
            #print (str(end))
            if "".join(list(map(str, rec[-len(end):]))) == end:
                print (n_new_recipe, i)
                print (len(rec) - len(end))
                print ("".join(list(map(str, rec[-len(end):]))))
                #print (rec)
                exit = True
                break

    if (exit):
        break

#print (last_ten)



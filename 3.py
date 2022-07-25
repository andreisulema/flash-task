for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                for v in 0,1:
                    f = (x and y and z) <= (not y and w and v)
                    if f == 0:
                        print(x,y,z,w,v)

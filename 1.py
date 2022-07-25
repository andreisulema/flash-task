def f(x,y,z):
    return int((x or y) == (y or not z) and x)

print('x y z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if f(x,y,z)!=(not f(not x, not y, not z)):
                print(x,y,z)

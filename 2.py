def f(x,y,z):
    return int(x == (((y and z)<= z) and not z))

print('x y z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            print(x,y,z,f(x,y,z))

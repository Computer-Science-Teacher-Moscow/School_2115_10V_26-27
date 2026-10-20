def f(x, y, w, z):
    print(f'x = {x}, y = {y}, w = {w}, z = {z}')


d = {'x': 5,
     'z': 7,
     'y': 3,
     'w': 1}
f(**d)
a = (1, 0, 1, 1)
p = ('x','z','w','y')
zp = dict(zip(p, a))
print(zp)
f(**zp)

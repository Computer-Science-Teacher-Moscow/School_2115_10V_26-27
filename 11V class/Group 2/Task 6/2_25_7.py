from turtle import *

lt(90)
tracer(0)
screensize(5000, 5000)
r = 15
for _ in range(3):
    fd(39 * r)
    rt(90)
    fd(48 * r)
    rt(90)
up()
fd(27 * r)
rt(90)
fd(24 * r)
lt(90)
down()
for _ in range(3):
    fd(29 * r)
    rt(90)
    bk(18 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()

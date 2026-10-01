from turtle import *

lt(90)
tracer(0)
screensize(5000, 5000)
r = 15
for _ in range(3):
    fd(28 * r)
    rt(90)
    fd(26 * r)
    rt(90)
up()
fd(8 * r)
rt(90)
fd(7 * r)
lt(90)
down()
for _ in range(4):
    fd(67 * r)
    rt(90)
    fd(98 * r)
    rt(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()

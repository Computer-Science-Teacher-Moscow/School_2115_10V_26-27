from turtle import *

lt(90)
tracer(0)
r = 20
rt(90)
for _ in range(3):
    rt(45)
    fd(10 * r)
    rt(45)
rt(315)
fd(10 * r)
for _ in range(2):
    rt(90)
    fd(10 * r)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()

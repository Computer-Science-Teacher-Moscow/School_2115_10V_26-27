from turtle import *

lt(90)
tracer(0)
screensize(5000, 5000)
r = 15
for _ in range(2):
    fd(6 * r)
    rt(90)
    fd(12 * r)
    rt(90)
up()
fd(1 * r)
rt(90)
fd(3 * r)
lt(90)
down()
for _ in range(2):
    fd(77 * r)
    rt(90)
    fd(45 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()

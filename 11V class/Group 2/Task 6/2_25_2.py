from turtle import *

lt(90)
tracer(0)
r = 20
rt(30)
for _ in range(3):
    rt(150); fd(6 * r); rt(30); fd(12 * r)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()

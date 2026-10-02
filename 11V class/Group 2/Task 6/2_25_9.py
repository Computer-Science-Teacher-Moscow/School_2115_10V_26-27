# 2.25 №9
from turtle import *

tracer(0)
r = 30
screensize(5000, 5000)

for _ in range(2):
    down()
    for __ in range(2):
        fd(8 * r)
        rt(90)
        fd(8 * r)
        rt(90)
    up()
    fd(6 * r)
    rt(90)
    fd(6 * r)
    lt(90)
rt(180)
fd(4 * r)
down()
for _ in range(4):
    fd(8 * r)
    rt(270)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()
done()
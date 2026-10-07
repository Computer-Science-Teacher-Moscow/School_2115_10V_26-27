from turtle import *  # импортируем все функции модуля turtle

lt(90)  # поворот налево на 90 градусов (направляем черепаху вертикально вверх)
tracer(0)  # отключает отрисовку черепахой
screensize(5000, 5000)

r = 20  # шаг в пикселях на 1 единицу движения черепахи

for _ in range(2):
    fd(13 * r)
    rt(90)
    fd(20 * r)
    rt(90)
up()
fd(8 * r)
rt(90)
bk(3 * r)
lt(90)
down()
for _ in range(2):
    fd(16 * r)
    rt(90)
    fd(8 * r)
    rt(90)

up()  # поднимаем хвост вверх чтобы рисовать точки целочисленные
# Отрисовка целочисленных точек
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update()  # для Pycharm
done()  # для Pycharm

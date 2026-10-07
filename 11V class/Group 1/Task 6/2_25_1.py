from turtle import * # импортируем все функции модуля turtle

lt(90)  # поворот налево на 90 градусов (направляем черепаху вертикально вверх)

tracer(0) # отключает отрисовку черепахой
r = 25  # шаг в пикселях на 1 единицу движения черепахи
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

up() # поднимаем хвост вверх
# Отрисовка целочисленных точек
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(5, 'red')
update() # для Pycharm
done() # для Pycharm
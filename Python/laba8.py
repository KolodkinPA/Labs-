# coding: utf8
from math import sqrt
import random
import matplotlib.pyplot as plt

x = []
y = []


def massive_generation():  # заполнение массива генератором случайных чисел
    for i in range(100):
        x.append(random.uniform(-5, 5))
        y.append(random.uniform(-5, 5))


def belong_to_locality(x_coord, y_coord, rad, changingpoint_x, changingpoint_y):
    # функция, определяющая принадлежность окрестности
    distance = sqrt((x_coord - changingpoint_x) ** 2 + (y_coord - changingpoint_y) ** 2)
    if distance <= rad:
        return 1
    else:
        return 0

def changepoint():
    change = random.randint(0,99)
    return change

def points_quantity(rad,change):  # функция, считающая число точек, входящих в окрестность
    counter = 0
    data = []
    xx = []
    yy = []
    massive_generation()
    for i in range(100):
        if belong_to_locality(x[i], y[i], rad, x[change], y[change]) == 1:
            counter += 1
            xx.append(x[i])
            yy.append(y[i])
    data.append(xx)
    data.append(yy)
    data.append(counter)
    return data


radius = float(input("Введите радиус окрестности: "))
change = changepoint()
data = points_quantity(radius*2, change)
count = data[2]
print("X = ", x)
print("Y = ", y)
print("Кол-во точек в окрестности: ", count)

fig = plt.figure()
plt.scatter(x, y)
plt.scatter(data[0], data[1], color='red')
plt.scatter(x[change], y[change], color='green')

circle = plt.Circle((x[change], y[change]), radius*2, Fill=False)
plt.gcf().gca().add_artist(circle)

print(fig.axes)

plt.grid()

plt.show()
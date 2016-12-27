# coding: utf8
from math import atanh
from math import fabs

import math

change = 1

while change == 1:
    enter = input("Введите X: ")
    x = float(enter)
    enter = input("Введите границу Х: ")
    x2 = float(enter)
    enter = input("Введите а: ")
    a = float(enter)
    enter = input("Введите шаг: ")
    step = float(enter)
    enter = input("Введите разницу между значениями функции: ")
    delta = float(enter)
    enter = input("Введите шаблон: ")
    name = input("Выберите функцию. 1 если G , 2 если F, 3 если Y: ")
    i = 0
    pi = 3.14
    perm1=(27*a**2+33*a*x+10*x**2)
    perm2=(72*a**2-5*a*x-12*x**2-pi/2)
    perm3=(42*a**2+53*a*x+15*x**2+1)
    output = str()
    counter = 0

    if name == 1:
        while x < x2:
            if perm1 != 0:
                function = (-(8*(7*a**2+34*a*x-5*x**2))/(27*a**2+33*a*x+10*x**2))
                print("G = ", function)
                output = output + str(function)
            x += step
            i += 1
            if x >= x2 or i > 100:
                break
        print(output)
        output1 = output.split(enter)
        print(output1)
        k = len(output1)-1
        print(k)
        output = ' '
    elif name == 2:
        while x < x2:
            if perm2 != 0:
                function = (-(1)/(math.sin(72*a**2-5*a*x-12*x**2-pi/2 )))
                print("F = ", function)
                output = output + str(function)
            x += step
            i += 1
            if x >= x2 or i > 100:
                break
        print(output)
        output1 = output.split(enter)
        print(output1)
        k = len(output1) - 1
        print(k)
        y = ' '
    elif name == 3:
        while x < x2:
            if perm3 >= 0:
                function = (math.log(42 * a ** 2 + 53 * a * x + 15 * x ** 2 + 1))
                print("Y = ", function)
                output = output + str(function)
            x += step
            i += 1
            if x >= x2 or i > 100:
                break
        print(output)
        output1 = output.split(enter)
        k = len(output1) - 1
        print(k)
        output = ' '
    else:
        print("Неправильно выбрана функция, или ничего не выбрано")
change = int(input("Хотите посчитать другую функцию? Введите 1, если да, в противном случае - любой другой символ"))

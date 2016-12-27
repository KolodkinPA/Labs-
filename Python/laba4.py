# coding: utf8
import math
import matplotlib.pyplot as plt
#Спрашиваем пользователя хочет ли он запустить код
print ("Вы хотите начать программу? Если да нажмите 1. Если нет нажмите 0")
z=int(input())
xv= []
if z==1:
    #Задаем все переменные имеющиеся в коде
    print("Введите переменную a")
    a=float(input())
    print("Введите переменную x")
    x=float(input())
    print("Введите ограничитель для  x")
    gran=float(input())
    print ("Введите ограничитель для а")
    gran2= float(input())
    print("Введите размер шага")
    step=float(input())
    print("Введите количество шагов")
    pl= float(input())
    pi=3.14
    #Чать функции которая участвует в цикле
    perm1=(27*a**2+33*a*x+10*x**2)
    perm2=(72*a**2-5*a*x-12*x**2-pi/2)
    perm3=(42*a**2+53*a*x+15*x**2+1)
    #Выбор функции коорую нужно посчитать
    print("Введите функцию которую хотите посчитать.1 если первую,2 если вторую. 3 если третью")
    o=int(input())
    if o==1:
            #Вычисление 1 функции
            while gran /step > pl:
                step = step + 0.1
                #Начало цикла
                while x < gran:
                    if perm1 != 0:
                        g=(-(8*(7*a**2+34*a*x-5*x**2))/(27*a**2+33*a*x+10*x**2))
                        print ([ g, x,])
                        #Сохраненее даннных в список
                        x = x + step
                        xv.append(g)
                        max(xv)
                        min(xv)
            while  gran /step < pl:
                #Изменение шага
                step=step-0.1
                while x < gran:
                    if perm1>0:
                        g = (-(8 * (7 * a ** 2 + 34 * a * x - 5 * x ** 2)) / (27 * a ** 2 + 33 * a * x + 10 * x ** 2))
                        round(g, 3)
                        print ([ g, x])
                        x = x + step
                        xv.append(g)
                        max(xv)
                        min(xv)
            #Построение графика функции
            print("MIN", min(xv))
            print("MAX",max(xv))
            fig = plt.figure()
            plt.plot(xv , 'bo-' )
            print(fig.axes)
            plt.show()
    if o==2:
            while gran/step > pl:
                step = step + 0.1
                while x < gran:
                    if perm2 > 0:
                        f= (-(1)/(math.sin(72*a**2-5*a*x-12*x**2-pi/2 )))
                        print([f, x])
                        x= x+step
                        xv.append(f)
                        max(xv)
                        min(xv)
            while  gran/step < pl:
                step=step-0.1
                while x<gran:
                    if perm2 > 0:
                        f= (-(1)/(math.sin(72*a**2-5*a*x-12*x**2-pi/2 )))
                        print([f, x])
                        x= x+step
                        xv.append(f)
                        max(xv)
                        min(xv)
            print("MIN", min(xv))
            print("MAX",max(xv))
            fig = plt.figure()
            plt.plot(xv , 'bo-'  )
            print(fig.axes)
            plt.show()
    if o == 3:
        while  gran / step > pl:
            step = step + 0.1
            while x < gran :
                if perm3 > 0:
                    y = (math.log(42 * a ** 2 + 53 * a * x + 15 * x ** 2 + 1))
                    print([y, x])
                    x = x + step
                    xv.append(y)
                    max(xv)
                    min(xv)
        while gran / step < pl:
            step = step - 0.1
            while x < gran:
                if perm3 > 0:
                    y = (math.log(42 * a ** 2 + 53 * a * x + 15 * x ** 2 + 1))
                    print([y, x])
                    x = x + step
                    xv.append(y)
                    max(xv)
                    min(xv)
    print("MIN", min(xv))
    print("MAX", max(xv))
    fig = plt.figure()
    plt.plot(xv, 'bo-')
    print(fig.axes)
    plt.show()
elif z==0:
        print("Завершение программы")
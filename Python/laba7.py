# coding: utf8
import math
output = []
memory = []
iterator = []
n = 0
x = float(input("Введите х"))
memory.append(x)
gran = float(input("Введите предел х"))
memory.append(gran)
a = float(input("Введите параметр а"))
step = float(input("Введите размер шага"))
pi = 3.14
perm1 = (27 * a ** 2 + 33 * a * x + 10 * x ** 2)
perm2 = (72 * a ** 2 - 5 * a * x - 12 * x ** 2 - pi / 2)
perm3 = (42 * a ** 2 + 53 * a * x + 15 * x ** 2 + 1)

while x < gran:
    if perm1 != 0:
        function = (-(8*(7*a**2+34*a*x-5*x**2))/(27*a**2+33*a*x+10*x**2))
        output.append(str(function))
    x = x + step
    n = n + 1
    if x >= gran or n > 100:
        break

x = memory[0]
gran = memory[1]
iterator.append(n)
n = 0

while x < gran:
        function = (-(1) / (math.sin(72 * a ** 2 - 5 * a * x - 12 * x ** 2 - pi / 2)))
        output.append(str(function))
        x = x + step
        n = n + 1

x = memory[0]
gran = memory[1]
iterator.append(n)
f = open("/home/ipavel/laba7.txt","w")
f.write("===================================================================================================\n")
for k in range(iterator[0]+iterator[1]):
    f.write("|" + output[k] + "|\n")
    f.write("_______________________________________________________________________________________________\n")
f.write("===================================================================================================\n")
f.close()
f1 = open("/home/ipavel/laba7.txt","r")
for line in f1:
    print(line)
f1.close()

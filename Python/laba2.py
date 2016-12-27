if o == 2:
    if i / step < pl:
        while x < i:
            if perm2 > 0:
                f = (-(1) / (math.sin(72 * a ** 2 - 5 * a * x - 12 * x ** 2 - pi / 2)))
                print(f)
                x = x + step
                xv.append(f)
            else:
                print("Ошибка")
    elif i / step > pl:
        step = step - size
        while x < i:
            if perm2 > 0:
                f = (-(1) / (math.sin(72 * a ** 2 - 5 * a * x - 12 * x ** 2 - pi / 2)))
                print(f)
                x = x + step
                xv.append(f)
    else:
        step = step + size
        while x < i:
            if perm2 > 0:
                f = (-(1) / (math.sin(72 * a ** 2 - 5 * a * x - 12 * x ** 2 - pi / 2)))
                print(f)
                x = x + step
                xv.append(f)
    fig = plt.figure()
    plt.plot(xv, 'bo-')
    print(fig.axes)
    plt.show()
if o == 3:
    if i / step < pl:
        while x < i:
            if perm3 > 0:
                y = (math.log(42 * a ** 2 + 53 * a * x + 15 * x ** 2 + 1))
                print(y)
                x = x + step
                xv.append(y)
        else:
            print("Ошибка")
    elif i / step > pl:
        step = step - size
        while x < i:
            if perm3 > 0:
                y = (math.log(42 * a ** 2 + 53 * a * x + 15 * x ** 2 + 1))
                print(y)
                x = x + step
                xv.append(y)
    else:
        step = step + size
        while x < i:
            if perm3 > 0:
                y = (math.log(42 * a ** 2 + 53 * a * x + 15 * x ** 2 + 1))
                print(y)
                x = x + step
                xv.append(y)
    fig = plt.figure()
    plt.plot(xv, 'bo-')
    print(fig.axes)
    plt.show()
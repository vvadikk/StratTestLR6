import two
import re

while 1:
    x1 = int(input('Введите аргумент для f1: '))
    try:
        y1 = two.f1(x1)
        print(y1)
        break
    except ZeroDivisionError:
        print('Знаменатель обратился в ноль, введите другое значение')

x2 = int(input('Введите первый аргумент для f2: '))
y2 = int(input('Введите второй аргумент для f2: '))
try:
    w2 = two.f2(x2, y2)
    print(w2)
except NameError:
    two.z = int(input('Переменная z не определена, введите ее значение: '))
    w2 = two.f2(x2, y2)
    print(w2)

while 1:
    s = input('Введите строку s, отличную от числа: ')
    if bool(re.fullmatch(r'\d+(\.\d+)?', s)):
        s = float(s)
    try:
        l = two.f3(s)
        print(l)
        break
    except TypeError:
        print('Введенное значение было принято за число, возникла ошибка')
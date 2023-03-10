print('''Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные,
 прямоугольные и круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой
  подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.

Формат ввода, который используют Малевийцы:

треугольник
a
b
c
где a, b и c — длины сторон треугольника

прямоугольник
a
b
где a и b — длины сторон прямоугольника

круг
r
где r — радиус окружности''')
room = input('Введите фигуру комнаты: ')
if room == 'треугольник':
    a, b, c = float(input('Введите первую сторону: ')), float(input("Введите вторую сторону: ")), float(input("Введите третью сторону: "))
    p = (a + b + c) / 2
    print(("Площадь комнаты =", p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif room == 'прямоугольник':
    a, b = float(input('Введите первую сторону: ')), float(input("Введите вторую сторону:"))
    print("Площадь комнаты =", a * b)
elif room == 'круг':
    p = 3.14
    r = float(input("Введите радиус комнаты: "))
    print("Площадь комнаты =", p*(r**2))
print('''Напишите программу, которая получает на вход три целых числа, по одному числу в строке, 
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.''')
a, b, c = int(input('Введите  первое число: ')), int(input('Введите второе число: ')), int(input('Введите  третье числоЖ '))
x = max(a, b, c)
y = min(a, b, c)
print(x)
print(y)
if (x == a and y == b) or (x == b and y == a):
    print(c)
elif (x == a and y == c) or (x == c and y == a):
    print(b)
elif (x == b and y == c) or (x == c and y == b):
    print(a)
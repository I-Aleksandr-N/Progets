print('''Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение
попадает в интервал (−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).
Обратите внимание на разные скобки, используемые для обозначения интервалов. В задании используются
полуоткрытые и открытые интервалы. Подробнее про это вы можете прочитать, например, на википедии
(полуинтервал, промежуток).''')

from decimal import Decimal
pos_inf = Decimal('Infinity')
num = int(input("Введите числоЖ "))
x = 19
if num in range(-14, 13):
    print(True)
elif num in range(15, 17):
    print(True)
elif x <= num < pos_inf:
    print(True)
else:
    print(False)
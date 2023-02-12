count = int(input())
students = int(str(count)[-1])
students2 = int(str(count)[-2:])
if students == 1 and not(11 <= students2 <= 14):
    print(count, 'программист')
elif students in range(2, 5) and (0 <= count <= 1000) and not(11 <= students2 <= 14):
    print(count, 'программиста')
elif (0 <= count <= 1000):
    print(count, 'программистов')
comand1 = int(input())
comand2 = int(input())
pie = 1
while comand1 > 0 and comand2 > 0:
    if pie % comand1 == 0 and pie % comand2 == 0:
        break
    pie += 1
print(pie)
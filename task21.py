#Напишите программу, на вход которой подаётся список чисел одной строкой. 
#Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
#Подробнее: https://stepik.org/lesson/3368/step/11?unit=951 

a=[int(i) for i in input().split()]
if len(a)==1:
    print(*a)
else:
    for i in range (0, len(a)):
        print(*[a[i-1]+a[i-len(a)+1]],' ', end='')
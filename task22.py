#Напишите программу, которая принимает на вход список чисел в одной строке 
#и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
#Подробнее: https://stepik.org/lesson/3368/step/12?unit=951

a=[int(i) for i in input().split()]
a.sort()
b=[]
if len(a)>1:
    for i, item in enumerate(a):
        if (a[i-1]==a[i] or a[i]==a[i-len(a)+1]) and a[i] not in b:
            b.append(a[i])
print(*b)
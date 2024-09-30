#Условие: https://stepik.org/lesson/3369/step/9?unit=952

lst=[int(i) for i in input().split()]
n=int(input())
if lst.count(n)==0:
    print('Отсутствует')
else:
    for i in range(0,len(lst)):
        if lst[i]==n:
            print(i, end=' ')
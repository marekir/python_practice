#Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, 
#выходящей из левого верхнего угла и закрученной по часовой стрелке
#Условие: https://stepik.org/lesson/3369/step/11?unit=952

n = int(input())
a = [[0 for i in range(n)]for i in range(n)]
step = 1
n1 = 0

while step<=n**2:
    for i in range(0+n1,n-n1):
        a[n1][i]=step
        step+=1    
    for i in range(n1+1,n-n1):
        a[i][n-n1-1]=step
        step+=1
    for i in range (n-n1-1,n1,-1):
        a[n-n1-1][i-1]=step
        step+=1
    for i in range (n-n1-2,n1,-1):
        a[i][n1]=step
        step+=1
    n1+=1
        
for i in range(0,n):
    print(*a[i])
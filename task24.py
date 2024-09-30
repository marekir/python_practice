#Условие: https://stepik.org/lesson/3369/step/8?unit=952

n=int(input())
cur=1
pr=1
while pr<=n:
    a=1
    while a<=cur and pr<=n:
        print(cur, end=' ')
        a+=1
        pr+=1
    cur+=1
#Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) 
#в введенной строке (программа не должна зависеть от регистра вводимых символов).
#Подробнее: https://stepik.org/lesson/3367/step/3?unit=950

a=int(input())
b=int(input())
ab=0
step=0

a+=-a%3

for i in range(a,b+1,3):
    step+=1
    ab+=i
    
print(ab/step)

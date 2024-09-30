#Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и 
#выводит на консоль среднее арифметическое всех чисел из отрезка [a;b][a;b], которые кратны числу 3.
#Подробнее: https://stepik.org/lesson/3366/step/7?unit=949

a=int(input())
b=int(input())
ab=0
step=0

a+=-a%3

for i in range(a,b+1,3):
    step+=1
    ab+=i
    
print(ab/step)

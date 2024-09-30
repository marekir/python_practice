#Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. 
#Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b][a;b] на все числа отрезка [c;d][c;d].
#Числа a, b, c и d являются натуральными и не превосходят 10, a≤ba≤b, c≤dc≤d
#Подробное условие: https://stepik.org/lesson/3366/step/3?unit=949

a=int(input())
b=int(input())
c=int(input())
d=int(input())

res=""

for i in range(c,d+1):
    res+='\t'+str(i)
print(res)

for i in range(a,b+1):
    res=""
    res+=str(i)+'\t'
    for j in range(c,d+1):
        res+=str(i*j)+'\t'
    print(res)

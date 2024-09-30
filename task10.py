#Напишите программу, которая получает на вход три целых числа, по одному числу в строке, 
#и выводит на консоль в три строки сначала максимальное, потом минимальное, 
#после чего оставшееся число.

a, b, c = int(input()), int(input()), int(input())

if a==b==c:
    print(a,'\n',b,'\n',c)
elif a>=b and a>=c:
    print (a)
    if b<=c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif b>=a and b>=c:
    print (b)
    if a<=c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
elif c>=a and c>=b:
    print(c)
    if a<=b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)
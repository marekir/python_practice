#Напишите программу, считывающую с пользовательского ввода целое число nn (неотрицательное), 
#выводящее это число в консоль вместе с правильным образом изменённым словом "программист", 
#например: 1 программист, 2 программиста, 5 программистов.
#Для того, чтобы это звучало правильно, для каждого nn нужно использовать верное окончание слова.
#Число программистов 0≤n≤10000≤n≤1000

num=str(input())
str_len = len(num)

if str_len==1:
    if num=="1":
        print (num, "программист")
    elif num in ["2","3","4"]:
        print (num,"программиста")
    else:
        print (num,"программистов")
else:
    if num[str_len-2]!="1" and num[str_len-1] in ["2","3","4"]:
        print(num,"программиста")
    elif num[str_len-2:]=="11" or num[str_len-1]!="1":
        print(num,"программистов") 
    else:
        print(num,"программист")
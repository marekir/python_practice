#Напишите функцию modify_list(l), которая принимает на вход список целых чисел, 
#удаляет из него все нечётные значения, а чётные нацело делит на два. 
#Функция не должна ничего возвращать, требуется только изменение переданного списка
#Условие: https://stepik.org/lesson/3372/step/9?unit=955

def modify_list(l):
    i=0
    while i<len(l):
        if l[i]%2==0:
            l[i]//=2
            i+=1
        else:
            l.remove(l[i])
            i+1
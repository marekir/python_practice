#Программа должна считывать два положительных целых числа aa и bb, каждое число вводится на отдельной строке)
#и выводить наименьшее число d, которое делится на оба этих числа без остатка.

a=int(input())
b=int(input())
n=1

while not (n%a==0 and n%b==0):
    n+=1
print(n)

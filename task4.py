#Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы AA часов в сутки, 
#но пересыпать тоже вредно и не стоит спать более BB часов. 
#Сейчас Аня спит HH часов в сутки. Если режим сна Ани удовлетворяет рекомендациям 
#передачи “Здоровье”, выведите “Это нормально”. Если Аня спит менее AA часов, 
#выведите “Недосып”, если же более BB часов, то выведите “Пересып”.

#Получаемое число AA всегда меньше либо равно BB.

#На вход программе в три строки подаются переменные в следующем порядке: AA, BB, HH.

a=int(input())
b=int(input())
h=int(input())

if h<a:
    print
    print ("Недосып")
if h>b:
    print ("Пересып")
else:
    if h>=a and h<=b:
        print ("Это нормально")
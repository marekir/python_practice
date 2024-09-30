#Условие: https://stepik.org/lesson/3373/step/6?unit=956

words=[str(i) for i in input().lower().split()]
res = {}
for i in words:
    res[i]=words.count(i)
    
for key, value in res.items():
    print(key, value, end='\n')
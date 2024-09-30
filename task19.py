#Алгоритм сжатия, который сжимает повторяющиеся символы в строке.
#Подробнее: https://stepik.org/lesson/3367/step/7?unit=950

s=str(input())
code=""
while s:
    code+=s[0]
    n=0
    while s[0]==code[-1]:
        n+=1
        s=s.replace(s[0],'',1)
        if len(s)==0:
            break
    code+=str(n)
    #print(code, s)
        
print(code)

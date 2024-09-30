#Условие: https://stepik.org/lesson/3363/step/2?unit=1135

s = ''
with open('dataset_3363_2.txt','r') as inf:
    s = inf.readline().strip()
l = len(s)

for i in range(0,l):
    num=''
    alpha=''
    if s[i].isalpha():
        alpha+=s[i]
        i+=1
        while not s[i-l].isalpha():
            num+=s[i-l]
            i+=1
        with open('dataset.txt','a') as f:
            for j in range(0, int(num)):
                f.write(alpha)

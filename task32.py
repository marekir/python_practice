#Условие: https://stepik.org/lesson/3373/step/7?unit=956

n=int(input())
nums = [int(input()) for i in range(n)]
res = {}
for i in set(nums):
    res[i]=f(i)
    
for i in nums:
    print(res[i])
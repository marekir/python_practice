#Условие: https://stepik.org/lesson/3363/step/3?unit=1135
calc = {}
s = []
with open('dataset_3363_3.txt') as f:
    for line in f:
        s+= f.readline().strip().lower().split()

for i in set(s):
    if s.count(i) in calc.keys():
        calc[s.count(i)].append(i)
    else:
        calc[s.count(i)]=[]
        calc[s.count(i)].append(i)
print(calc)    
print(min(calc[max(calc.keys())]), max(calc.keys()))

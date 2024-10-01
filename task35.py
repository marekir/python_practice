#Условие: https://stepik.org/lesson/3363/step/4?unit=1135
students = {}
with open('dataset_3363_4.txt',encoding='utf-8') as f:
    for line in f:
        s = line.strip().split(';')
        students[s[0]]=[]
        for i in s[1:]:
            students[s[0]].append(float(i))

names_num = len(students.keys())
with open('task35_res.txt', 'w') as f:
    math=float(0)
    ph=float(0)
    rus=float(0)
    for key in students.keys():
        f.write(str(round(sum(students[key])/3,9))+'\n')
        math+=students[key][0]
        ph+=students[key][1]
        rus+=students[key][2]
    f.write(str(round(math/names_num,9))+' '+str(round(ph/names_num,9))+' '+str(round(rus/names_num,9)))

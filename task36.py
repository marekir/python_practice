#Условие: https://stepik.org/lesson/3378/step/2?unit=961

import requests

f=open("dataset_3378_2.txt","r")
url=f.readline().strip()
f.close()

print(url)
r=requests.get(url)
if r.status_code == 200:
    print("Success")
else:
    print("Failed")

#print(r.text)
print(len(r.text.splitlines()))

#Условие: https://stepik.org/lesson/3378/step/3?unit=961

import requests

f=open("dataset_3378_3.txt","r")
url=f.readline().strip()
f.close()
print(url)
r=requests.get(url)

while not r.text.startswith("We"):
    r = requests.get("https://stepik.org/media/attachments/course67/3.6.3/"+r.text)

print(r.text)

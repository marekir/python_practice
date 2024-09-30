#Условие: https://stepik.org/lesson/3373/step/5?unit=956

def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        if key*2 in d:
            d[key*2].append(value)
        else:
            d[key*2]=[value]
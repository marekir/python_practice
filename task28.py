#Условие: https://stepik.org/lesson/3372/step/8?unit=955

def f(x):
    if x<=-2:
        x=1-(x+2)**2
    elif -2<x<=2:
        x=x*(-0.5)
    elif x>2:
        x=1+(x-2)**2
    return x
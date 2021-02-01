"""
Podríamos dibujar varios polígonos con nuestra función, incrementando el número de lados:
"""
from turtle import *

def poligonos(lado,a):
    for i in range(a): 
        forward(lado)
        left(360/a)#los lados iguales que va a tener por eso 360 lo dividimos por a 

for i in range(3,15):
    poligonos(50,i)

    

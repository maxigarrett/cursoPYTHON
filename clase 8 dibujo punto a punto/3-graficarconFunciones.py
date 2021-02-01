"""rear una función que dibuje polígonos regulares."""

from turtle import *

def poligonos(lado,a):
    for i in range(a): 
        forward(lado)
        left(360/a)#los lados iguales que va a tener por eso 360 lo dividimos por a 

poligonos(100,5)


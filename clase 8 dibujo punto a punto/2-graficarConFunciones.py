# graficar cuadrado con funcion

from turtle import *
def cuadrado(lado):
    for i in range(4):
        forward(lado)
        left(90)
cuadrado(100)
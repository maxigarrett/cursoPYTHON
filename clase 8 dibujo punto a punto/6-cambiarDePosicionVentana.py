
# setup(ancho,alto,x,y)
from turtle import *

setup(600,300,40,50)
title("titulo de la vantana")

def poligonos(lado,a):
    for i in range(a): 
        forward(lado)
        left(360/a)
poligonos(100,5)

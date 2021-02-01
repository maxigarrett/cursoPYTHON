from turtle import *

setup(600,400,40,20)
title("titulo de la vantana")
screensize(100,100)#por defecto es 400X300
def poligonos(lado,a):
    for i in range(a): 
        forward(lado)
        left(360/a)
poligonos(100,5)
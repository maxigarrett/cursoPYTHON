"""Podemos movernos de un lado al otro del área de dibujo sin dibujar la línea con la función PENUP 
(y con la función PENDOWN volvemos a bajar el lápiz).
"""
from turtle import *
forward(100)
penup()#levenatamos el lapiz
back(50)#mientras esta leveantado retorcedemos 50px
pendown()#bajamos el lapiz
left(45)
forward(100)
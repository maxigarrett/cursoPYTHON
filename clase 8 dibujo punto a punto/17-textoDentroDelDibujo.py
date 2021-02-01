from turtle import *
# circle(40)
# left(90)
# penup()
# forward(100)
# write("esto es un circulo")

"""DESPLAZAMIENTO: este parámetro puede tomar los valores TRUE o FALSE y lo que le indicamos a Python es si desplaza el 
cursor a la esquina inferior derecha del texto o no antes de seguir dibujando.

Probamos FALSE:
"""
circle(40)
left(90)
penup()
forward(100)
write("esto es un circulo",False)#termina de escribir y con FALSE le decimos que continua ala izquierda del texto Y VERDADERO a la derecha
pendown()
forward(70)
"""hacemos una espiral con nuestra función polígono.
Le pasamos los datos para crear un triángulo, pero lo hacemos dentro de un bucle en el que luego de dibujar un triángulo, 
rotamos 10 grados a la derecha antes de dibujar el otro
"""


from turtle import *

def poligonos(lado,a):
    for i in range(a): 
        forward(lado)
        left(360/a)#los lados iguales que va a tener por eso 360 lo dividimos por a 

for i in range(20,100,5):
    poligonos(i,3)
    left(10)
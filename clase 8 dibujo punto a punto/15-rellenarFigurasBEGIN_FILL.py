"""La función BEGIN_FILL le indica al programa que, a partir de ahí, todas las figuras que se hagan, deben ir rellenas hasta
 que le indiquemos que deje de hacerlo mediante la función END_FILL.
Para especificar el color de relleno, utilizaremos la función FILLCOLOR.
"""
from turtle import *

begin_fill()
fillcolor("green")#empezar a rellenar de un color
for i in range(4):
    forward(100)
    left(90)
end_fill()#cuando terminamos de dibujar le decimos que pare de rellenar

penup()
forward(150)
pendown()

for item in range(4):
    forward(100)
    left(90)

penup()
back(350)
pendown()
begin_fill()
fillcolor("orange")

left(90)
forward(100)
right(135)
forward(200)
left(135)
forward(100)
left(135)
forward(200)
end_fill
    
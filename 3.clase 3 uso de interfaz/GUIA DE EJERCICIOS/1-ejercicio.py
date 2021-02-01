"""Hacer un programa que contenga tres botones y cada uno de ellos muestre por pantalla (usando una etiqueta) un número al azar
con el siguiente criterio:
•	Botón 1: un número al azar entre 0 y 10.
•	Botón 2: un número al azar entre 0 y 50.
•	Botón 3: un número al azar entre 0 y 100."""

from tkinter import *
from random import randint,random
ventana=Tk()
ventana.title("ingreso de datos")
ventana.resizable(0,0)
ventana.geometry("600x400")

#----------------------------FUNCIONES-----------------------------
def num_aleatorios1():
    aleatorio=randint(0,10)
    lbl2.config(text=aleatorio)
    
def num_aleatorios2():
    aleatorio=randint(0,50)
    lbl3.config(text=aleatorio)

#-----------------------------------------------------------------


lbl1=Label(ventana,text="aleatorios entre 0 y 10")
lbl1.grid(row=0,column=0)
bt1=Button(ventana,text="generar 1",command=num_aleatorios1)
bt1.grid(row=0,column=1)

lbl2=Label(ventana,text="",bg="#003245",font=10,fg="#fff")
lbl2.grid(row=1,column=0)



lbl3=Label(ventana,text="aleatorios entre 0 y 50")
lbl3.grid(row=0,column=2)
bt2=Button(ventana,text="generar 2",command=num_aleatorios2)
bt2.grid(row=0,column=3)

lbl3=Label(ventana,text="",bg="#003245",font=10,fg="#fff")
lbl3.grid(row=1,column=2)

ventana.configure(background="#003245")
ventana.mainloop()

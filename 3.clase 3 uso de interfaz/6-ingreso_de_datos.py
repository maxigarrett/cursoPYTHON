
from tkinter import *

ventana=Tk()
ventana.title("ingreso de datos")
ventana.resizable(0,0)#evitamos la redimencion de la ventana por el usuario
ventana.geometry("600x400")#le damos unas dimenciones



""" entry es para crear una caja de texto y le damos el ancho con width
caja=Entry(width=30)
caja.grid(row=0,column=0)"""

#EJERCICIO
"""Veamos como recuperar y utilizar dicho valor haciendo un ejemplo práctico de un programa que nos permita escribir una palabra, 
y luego, presionando un botón, nos muestre dicha palabra por pantalla."""
def clic():
    mensaje=texto.get()
    etiqueta2.config(text=mensaje)

etiqueta1=Label(ventana,text="texto a ingresar")
etiqueta1.grid(row=0,column=0)
etiqueta2=Label(ventana,text="se imprimira aqui")
etiqueta2.grid(row=1,column=0)

texto=Entry(ventana,width=30)
texto.grid(row=0,column=1)

boton1=Button(ventana,text="Aceptar",command=clic)
boton1.grid(row=0,column=2)

ventana.configure(background="#003245")
ventana.mainloop()
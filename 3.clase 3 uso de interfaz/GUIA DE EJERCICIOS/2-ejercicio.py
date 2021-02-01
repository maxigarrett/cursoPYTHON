"""Modificar el código del ejemplo de la página 15 del apunte de la clase 3 para que, además de mostrar mediante una etiqueta
 el texto que ingresamos en la caja de texto, luego de hacerlo, borre todo el contenido de dicha caja de texto, limpiando el 
 formulario antes del próximo ingreso."""
from tkinter import *

ventana=Tk()
ventana.title("ingreso de datos")
ventana.resizable(0,0)#evitamos la redimencion de la ventana por el usuario
ventana.geometry("600x400")#le damos unas dimenciones





#EJERCICIO
"""Veamos como recuperar y utilizar dicho valor haciendo un ejemplo práctico de un programa que nos permita escribir una palabra, 
y luego, presionando un botón, nos muestre dicha palabra por pantalla."""
def clic():
    mensaje=texto.get()
    etiqueta2.config(text=mensaje)
def borrar():
    texto.delete(0,END)
    etiqueta2.config(text="se imprimira aqui")

etiqueta1=Label(ventana,text="texto a ingresar")
etiqueta1.grid(row=0,column=0)
etiqueta2=Label(ventana,text="se imprimira aqui")
etiqueta2.grid(row=1,column=0)

texto=Entry(ventana,width=30)
texto.grid(row=0,column=1)

boton1=Button(ventana,text="Aceptar",command=clic)
boton1.grid(row=0,column=2)
boton2=Button(ventana,text="Borrar",command=borrar)
boton2.grid(row=0,column=3)

ventana.configure(background="#003245")
ventana.mainloop()
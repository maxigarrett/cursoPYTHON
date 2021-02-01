
from tkinter import *

ventana=Tk()
ventana.title("ventana")
ventana.resizable(0,0)#evitamos la redimencion de la ventana por el usuario
ventana.geometry("600x400")#le damos unas dimenciones


"""Atributo COMMAND.
Este atributo del botón nos permite definir el código a ejecutar cada vez que el botón sea presionado.
Veamos un ejemplo con dos botones cada uno asociado a una función diferente:
"""
def clic_uno():
    lbl_uno.configure(text="se preciono el boton 1")
def clic_dos():
    lbl_uno.configure(text="se preciono el boton 2")

    
boton1=Button(ventana,text="boton 1",bg="black",fg="green",command=clic_uno)
boton1.grid(row=1,column=1)
boton2=Button(ventana,text="boton 2",bg="black",fg="green",command=clic_dos)
boton2.grid(row=1,column=2)

lbl_uno=Label(ventana,text="precione un boton")
lbl_uno.grid(row=2,column=0)

ventana.mainloop()
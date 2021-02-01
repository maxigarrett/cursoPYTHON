
from tkinter import *

ventana=Tk()
ventana.title("ventana")
ventana.resizable(0,0)#evitamos la redimencion de la ventana por el usuario
ventana.geometry("600x400")#le damos unas dimenciones

etiqueta1=Label(ventana,text="titulo del programa",bg="#003245",fg="#fff")
etiqueta1.grid(row=0,column=0)

"""RELIEVES: los botones tienen una propiedad para el relieve, la forma en que se verán por pantalla.
Esta propiedad es RELIEF y puede tomar los valores FLAT, SUNKEN, RIDGE o SOLID.
"""
boton1=Button(ventana,text="simple",bg="black",fg="green")
boton1.grid(row=1,column=1)
boton2=Button(ventana,text="flat",bg="black",fg="green",relief=FLAT)
boton2.grid(row=1,column=2)
boton3=Button(ventana,text="suncken",bg="black",fg="green",relief=SUNKEN)
boton3.grid(row=1,column=3)
boton4=Button(ventana,text="ridge",bg="black",fg="green",relief=RIDGE)
boton4.grid(row=1,column=4)
boton4=Button(ventana,text="solid",bg="black",fg="green",relief=SOLID)
boton4.grid(row=1,column=5)
ventana.configure(background="#003245")

ventana.mainloop()
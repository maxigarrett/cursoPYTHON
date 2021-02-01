
from tkinter import *
from tkinter import messagebox as MessageBox

ventana=Tk()
ventana.title("ingreso de datos")
ventana.resizable(0,0)#evitamos la redimencion de la ventana por el usuario
ventana.geometry("600x400")#le damos unas dimenciones



"""Mensajes.
Para mostrarle mensajes emergentes al usuario, vamos a utilizar el módulo MESSAGEBOX.
Veamos un ejemplo simple de como funciona, haciendo un programa que muestre dos botones y que, al presionarlo, salga un mensaje
emergente diferente para cada uno.
"""

def text_a():
    MessageBox.showinfo("Mensaje","Exelente")
def text_b():
    MessageBox.showinfo("Mensaje","No sabes nada de futbol")

bt1=Button(ventana,text="Soy de chaca",command=text_a)
bt1.grid(row=0,column=0)
bt2=Button(ventana,text="Soy de otro club",command=text_b)
bt2.grid(row=1,column=0)
ventana.configure(background="#003245")
ventana.mainloop()
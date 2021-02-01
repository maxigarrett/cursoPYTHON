#Con esto, tenemos disponibles todos los métodos y funcionalidades de la librería para utilizar en nuestro programa.
from tkinter import *

#El segundo paso es crear nuestro contenedor principal, la raíz de nuestra interfaz, y para ello le tenemos que dar un nombre,
# por ejemplo, “ventana”.
ventana=Tk()
ventana.title("ventana")
ventana.resizable(0,0)#evitamos la redimencion de la ventana por el usuario
ventana.geometry("600x400")#le damos unas dimenciones

#CREAMOS LABEL Y LE DECIMOS EN QUE POSICION DE LA VENTANA VA A IR CON GRID
etiqueta1=Label(ventana,text="etiqueta 1")
etiqueta1.grid(row=0,column=1)
etiqueta2=Label(ventana,text="etiqueta 2")
etiqueta2.grid(row=1,column=0)
etiqueta3=Label(ventana,text="etiqueta 3")
etiqueta3.grid(row=1,column=2)

#A continuación, creamos un bucle dentro del cual estará contenido nuestro programa:
ventana.mainloop()

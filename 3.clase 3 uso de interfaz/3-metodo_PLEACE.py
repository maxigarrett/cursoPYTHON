"""Método PLACE.
Como vimos, el método GRID es muy útil si queremos ubicar varios elementos dentro de nuestra ventana (en este caso etiquetas)
 sin necesidad de andar calculando coordenas de X e Y, pero no es muy cómodo si lo que queremos es colocar nuestro elemento 
 exactamente en una coordenada.
Veamos cómo podemos usarlo para colocar nuestra etiqueta, por ejemplo, en las coordenas x=50 e y=1
"""

from tkinter import *

ventana=Tk()
ventana.title("ventana")
ventana.resizable(0,0)#evitamos la redimencion de la ventana por el usuario
ventana.geometry("600x400")#le damos unas dimenciones

etiqueta1=Label(ventana,text="etiqueta 1",font=("calibri",20),bg="black",fg="red")
etiqueta1.place(x=80,y=110)

ventana.configure(background="#003245")

ventana.mainloop()
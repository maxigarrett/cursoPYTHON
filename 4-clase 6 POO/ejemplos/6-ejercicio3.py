"""Crear una clase Persona con un método INIT que haga posible que, al instanciarla, es decir, al crear un objeto,
 nos solicite un valor para el atributo nombre, un valor para el atributo apellido y finalmente muestre un mensaje saludando,
  con nombre y apellido, a la persona recién creada."""

class Persona:
    nombre=''
    apellido=''
    def __init__(self):
        self.nombre=input("nombre")
        self.apellido=input("apellido")
        print("Hola",self.nombre,',',self.apellido)
jose=Persona()

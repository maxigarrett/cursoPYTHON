class Empleado:
    nombre=""
    apellido=""
    def __init__(self):
        self.nombre=input("nombre")
        self.apellido=input("apellido")

    # modificamos el metodo por defecto para que devuelva un los valores al llamar a la clase solamente y no sus atributos 
    def __str__(self):
        mensaje=self.apellido+','+self.nombre
        return mensaje

empleado_uno = Empleado()
print(empleado_uno)

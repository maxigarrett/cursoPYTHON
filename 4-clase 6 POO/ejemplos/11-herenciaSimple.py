class Empleado:
    nombre=""
    apellido=""
    def __init__(self):
        self.nombre=input("nombre")
        self.apellido=input("apellido")

# usamos pass para llamar a la clase padre si solo vamos a utilizar los mismos atributos y metodos
class Gerencia(Empleado):
    pass

fac=Gerencia()
print(fac.nombre,",",fac.apellido)
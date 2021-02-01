class Empleado:
    nombre=""
    apellido=""
    def __init__(self):
        self.nombre=input("nombre")
        self.apellido=input("apellido")

#eredamos poniendo entre parentecis la clase a Heredar entonces ademas de pedir nombre y apellido va  a pedir la gerencia
# tambien usamos super para llamar a la clase padre de la clase heredada que es el constructor
class Gerencia(Empleado):
    gerencia=""
    def __init__(self):
        super().__init__()#usamos super para llamar a la clase padre con su metodo constructor
        self.gerencia=input("gerencia?")

fac=Gerencia()
print(fac.nombre,",",fac.apellido,"gerencia",fac.gerencia)

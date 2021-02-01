"""Crear una clase Alumno que al instanciarse pida nombre, apellido y nota final de un alumno.
Sobrescribir el método especial STR para que, al imprimir los objetos, se vea por pantalla el nombre, apellido, nota final y
un mensaje (‘Promoción’ si la nota es igual o mayor a 7, ‘Final’ si la nota es mayor o igual a 4 y menor a 7 y ‘Recursa’ si la
nota es menor a 4).
Instanciar la clase y probar el método.
"""

class Alumno:
    nombre=""
    apellido=""
    notaFinal=0
    def __init__(self):
        self.nombre=input("nombre")
        self.apellido=input("apellido")
        self.notaFinal=input("nota final")
    def __str__(self):
        if(self.notaFinal<='3'):
            mensaje="reprueba el alumno "+self.nombre+" "+self.apellido+" nota final:"+self.notaFinal
            return mensaje
        if(self.notaFinal<='4'):
            mensaje="Va a final el alumno "+self.nombre+" "+self.apellido+" nota final:"+self.notaFinal
            return mensaje
        if(self.notaFinal>='7'):
            mensaje="Promociona el alumno "+self.nombre+" "+self.apellido+" nota final:"+self.notaFinal
            return mensaje
alumno=Alumno()
print(alumno)
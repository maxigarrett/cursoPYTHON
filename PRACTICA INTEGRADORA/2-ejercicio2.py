alumnos=[]

todos=[]
class Alumno:
    apellido=""
    notaFinal=0
    def __init__(self,apellido,ntf):
        self.apellido=apellido
        self.notaFinal=ntf
    def __str__(self):
           
        mensaje="El alumno {} tiene nota final de {}".format(self.apellido,self.notaFinal)
        return mensaje

alumnos= [Alumno("garrett",7),Alumno("Pepe",9),Alumno("falabella",4),Alumno("reinoso",1),Alumno("Diz",5),Alumno("gonzales",8),
Alumno("casado",3),Alumno("borau",9),Alumno("beyer",2),Alumno("gomez",10)]






todos=list(map(lambda alumn: Alumno(alumn.apellido , alumn.notaFinal ),alumnos))

todos_notas=[]
desicion=[]
for i in todos:
    if (i.notaFinal > 6):
        todos_notas.append(i)
        desicion="aprobó"
        todos_notas.append(desicion)
    elif (i.notaFinal < 7 and i.notaFinal > 3):
        todos_notas.append(i)
        desicion="FINAL"
        todos_notas.append(desicion)
    elif(i.notaFinal < 4):
        todos_notas.append(i)
        desicion="recursa"
        todos_notas.append(desicion)


# recorremos todos_notas que guardan los aprobados y desaprobados y lo guardamos en el array todos que usa la funcion map
for i in todos_notas:
    todos.append(i) 

    print("",i)
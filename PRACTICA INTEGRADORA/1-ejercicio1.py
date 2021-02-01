"""1.1 Escribir una clase llamada Alumno, con un método constructor que reciba como parámetros el apellido y la nota final del alumno.

1.2 Sobrescribir el método STR para que devuelva el nombre del alumno y la nota con el siguiente formato:
El alumno (acá va el nombre) tiene nota final (acá va la nota)

1.3 Crear una lista de objetos, preferentemente instanciando la clase dentro de la lista para simplificar el código, con al menos 10
nombresy 10 notas finales entre 1 y 10.

1.4 Combinando la función FILTER con funciones LAMBDA, crear tres listas de objetos, una con alumnos que recursan (nota final 1,2 o 3), 
una con alumnos que van a final (nota final 4,5 o 6) y otra con alumnos que promocionan (nota final 7,8,9 o 10).
"""
from os import system

alumnos=[]
alumnos_recursan=[]
alumnos_final=[]
alumnos_promocionan=[]
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

opcion=""
print("verificar alumnos")
# funcion filter para mostrar alumnos reprobados
print("\n")

# alumn es un parametro y usamos la propiedad notaFinal de la clase Alumno y despues al final ponemos el objeto a recorrer y filtar
#  que es el Array de objeto alumnos
print("elija una opcion:\n0-Salir\n1-Mostar Alumnos\n2-Alumnos Recursantes\n3-alumnos a Final\n4Alumnos que promocion\n5-ejericio 2 MAP\n6-Factorial de un numero com REDUCE")
opcion=int(input())


# PRECIONE ENTER DESPUES DE ELEGIR CADA OPCION PARA VOLVER AL MENU
while True:
    if(opcion==0):
        break
    elif (opcion==1):
        for i in alumnos:
            print(i)
        input()
        system("cls")
    elif (opcion==2):
        alumnos_recursan=list(filter(lambda alum: alum.notaFinal < 4,alumnos))
        print("-----------------recursan--------------------")
        for i in alumnos_recursan:#recursan
            print(i)
        input()
        system("cls")
    elif (opcion==3):
        alumnos_final=list(filter(lambda alum: alum.notaFinal < 7 and alum.notaFinal> 3,alumnos)) 
        print("------------final----------------------------")    
        for i in alumnos_final:#final
            print(i)
        input()
        system("cls")
    elif (opcion==4):
        alumnos_promocionan=list(filter(lambda alum: alum.notaFinal >= 7,alumnos))
        print()
        print("------------promocionan----------------------------")  
        for i in alumnos_promocionan:#Promocionan
            print(i)
        input()
        system("cls")
    elif (opcion==5):
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

         # recorremos todos_notas que guardan los aprobados y desaprobados y lo guardamos en el array todos[] que usa la funcion map
        for i in todos_notas:
            todos.append(i) 

            print("",i)
        input()
        system("cls")
    elif (opcion==6):
        from functools import reduce
        n=int(input("digite un nuermo para sacar el factorial"))
        def fact(n):
            return reduce(lambda x,y:x*y, range(2,n+1), 1)
        print(fact(n))
        input()
        system("cls")      
    else:
        print("opcion incorrecta")
        input()
        system("cls")
    print("elija una opcion:\n0-Salir\n1-Mostar Alumnos\n2-Alumnos Recursantes\n3-alumnos a Final\n4-Alumnos de promocion\n5-ejericio 2 MAP\n6-Factorial de un numero com REDUCE")
    opcion=opcion=int(input())
    

    system("cls")
    
print("Fin de verificacion")  











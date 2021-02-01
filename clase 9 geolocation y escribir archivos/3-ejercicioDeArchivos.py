"""Ejercicio propuesto: Escribir un programa que solicite el ingreso por teclado de los datos de un cliente
 (DNI, apellido y nombre) y le pregunte al usuario si desea seguir cargando datos (las opciones son s/n).
Una vez terminada la carga de datos, guardarlos en un archivo.
"""
# lista=[]
# respuesta="s"

# while respuesta=="s":
#     dni=input("ingrese el dni")
#     apellido=input("ingrese el apellido")
#     nombre=input("ingrese el nombre")
#     lista.append(dni)
#     lista.append(apellido)
#     lista.append(nombre)

#     print("\n")
#     respuesta= input("desea ingresar mas (s/n)")
#     if(respuesta!="s"):
#         break

# print(lista)
# txt=open("C:/Users/usuario/Desktop/CURSO PYTHON/texto.txt","w")
# txt.write(str(lista))
# txt.close()

# otra solucion mas amigable al leer archivos de texto

respuesta="s"
txt=open("C:/Users/usuario/Desktop/CURSO PYTHON/texto.txt","w")
while respuesta=="s":
    dni=input("ingrese el dni")
    apellido=input("ingrese el apellido")
    nombre=input("ingrese el nombre")
    txt.write(dni+","+apellido+","+nombre +"\n")#escribimos cada vuelta de bucle si queremos agregar mas en ves de hacer una lista
    print("\n")
    respuesta= input("desea ingresar mas (s/n)")
    if(respuesta!="s"):
        break


txt.close()

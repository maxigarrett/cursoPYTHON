txt=open("C:/Users/usuario/Desktop/CURSO PYTHON/texto.txt","r")
contenido=txt.readline()
while contenido!="":
    # buscamos el dni 33333
    # Modificamos el código que leía línea a línea para que busque un determinado número de DNI y en caso de encontrarlo,
    #  mostrar por pantalla todo el registro.
    dni=contenido[0:5]
    if dni=="33333":
        print(contenido)
    else:
        print("erro")
    contenido=txt.readline()
txt.close()

"""Modificar el código del ejercicio para que pida un DNI por teclado y muestre un mensaje en caso de no
encontrarse el DNI buscado."""
txt=open("C:/Users/usuario/Desktop/CURSO PYTHON/texto.txt","r")
dni_buscado=input("ingrese dni a buscar")
contenido=txt.readlines()
for i in contenido:
    # [:]si nno especificamos nada a la izquieda arranca de 0 y desoues el largo del dni
    if(dni_buscado==i[:len(dni_buscado)]):
        lista_datos=i#si lo encuebtra lo guarda en una variable con todos los datos
        break
print(lista_datos)
txt.close()
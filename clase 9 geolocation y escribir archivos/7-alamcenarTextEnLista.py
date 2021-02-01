# Mediante el uso del método READLINES podemos almacenar en una lista, las líneas de texto recuperadas de nuestro archivo.
# mediant el uso de este ,etodo carga cada entrada en un elemento de lista
# txt=open("C:/Users/usuario/Desktop/CURSO PYTHON/texto.txt","r")
# contenido=txt.readlines()
# print('la lista tiene:',str(len(contenido)),"elementos")

# for i in contenido:
#         print(i)
# txt.close()


# BUSCAMOS LE DNI 3333 o con un input el dni que dijite el usuario
txt=open("C:/Users/usuario/Desktop/CURSO PYTHON/texto.txt","r")
dni_buscado=input("ingrese dni a buscar")
contenido=txt.readlines()
for i in contenido:
    if(dni_buscado==i[:len(dni_buscado)]):
        lista_datos=i
        break
print(lista_datos)
lista_datos=lista_datos.split(",")#usamos split para que cada espacio en blanco le meta una coma y convertimos en array
print(lista_datos)
txt.close()
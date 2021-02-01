"""Python nos provee de herramientas muy simples para generar un respaldo de los datos que estamos trabajando en archivos 
de texto.Veamos un ejemplo sencillo:
"""
"""txt=open("texto.txt","w")"""#abrimos un archivo exista o no lo nombramos y la "w" es decir q es de escrotura osea write
"""txt.write("linea 1\n")"""#las lineas que deseamos escribir y guardar
"""txt.write("linea 2\n")"""
"""txt.write("linea 3\n")"""
"""txt.close()"""#cerramos la conexion con el archivo

# el ejmplo anterior si volvemos a  guardar otra cosa se pisa y deja solo el ultimo agregado
# podemos especificar la ruta donde queremos poner el archivo por ejemplo txt=open("c:/CURSO PYTHON/texto.txt","w")
txt=open("texto.txt","w")

lista1=str([1,2,3,4,5])+"\n"
lista2=str([11,12,13,14,15])+"\n"
lista3=str([21,22,23,24,25])+"\n"

txt.write(lista1)
txt.write(lista2)
txt.write(lista3)

txt.close()
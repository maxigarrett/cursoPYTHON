"""Escribir un programa que le pregunte al usuario cuantas palabras desea ingresar, luego le permita ingresarlas todas y
 finalmente mostrarlas por pantalla"""

array_palabras=[]

cantidad_palabras=int(input("cuantas palabras desea ingresar\n"))

for item in range(0,cantidad_palabras):
     palabra=input("ingrese una palabra\n")
     array_palabras.append(palabra)
print(array_palabras)
"""Crear una lista con 10 números enteros y mostrarlos por pantalla.
Luego reemplazar todos los números pares por la palabra PAR y volver a mostrar la lista por pantalla.
"""
array_numeros=[]
for item in range(1,4+1):
    numeros=int(input("ingrese un numero"))
    array_numeros.append(numeros)
print(array_numeros)

for item in range(0,len(array_numeros)):
    if(array_numeros[item] %2 ==0):
        array_numeros[item]='par'
print(array_numeros)
    


    
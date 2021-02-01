#Escribir un programa que permita al usuario ingresar por teclado tantos números enteros como desee. Cuando no quiera ingresar
#más números, deberá ingresar el cero.
#A continuación, determinar cuál de los números ingresados es el mayor y cuál es el menor. Mostrar ambos por pantalla.


numero=int(input("ingrese un numero o  (0 para salir)"))
mayor=[]
while numero!=0:
   numero=int(input("ingrese un numero (0 para salir)"))
   mayor.append(numero)

print("el mayor es:",max(mayor),"y el meno es",min(mayor))
    

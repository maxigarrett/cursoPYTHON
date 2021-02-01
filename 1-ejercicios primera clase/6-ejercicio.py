#Pedirle al usuario que ingrese dos números enteros por teclado y contar cuantos números pares hay entre ambos valores ingresados.
numero1=int(input("ingrese un numero entero"))
numero2=int(input("ingrese otro numero entero"))
contador=0
if(numero1==0 or numero2==0):
    print("ingrse numeros mayor a 0")
else:
    for item in range(numero1,numero2 +1):
        if(item %2==0):
            print(item)
            contador+=1
    print("los numero pares encontrados entre",numero1,"y",numero2," son:",contador)
        
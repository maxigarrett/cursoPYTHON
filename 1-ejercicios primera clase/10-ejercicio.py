#Escribir una función para determinar si un número entero, ingresado por teclado es un número primo.
#Un número primo es aquel que solo tiene como divisores enteros (resto igual a cero) al número 1 y a sí mismo, por ejemplo, 
#el número 5.
def es_primo(num):
    if num < 2:     #si es menos que 2 no es primo, 
        print("no es primo")
    for i in range(2, num +1):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:    #si el resto da 0 no es primo, 
            print(i,"no es primo")
        else:
            print(i,"esprimo")    #de lo contrario devuelve Verdadero

es_primo(25)    #para probarlo llamamos a la función

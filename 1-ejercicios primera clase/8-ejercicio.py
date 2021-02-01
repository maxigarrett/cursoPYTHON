#Escribir un programa que pida al usuario, que ingrese una frase por teclado.
#El programa deberá tener dos funciones, una que reciba la frase y devuelva solo las vocales de dicha frase y otra función que 
#reciba la misma frase pero que devuelva solo las consonantes.
#Mostrar por pantalla la frase original ingresada por el usuario, las vocales y las consonantes devueltas por sus respectivas
#funciones.



textoPalabra=input("ingrese una palbra para mostrar las vocales")

def contar_vocales(texto):
    contadorVocales=0   
    for item in (texto):
        if (item=='a' or item=='e' or item=='i' or item=='o' or item=='u'):
            contadorVocales+=1
        else:
            contadorVocales+=0

    return print('vocales',contadorVocales)   
  

def contar_consonantes(texto):
    contadorConsonantes=0  
    for item in (texto):
        if (item=='a' or item=='e' or item=='i' or item=='o' or item=='u'):
            contadorConsonantes+=0
        else:
            contadorConsonantes+=1
    return print('consonantes',contadorConsonantes)   

print('palabra',textoPalabra)
contar_vocales(textoPalabra)
contar_consonantes(textoPalabra)

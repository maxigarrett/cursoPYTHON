"""La mejor definición de funciones LAMBA la podemos sacar de la documentación oficial de Python:
https://docs.python.org/3/faq/design.html#why-can-t-lambda-expressions-contain-statements

una forma abreviada de definir funciones sin necesidad de ponerles un nombre, por lo que comúnmente leemos en algunos textos que se 
trata de funciones anónimas.
La sintaxis es muy sencilla, utilizando la palabra reservada LAMBDA seguida de los parámetros, dos puntos y a continuación la condición

"""
# EJEMPLO
# Veamos un ejemplo sencillo, una función LAMBA que nos devuelva el producto de dos números

#funcion simple
def producto(x,y):
    return x*y

# funcion LAMBDA
lambda x,y:  x*y 

# La primera es la definición tradicional que conocemos, en la que asignamos a la función un nombre.
# La segunda es la función LAMBDA, ambas hacen exactamente lo mismo.
# Para utilizar una función de estas, tenemos que asignársela a una variable, por ejemplo
producto=lambda x,y:  x*y 
print(producto(2,2))

"""Esta función toma como entrada, una función y una lista de elementos sobre los cuales aplicará dicha función.
Es decir, utiliza todos los elementos de la lista como argumento para la función que pasamos como argumento, y nos devuelve una lista
 filtrada solo con los elementos que satisfacen a la función simple pasada como argumento.

EJEMPLO
Veamos un ejemplo sencillo.
Vamos a escribir dos funciones simples, una que determine si un valor es múltiplo de 3 y otra que determine si un valor es múltiplo de 5.
Luego vamos crear una lista con números y, mediante el uso de la función FILTER, vamos a extraer de dicha lista, primero los múltiplos 
de 3 y luego los múltiplos de 5.
"""


# Paso 1: escribimos las funciones simples.
def m3(v):
    if(v % 3==0):
        return True

def m5(v):
    if(v % 5==0):
        return True

# Paso 2: creamos una lista de números.
lista=[23,12,4,7,33,75,2,9,10]

# Paso 3: Utilizamos la funcion FILTER en ambas funciones
print(list(filter(m3,lista)))
print(list(filter(m5,lista)))
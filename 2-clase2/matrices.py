#MATRICES
linea1=[1,2,3]
linea2=[4,5,6]
linea3=[7,8,9]
matriz=[linea1,linea2,linea3]

print(matriz)
print(matriz[0][0])#saldra el 1 porque esta en la fila 0 colmna 0
print(matriz[1][2])
#---------------------------------------------------------

print()
print()
#recorremos la matriz
linea4=[1,2,3]
linea5=[4,5,6]
linea6=[7,8,9]
matriz=[linea4,linea5,linea6]

#esto va a ir a los for para recorrer la matriz tambien lo podemos almacenar en una variable
print(len(matriz))
print(len(matriz[0]))#mostra toda la fila 0 por lo que sabremos la cantidad de columnas que hay que son 3 con metodo len lo sabemos

for fila in range(0,len(matriz)):
    for columnas in range(0,len(matriz[0])):
        print(matriz[fila][columnas],end=',')#evitamos salto de lineas con end
    print("\n")

        
    
# ------------------------------------------------------------


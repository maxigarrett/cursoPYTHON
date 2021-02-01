txt=open("C:/Users/usuario/Desktop/CURSO PYTHON/texto.txt","r")
contenido=txt.readline()#metodo READLINE diferente de REDLINES este lee linea a linea 
while contenido!="":
    print(contenido,end="")
    contenido=txt.readline()
txt.close()
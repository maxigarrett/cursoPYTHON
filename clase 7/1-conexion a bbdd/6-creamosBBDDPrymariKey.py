import sqlite3
conexion= sqlite3.connect("base_de_datos.db")
cursor=conexion.cursor()

# creamos tabla y para ponerlo en varias lineas utilizamos comillas triple
# lo comentamos porque tira error si creamos de nuevo  la misma tabla
# cursor.execute("""
#     create table contactos(
#     dni varchar(8) primary key,
#     apellido varchar(100),
#     nombre varchar(100))
# """)
    
lista=[("666","corona","virus"),("999","gandalf","elgris")]
cursor.executemany("insert into contactos values (?,?,?)",lista)


# confirmamos la transaccion para que pueda insertar la info a la bbdd
conexion.commit()
conexion.close()
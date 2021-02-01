import sqlite3
conexion= sqlite3.connect("base_de_datos.db")
cursor=conexion.cursor()

# creamos tabla si lo ejecutamos dos veces tira error porque la tabla ya esta creada
# conexion.execute("create table clientes (dni integer, apellido varchar(100),nombre varchar(100) )")



conexion.close()
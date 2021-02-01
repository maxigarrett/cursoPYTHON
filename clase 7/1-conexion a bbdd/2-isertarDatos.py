import sqlite3
conexion= sqlite3.connect("base_de_datos.db")
cursor=conexion.cursor()

cursor.execute("insert into clientes values(1111,'garrett','maxi') ")
cursor.execute("insert into clientes values(1111,'garrett','jose') ")

# confirmamos la transaccion para que pueda insertar la info a la bbdd
conexion.commit()
conexion.close()
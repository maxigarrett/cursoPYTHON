import sqlite3
conexion= sqlite3.connect("base_de_datos.db")
cursor=conexion.cursor()

cursor.execute("select * from clientes")

registro=cursor.fetchall()

for cliente in registro:
    print("DNI",registro[0])
    print("APELLIDO",registro[1])
    print("NOMBRE",registro[2])
    print()
    


# confirmamos la transaccion para que pueda insertar la info a la bbdd
conexion.commit()
conexion.close()
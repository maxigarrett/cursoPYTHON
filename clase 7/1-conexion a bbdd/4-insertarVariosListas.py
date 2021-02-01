import sqlite3
conexion= sqlite3.connect("base_de_datos.db")
cursor=conexion.cursor()

# creamos un array con clientes
nuevos_clientes=[(222,"fernandez","roman"),(555,"alvaro","lautaro")]

# insertamos de forma masiva
cursor.executemany("insert into clientes values (?,?,?)",nuevos_clientes)


# confirmamos la transaccion para que pueda insertar la info a la bbdd
conexion.commit()
conexion.close()
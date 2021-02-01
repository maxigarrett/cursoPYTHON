import sqlite3
conexion= sqlite3.connect("base_de_datos.db")
cursor=conexion.cursor()

# creamos tabla y para ponerlo en varias lineas utilizamos comillas triple
# LA DE SOCIOS NO ANDA ENTONCES CREAMOS ESTA
# cursor.execute("""
#     create table socios2(
#     dc_socios integer primary key autoincrement,
#     apellido varchar(100),
#     nombre varchar(100))
    
# """)

socio=[("PEPE","asas"),("garrett","jjjjj")]
cursor.executemany("insert into socios2 values (null,?,?)",socio)


# confirmamos la transaccion para que pueda insertar la info a la bbdd
conexion.commit()
conexion.close()
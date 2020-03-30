import sqlite3
conexion = sqlite3.connect("database.sqlite")
cursor = conexion.cursor()
#cursor.execute("CREATE TABLE personas(nombre TEXT, edad NUMERIC)")
personas = (("Damian",32),("Jorge",44),("Clara",24))
for nombre,edad in personas:
    cursor.execute("INSERT INTO personas VALUES(?,?)",(nombre,edad))

cursor.execute("SELECT * FROM personas")
datos = cursor.fetchall()
print(datos)
conexion.commit()

conexion.close()
import sqlite3 as sq
#Productos en sqlite
conexion = sq.connect("productos.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE Producto (id INT primary key, nombre TEXT, precio INT)")
filas = ((1, "Teclado", 500),(2, "Mouse", 350),(3, "Monitor", 1500),(4, "Parlantes", 1100))
for id,nombre,precio in filas:
    cursor.execute("INSERT INTO Producto VALUES(?,?,?)",(id,nombre,precio))

cursor.execute("SELECT * FROM Producto")
consulta = cursor.fetchall()
print(consulta)
conexion.commit()
conexion.close()
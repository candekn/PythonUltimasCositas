import pymysql
#MySql 
conexion = pymysql.connect(host="remotemysql.com", port=3306, user="RYrlWxWfCO", passwd="aUwiBBth6c", db="RYrlWxWfCO")
cursor = conexion.cursor()
id = 0
personas = (("Ana",22),("Clara",27),("Sonia",41))

try:
    cursor.execute("CREATE TABLE Persona (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, nombre TEXT, edad SMALLINT)")
except:
    print("No se pudo crear la tabla")
    
#for nombre,edad in personas:
   cursor.execute("INSERT INTO Persona(nombre,edad) VALUES(%s,%s)",(nombre,edad))

print("Datos ingresados correctamente")
cursor.execute("SELECT id, nombre, edad FROM Persona")
datos = cursor.fetchall()
print(datos)
conexion.commit()
conexion.close()

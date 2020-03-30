#programa q cree una tabla: Producto(id, nombre, precio)
#pedir al usuario datos y agregar a la tabla
#al finalizar commit, close.
#Despues volver a abrir la conexion y traer todo
import pymysql
import sys


try:
    conexion = pymysql.connect(host="remotemysql.com", port=3306, user="RYrlWxWfCO", passwd="aUwiBBth6c", db="RYrlWxWfCO")
except pymysql.err.OperationalError:
    print("No se pudo conectar a la base de datos. Verifique que los datos sean correctos")
    sys.exit()
cursor = conexion.cursor()
try:
    cursor.execute("CREATE TABLE Producto (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(60) NOT NULL, precio NUMERIC NOT NULL)")
except pymysql.err.InternalError:
    print("La Tabla a crear ya existe")
    
def Menu():
    print("\nOpciones disponibles: ")
    print("1.Agregar Producto")
    print("2.Mostrar todos los productos: ")
    print("3.Salir")
    op = input("Ingrese opcion deseada: ")
    return op

def ConvertirPrecio(precio):
    try:
        precio = int(precio)
    except (ValueError,TypeError):
        print("El precio ingresado no es valido")
        precio = 0
    return precio

def InsertarProducto(nombre,precio):
    try:
        cursor.execute("INSERT INTO Producto(nombre,precio) VALUES (%s,%s)",(nombre,precio))
    except:
        conexion.rollback()
        raise
    else:
        conexion.commit()


print("\nBienvenido")

while True:
    op = Menu()
    if op=="3":
        conexion.close()
        print("Gracias por utilizar este programa")
        break
    elif op=="1":
        nombre = input("\nIngrese nombre de producto: ")
        while True:
            precio = input("Ingrese precio de producto: ")
            precio = ConvertirPrecio(precio)
            if precio!=0:
                InsertarProducto(nombre,precio) 
                break
    elif op=="2":
        cursor.execute("SELECT id, nombre, precio FROM Producto")
        datos = cursor.fetchall()
        print("--ID-|-NOMBRE-|-PRECIO--")
        for i, n, p in datos:
            print("--"+str(i)+"-|-"+n+"-|-$"+str(p)+"--")
    else:
        print("Opcion ingresada no válida")
            
    




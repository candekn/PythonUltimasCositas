#Bases de datos: SQLServer
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TRAINING-05\SQLEXPRESS;'
                      'Database=dbCurso;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Categoria')
for row in cursor:
    print(row)

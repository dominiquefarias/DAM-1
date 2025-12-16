import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",        
  user="dominique3",        
  password="Domi123$",     
  database="portafolioexamen"   
)

cursor = conexion.cursor(dictionary=True) # Diccionario
cursor.execute('''
	SELECT
	nombre AS "Nombre del cliente",
	apellidos AS "apellidos del cliente",
	edad AS "Edad del cliente"
''')

filas = cursor.fetchall()

print(filas)

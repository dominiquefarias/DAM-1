import mysql.connector

conexion = mysql.connector.connect(
  host="localhost",        
  user="dominique3",        
  password="Domi123$",     
  database="portafolioexamen"   
)

cursor = conexion.cursor()
cursor.execute('''
	SELECT 
	COUNT(color) AS numero,
	color
	FROM productos
	GROUP BY color
	ORDER BY color ASC;
''');

filas = cursor.fetchall()

print(filas)

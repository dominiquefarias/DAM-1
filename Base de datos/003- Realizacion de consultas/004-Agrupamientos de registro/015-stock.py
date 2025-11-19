import mysql.connector
import matplotlib.pyplot as pt

conexion = mysql.connector.connect(
  host="localhost",        
  user="dominique3",        
  password="Domi123$",     
  database="portafolioexamen"   
)

cursor = conexion.cursor()
cursor.execute('''
	SELECT 
	COUNT(stock) AS numero,
	color
	FROM productos
	GROUP BY stock
	ORDER BY numero DESC;
''');

filas = cursor.fetchall()
cantidades = []
etiquetas = []
for fila in filas:
	cantidades.append(fila[0])
	etiquetas.append(fila[1])
print(cantidades)
print(etiquetas)
pt.pie(cantidades,labels=etiquetas)
pt.show()

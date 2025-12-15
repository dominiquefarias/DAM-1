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
	FROM clientes
	ORDER BY edad DESC;
''')

filas = cursor.fetchall()
resultado_json = json.dumps(filas, ensure_ascii=False,indent=2)
print(resultado_json)

for fila in filas:
	print("Nombre",fila['Nombre del cliente'])
	print("Apellidos: ",fila['Apellidos del cliente'])
	print("Edad: ",fila['Edad del cliente'])
	print("###################")s

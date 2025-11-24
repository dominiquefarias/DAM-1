import mysql.connector 

conexion = mysql.connector.connect(
  host="localhost",
  user="tiendaclase1",
  password="Tiendaclase123$",
  database="tienda1"
)                                      
  
cursor = conexion.cursor() 
cursor.execute("SELECT * FROM clientes;")  

filas = cursor.fetchall()

print(filas)



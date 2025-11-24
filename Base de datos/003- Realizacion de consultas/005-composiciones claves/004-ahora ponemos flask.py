import mysql.connector
from flask import Flask
import json

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="tiendaclase1",
    password="Tiendaclase123$",
    database="tienda1"
)        
app = Flask(__name__)

@app.route("/clientes")
def inicio():
	cursor = conexion.cursor() 
	cursor.execute("SELECT * FROM clientes;")  

	filas = cursor.fetchall()
	return json.dumps(filas)

if __name__ == "__main__":
	app.run(debug=True)

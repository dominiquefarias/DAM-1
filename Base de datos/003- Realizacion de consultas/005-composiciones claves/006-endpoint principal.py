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

@app.route("/")
def raiz():
	return json.dumps(render_template("index.html"))

# http://127.0.0.1:5000/clientes
@app.route("/clientes")
def clientes():
	cursor = conexion.cursor() 
	cursor.execute("SELECT * FROM clientes;")  

	filas = cursor.fetchall()
	return json.dumps(filas)

# http://127.0.0.1:5000/tablas
@app.route("/tablas")
def tablas():
	cursor = conexion.cursor() 
	cursor.execute("SHOW TABLES;")  

	filas = cursor.fetchall()
	tablas = []
	for fila in filas:
		tablas.append(fila[0])
	return json.dumps(tablas)

if __name__ == "__main__":
	app.run(debug=True) 
    

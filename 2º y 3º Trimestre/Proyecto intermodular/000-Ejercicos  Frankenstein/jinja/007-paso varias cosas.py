from flask import Flask, render_template

import mysql.connector

print("Bienvenidos a la aplicación")

conexion = mysql.connector.connect(

  host="localhost",        

  user="dominique5",        

  password="Domi.virt3",     

  database="portafolioexamen"   
)
cursor = conexion.cursor()
cursor.execute("SHOW TABLES;")
tablas = []
filas = cursor.fetchall()
for fila in filas:
	tablas.append(fila[0])
	
cursor.execute("SHOW COLUMNS in piezasportafolio;")
columnas = []
filas = cursor.fetchall()
for fila in filas:
	columnas.append(fila[0])
	
cursor.execute("SELECT * FROM piezasportafolio;")
contenido_tabla = cursor.fetchall()

app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template(
		"backoffice.html",
		mis_tablas = tablas,
		mis_columnas = columnas,
		mi_contenido_tabla = contenido_tabla
	)
	
if __name__ == "__main__":
    app.run(debug=True)


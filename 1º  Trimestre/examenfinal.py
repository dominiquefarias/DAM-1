import mysql.connector

# Imprimo un mensaje de bienvenida en pantalla
print("Bienvenidos a la aplicación")

# Conexión con la base de datos MySQL
conexion = mysql.connector.connect(
  host="localhost",        
  user="dominique3",        
  password="Domi123$",     
  database="portafolioexamen"   
)

# Creo un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Menú principal del programa
while True:
  print("\nSelecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualizar registro")
  print("4.-Eliminar registro")
  print("5.-Salir")

  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripción: ")
    fecha = input("Introduce la fecha: ")
    id_categoria = input("Introduce la categoria: ")

    cursor.execute('''
      INSERT INTO piezasportafolio VALUES (
      NULL,
      "'''+titulo+'''",
      "'''+descripcion+'''",
      "'''+fecha+'''",
      '''+id_categoria+'''
      );
    ''')
    conexion.commit()
    print("✅ Registro insertado correctamente.")

  elif opcion == 2:
    cursor.execute('SELECT * FROM piezasportafolio;')
    filas = cursor.fetchall()
    print("Lista de registros:")
    for fila in filas:
      print(fila)

  elif opcion == 3:
    identificador = input("Introduce el ID a actualizar: ")
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripcion: ")
    fecha = input("Introduce la fecha: ")
    id_categoria = input("Introduce la categoria: ")

    cursor.execute('''
      UPDATE piezasportafolio SET 
      titulo = "'''+titulo+'''",
      descripcion = "'''+descripcion+'''",
      fecha = "'''+fecha+'''",
      id_categoria = '''+id_categoria+'''
      WHERE Identificador = '''+identificador+''';
    ''')
    conexion.commit()
    print("Registro actualizado correctamente")

  elif opcion == 4:
    identificador = input("Introduce el id a eliminar: ")
    cursor.execute('''
      DELETE FROM piezasportafolio
      WHERE Identificador = '''+identificador+''';
    ''')
    conexion.commit()
    print("Registro eliminado correctamente")

# Cierro el cursor y la conexión
cursor.close()
conexion.close()

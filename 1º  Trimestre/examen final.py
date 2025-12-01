# Importo el módulo mysql.connector que permite conectar python con bases de datos mysql
import mysql.connector

# Imprimo un mensaje de bienvenida en pantalla
print("Bienvenidos a la aplicacion")

# Aquí se indican los datos del servidor, el usuario, la contraseña y la base de datos
conexion = mysql.connector.connect(
  # Dirección del servidor 
  host="localhost",        
  # Nombre del usuario de 
  user="dominique3",        
  # Contraseña 
  password="Domy123$",     
  # Nombre de la base de datos donde se trabajará 
  database="portafolioexamen"   
)

# Creo un cursor, que es el objeto que permite ejecutar consultas sql en la base de datos
cursor = conexion.cursor()

# Inicio un bucle infinito para mostrar el menú continuamente hasta que el usuario cierre el programa
while True:
  # Muestro las opciones disponibles 
  print("Selecciona una opcion:")
  print("1.-Crear un registro")
  print("2.-Listar registros")
  print("3.-Actualiar registro")
  print("4.-Eliminar registro")

  # Pido al usuario que elija una opción del 1 al 4
  opcion = int(input("Elige tu opcion: "))
  
  if opcion == 1:
    # Solicito los datos que se insertarán en la tabla Piezas
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripción: ")
    fecha = input("Introduce la fecha: ")
    id_categoria = input("Introduce la categoria: ")

    # Ejecuto una consulta SQL INSERT para agregar un nuevo registro a la tabla
    cursor.execute('''
      INSERT INTO Piezas VALUES (
      NULL,
     -- El campo 'Identificador' será autoincremental
      "'''+titulo+'''",    
      -- Inserto el título introducido por el usuario
      "'''+descripcion+'''",  
      -- Inserto la descripción
      "'''+fecha+'''",       
      -- Inserto la fecha
      '''+id_categoria+'''    
      -- Inserto el ID de la categoría 
      );
    ''')
    # Confirmo los cambios en la base de datos
    conexion.commit()

  elif opcion == 2:
    # Ejecuto una consulta SELECT para obtener todos los registros de la tabla 'Piezas'
    cursor.execute('''
      SELECT * FROM Piezas;
    ''')

    # Guardo todos los resultados obtenidos en una lista
    filas = cursor.fetchall()

    # Recorro la lista e imprimo cada fila en pantalla
    for fila in filas:
      print(fila)

  elif opcion == 3:
    # Pido al usuario que indique el identificador del registro que quiere modificar
    identificador = input("Introduce el ID a actualizar: ")

    # Pido los nuevos datos con los que se reemplazarán los anteriores
    titulo = input("Introduce el titulo: ")
    descripcion = input("Introduce la descripcion: ")
    fecha = ("Introduce la fecha")
    id_categoria = input("Introduce la categoria: ")

    # Ejecuto una consulta SQL UPDATE para modificar el registro seleccionado
    cursor.execute('''
      UPDATE Piezas SET 
      titulo = "'''+titulo+'''",            
      -- Actualizo el título
      descripcion = "'''+descripcion+'''",  
      -- Actualizo la descripción
      fecha = "'''+fecha+'''",            
      -- Actualizo la fecha
      id_categoria = '''+id_categoria+'''   
      -- Actualizo la categoría
      WHERE Identificador = '''+identificador+''';  
      -- Indico qué registro modificar
    ''')
    # Guardo los cambios en la base de datos
    conexion.commit()

  elif opcion == 4:
    # Pido el identificador del registro que se desea eliminar
    identificador = input("Introduce el id a eliminar: ")

    # Ejecuto una consulta sql DELETE para eliminar el registro
    cursor.execute('''
      DELETE FROM Piezas
      WHERE Identificador = '''+identificador+'''
    ''')
    # Confirmo los cambios en la base de datos
    conexion.commit()
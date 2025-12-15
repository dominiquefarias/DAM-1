def hazdivision(dividendo,divisor):
 print("Entramos a la funcion")
 if isinstance (dividendo,(int, float, complex)) and isinstance(divisor, (int,float,complex)):
  print("parece que los parametros son numeros")
  if divisor != 0:
   print("parece que los puedo dividir")
  resultado = dividendo/divisor
  return resultado
 else:
  print("no puedo dividirporque el divisor es cero")
  resultado = 0
 else:
  print("los parametros no son numeros, pero voy a intentar convertirlos")
  try:
   print("intento convertir a numeros con exito")
 return resultado
 
print(hazdivision(4,"a"))

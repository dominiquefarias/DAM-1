import pickle

archivo = open("datos.bin","wb")
cadena = "Dominique"

pickle.dump(cadena,archivo)

archivo.close()

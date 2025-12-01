import pickle

archivo = open("datos.bin","b")
cadena = pickle.load(archivo)
    print(cadena)


archivo.close()

def leer_instrucciones(archivo):
    with open(archivo, 'r') as archivo:
        instrucciones = archivo.readlines() #Lee todas las lineas del archivo y las guarda en una lista
    return [instr.strip() for instr in instrucciones] #Elimina los espacios en blanco y salto de linea al inicio y al final de cada instrucción
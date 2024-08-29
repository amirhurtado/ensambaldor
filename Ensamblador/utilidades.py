def leer_instrucciones(archivo):
    with open(archivo, 'r') as archivo:
        instrucciones = archivo.readlines() #Lee todas las lineas del archivo y las guarda en una lista
    return [instr.strip() for instr in instrucciones] #Elimina los espacios en blanco y salto de linea al inicio y al final de cada instrucción

labels = dict()

def leer_labels(instrucciones):
    for i, instruccion in enumerate(instrucciones, 1):
        if ":" in instruccion:
            labels[instruccion.replace(":", "")] = i+1
            
def distancia_label(linea_label, linea):
    distance = linea_label - linea
    distancia_binaria = int(distance*32).to_bytes(length=4, signed=True)
    binario_normal = ''.join(format(byte, '08b') for byte in distancia_binaria)
    return binario_normal

def numero_a_binario(number: int | str, length=4):
    if isinstance(number, str):
        if "0x" in number:
            number = int(number, 16)
    binary = int(number).to_bytes(length=4, signed=True)
    normal_binary = ''.join(format(byte, '08b') for byte in binary)
    return normal_binary[-length:]
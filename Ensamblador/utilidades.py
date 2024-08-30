
equivalencias = {
    "zero": "x0",
    "ra": "x1",
    "sp": "x2",
    "gp": "x3",
    "tp": "x4",
    "t0": "x5",
    "t1": "x6",
    "t2": "x7",
    "s0": "x8",
    "fp": "x8",
    "s1": "x9",
    "a0": "x10",
    "a1": "x11",
    "a2": "x12",
    "a3": "x13",
    "a4": "x14",
    "a5": "x15",
    "a6": "x16",
    "a7": "x17",
    "s2": "x18",
    "s3": "x19",
    "s4": "x20",
    "s5": "x21",
    "s6": "x22",
    "s7": "x23",
    "s8": "x24",
    "s9": "x25",
    "s10": "x26",
    "s11": "x27",
    "t3": "x28",
    "t4": "x29",
    "t5": "x30",
    "t6": "x31",
}

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

def registros(reg: str):
    if not "x" in reg:
        x_reg = equivalencias.get(reg)
        if not x_reg:
            raise ValueError(f"Registro Invalido: '{reg}'")
        reg = x_reg
    num_reg = int(reg[1:])
    return numero_a_binario(num_reg, 5)

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
    i = 0
    for instruccion in instrucciones.copy():
        if instruccion == "":
            continue
        if ":" in instruccion:
            labels[instruccion.replace(":", "")] = i
            i -= 1
            instrucciones.remove(instruccion)
        i += 1
        
        
        
    
def equivalencia_pseudo_instructions(instrucciones):
    # Diccionario de equivalencias de pseudo-instrucciones a instrucciones reales
    equivalencias = {
        'nop': 'addi x0, x0, 0',
        'mv': 'addi {rd}, {rs}, 0',
        'not': 'xori {rd}, {rs}, -1',
        'neg': 'sub {rd}, x0, {rs}',
        'seqz': 'sltiu {rd}, {rs}, 1',
        'snez': 'sltu {rd}, x0, {rs}',
        'sltz': 'slt {rd}, {rs}, x0',
        'sgtz': 'slt {rd}, x0, {rs}',
        'beqz': 'beq {rs}, x0, {offset}',
        'bnez': 'bne {rs}, x0, {offset}',
        'blez': 'bge x0, {rs}, {offset}',
        'bgez': 'bge {rs}, x0, {offset}',
        'bltz': 'blt {rs}, x0, {offset}',
        'bgtz': 'blt x0, {rs}, {offset}',
        'bgt': 'blt {rt}, {rs}, {offset}',
        'ble': 'bge {rt}, {rs}, {offset}',
        'bgtu': 'bltu {rt}, {rs}, {offset}',
        'bleu': 'bgeu {rt}, {rs}, {offset}',
        'j': 'jal x0, {offset}',
        'jr': 'jalr x0, {rs}, 0',
        'ret': 'jalr x0, x1, 0'
    }

    # Lista para almacenar las instrucciones traducidas
    instrucciones_traducidas = []

    for instruccion in instrucciones:
        # Separar la instrucción y los registros/operandos
        partes = instruccion.split(' ', 1)
        nombre_instruccion = partes[0]
        
        # Si la instrucción tiene operandos
        if len(partes) > 1:
            operandos = partes[1]
        else:
            operandos = ''
        
        # Buscar la equivalencia en el diccionario
        if nombre_instruccion in equivalencias:
            instruccion_equivalente = equivalencias[nombre_instruccion]

            # Reemplazar los placeholders {rd}, {rs}, {rt} y {offset} según la instrucción
            if '{rd}' in instruccion_equivalente and '{rs}' in instruccion_equivalente:
                rd, rs = operandos.split(', ')
                instruccion_equivalente = instruccion_equivalente.format(rd=rd, rs=rs)
            elif '{rt}' in instruccion_equivalente and '{rs}' in instruccion_equivalente and '{offset}' in instruccion_equivalente:
                rs, rt, offset = operandos.split(', ')
                instruccion_equivalente = instruccion_equivalente.format(rs=rs, rt=rt, offset=offset)
            elif '{rs}' in instruccion_equivalente and '{offset}' in instruccion_equivalente:
                rs, offset = operandos.split(', ')
                instruccion_equivalente = instruccion_equivalente.format(rs=rs, offset=offset)
            elif '{offset}' in instruccion_equivalente:
                instruccion_equivalente = instruccion_equivalente.format(offset=operandos)
            elif '{rs}' in instruccion_equivalente:
                rs = operandos.strip()
                instruccion_equivalente = instruccion_equivalente.format(rs=rs)
           
            instrucciones_traducidas.append(instruccion_equivalente)
        else:
            # Si la instrucción no está en el diccionario, se deja tal cual
            instrucciones_traducidas.append(instruccion)
    
    return instrucciones_traducidas
            
            
def distancia_label(linea_label, linea):
    distance = linea_label - linea
    return numero_a_binario(distance*4, 32)


    

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


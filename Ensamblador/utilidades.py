from bitstring import BitArray, Bits
import re

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

pseudoinstrucciones = {
    "^nop\\s*$": "addi x0, x0, 0",
    "^mv\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)\\s*$": "addi {rd}, {rs}, 0",
    "^not\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "xori {rd}, {rs}, -1",
    "^neg\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "sub {rd}, x0, {rs}",
    "^negw\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "subw {rd}, x0, {rs}",
    "^seqz\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "sltiu {rd}, {rs}, 1",
    "^snez\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "sltu {rd}, x0, {rs}",
    "^sltz\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "slt {rd}, {rs}, x0",
    "^sgtz\\s+(?P<rd>\\w+),\\s*(?P<rs>\\w+)$": "slt {rd}, x0, {rs}",
    "^beqz\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "beq {rs}, x0, {offset}",
    "^bnez\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bne {rs}, x0, {offset}",
    "^blez\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bge x0, {rs}, {offset}",
    "^bgez\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bge {rs}, x0, {offset}",
    "^bltz\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "blt {rs}, x0, {offset}",
    "^bgtz\\s+(?P<rs>\\w+),\\s*(?P<offset>\\w+)\\s*$": "blt x0, {rs}, {offset}",
    "^bgt\\s+(?P<rs>\\w+),\\s*(?P<rt>\\w+),\\s*(?P<offset>\\w+)\\s*$": "blt {rt}, {rs}, {offset}",
    "^ble\\s+(?P<rs>\\w+),\\s*(?P<rt>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bge {rt}, {rs}, {offset}",
    "^bgtu\\s+(?P<rs>\\w+),\\s*(?P<rt>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bltu {rt}, {rs}, {offset}",
    "^bleu\\s+(?P<rs>\\w+),\\s*(?P<rt>\\w+),\\s*(?P<offset>\\w+)\\s*$": "bgeu {rt}, {rs}, {offset}",
    "^j\\s+(?P<offset>\\w+)\\s*$": "jal x0, {offset}",
    "^jal\\s+(?P<offset>\\w+)\\s*$": "jal x1, {offset}",
    "^jr\\s+(?P<rs>\\w+)\\s*$": "jalr x0, {rs}, 0",
    "^jalr\\s+(?P<rs>\\w+)\\s*$": "jalr x1, {rs}, 0",
    "^ret\\s*$": "jalr x0, x1, 0",
    "^call\\s*(?P<symbol>\\w+)\\s*$": ["auipc x1, {symbol1}", "jalr x1, x1, {symbol2}"],
    "^tail\\s*(?P<symbol>\\w+)\\s*$": ["auipc x6, {symbol1}", "jalr x0, x6, {symbol2}"],
    "^li\\s+(?P<rd>\\w+),\\s*(?P<symbol>[+-]?\\d+|0[xX][0-9a-fA-F]+)\\s*$": ["lui {rd}, {symbol1}", "addi {rd}, x0, {symbol2}"],
    "^l(?P<letter>[bhwd])\\s+(?P<rd>\\w+),\\s*(?P<symbol>[+-]?\\d+|0[xX][0-9a-fA-F]+)\\s*$": ["auipc {rd}, {symbol1}", "l{letter} {rd}, {symbol1}({rd})"],
    "^s(?P<letter>[bhwd])\\s+(?P<rd>\\w+),\\s*(?P<symbol>[+-]?\\d+|0[xX][0-9a-fA-F]+),\\s*(?P<rt>\\w+)\\s*$": ["auipc {rt}, {symbol1}", "s{letter} {rd}, {symbol2}({rt})"],
    "^la\\s+(?P<rd>\\w+),\\s*(?P<symbol>[+-]?\\d+|0[xX][0-9a-fA-F]+)\\s*$": ["auipc {rd}, {symbol1}", "addi {rd}, {rd}, {symbol2}"]
}

def leer_instrucciones(archivo):
    with open(archivo, 'r') as archivo:
        instrucciones = archivo.readlines() #Lee todas las lineas del archivo y las guarda en una lista
    return [instr.strip() for instr in instrucciones] #Elimina los espacios en blanco y salto de linea al inicio y al final de cada instrucción

labels = dict()


        
    
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
        'jal': 'jal x1, {offset}',
        'jr': 'jalr x0, {rs}, 0',
        'jalr': 'jalr x1, {rs}, 0',
        'ret': 'jalr x0, x1, 0'
    }

    # Lista para almacenar las instrucciones traducidas
    instrucciones_traducidas = []

    for instruccion in instrucciones:
        # Separar la instrucción y los registros/operandos
        partes = instruccion.split(' ', 1)
        nombre_instruccion = partes[0]
        operandos = partes[1] if len(partes) > 1 else ''

        # Manejar las pseudo-instrucciones 'jal' y 'jalr'
        if nombre_instruccion == 'jal':
            if ',' in operandos:
                instrucciones_traducidas.append(instruccion)  # Es una instrucción normal
            else:
                instruccion_equivalente = equivalencias['jal'].format(offset=operandos)
                instrucciones_traducidas.append(instruccion_equivalente)
        elif nombre_instruccion == 'jalr':
            if ',' in operandos:
                instrucciones_traducidas.append(instruccion)  # Es una instrucción normal
            else:
                instruccion_equivalente = equivalencias['jalr'].format(rs=operandos)
                instrucciones_traducidas.append(instruccion_equivalente)
            
        
        else:
            # Buscar la equivalencia en el diccionario
            if nombre_instruccion in equivalencias:
                instruccion_equivalente = equivalencias[nombre_instruccion]

                # Reemplazar los placeholders {rd}, {rs}, {rt} y {offset} según la instrucción
                if '{rt}' in instruccion_equivalente and '{rs}' in instruccion_equivalente and '{offset}' in instruccion_equivalente:
                    # Extraer los tres operandos: rt, rs y offset
                    rs, rt, offset = operandos.split(', ')
                    instruccion_equivalente = instruccion_equivalente.format(rt=rt, rs=rs, offset=offset)

                elif '{rd}' in instruccion_equivalente and '{rs}' in instruccion_equivalente:
                    rd, rs = operandos.split(', ')
                    instruccion_equivalente = instruccion_equivalente.format(rd=rd, rs=rs)

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
                
    print ("\nORIGINALES: ",   instrucciones)            
    print ("\nEQUIVALENCIAS: ", instrucciones_traducidas)
    

    return instrucciones_traducidas

def is_pseudo(instruction: str):
    
    for pattern, equivalence in pseudoinstrucciones.items():
        match = re.match(fr"{pattern}", instruction)
        if match:
            return match.groupdict(), equivalence
    return False, False
            
def distancia_label(linea_label: str | int, linea):
    if isinstance(linea_label, str):
        if linea_label.isnumeric():
            raise ValueError
    distance = linea_label - linea
    return numero_a_binario(distance*4, 32)

def bin_to_decimal(binary: str):
    bin = Bits(bin=binary)
    return bin.int

def cut_symbol(symbol: str, line=None):
    try:
        symbol = distancia_label(symbol,line)
    except ValueError:
        pass

    symbol = BitArray(uint=int(symbol), length=32)
    symbol1 = symbol << 12    
    new_symbol = {
        "symbol1": bin_to_decimal(symbol1.bin[:20]),
        "symbol2": bin_to_decimal(symbol.bin[-12:]),
    }
    return new_symbol

def numero_a_binario(number: int | str, length=4, signed=True):
    if isinstance(number, str):
        if "0x" in number:
            number = int(number, 16)
        else:
            number = int(number)
    if signed:
        if not puede_representarse_con_signo(number, length):
            raise ValueError(f"No se puede representar este numero ({number}) en {length} bits")
    else:
        if not se_puede_representar_sin_signo(number, length):
            raise ValueError(f"No se puede representar este numero ({number}) en {length} bits")
    binary = int(number).to_bytes(length=4, signed=signed)
    normal_binary = ''.join(format(byte, '08b') for byte in binary)
    return normal_binary[-length:]

def registros(reg: str):
    if not "x" in reg:
        x_reg = equivalencias.get(reg)
        if not x_reg:
            raise ValueError(f"Registro Invalido: '{reg}'")
        reg = x_reg
    num_reg = int(reg[1:])
    if num_reg > 31 or num_reg < 0:
        raise ValueError(f"Registro Invalido: '{reg}'")
        
    return numero_a_binario(num_reg, 5, signed=False)

def puede_representarse_con_signo(numero, bits):
    min_valor = -(2 ** (bits - 1))
    max_valor = 2 ** (bits - 1) - 1
    return min_valor <= numero <= max_valor

def se_puede_representar_sin_signo(num, bits):
    max_val = 2**bits - 1
    return 0 <= num <= max_val

def preparar_valores():
    with open("./values.txt", "r") as f:
        txt = f.read()
    list_ = txt.strip().split("\n")
    return list_

def crear_archivo(file: str, info: list):
    byte_data = bytearray()

    for binary_str in info:
        # Divide la cadena binaria en bloques de 8 bits
        for i in range(0, len(binary_str), 8):
            byte_chunk = binary_str[i:i+8]
            byte_data.append(int(byte_chunk, 2))

    
    with open(file, "wb") as f:
            f.write(byte_data)
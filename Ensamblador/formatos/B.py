def obtener_funct3_tipo_b(opcode):
    tabla_funct3 = {
        'beq': '000',
        'bne': '001',
        'blt': '100',
        'bge': '101',
        'bltu': '110',
        'bgeu': '111',
    }
    return tabla_funct3[opcode]
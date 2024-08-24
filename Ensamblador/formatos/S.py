def obtener_funct3_tipo_s(opcode):
    tabla_funct3 = {
        'sb': '000',
        'sh': '001',
        'sw': '010',
    }
    return tabla_funct3[opcode]
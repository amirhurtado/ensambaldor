def obtener_funct3_tipo_r(opcode):  #3 bits
    tabla_funct3 = {
        'add': '000',
        'sub': '000',
        'xor': '100',
        'or': '110',
        'and': '111',
        'sll': '001',
        'srl': '101',
        'sra': '101',
        'slt': '010',
        'sltu': '011',
    }
    return tabla_funct3[opcode]

def obtener_funct7_tipo_r(opcode): #7 bits
    tabla_funct7 = {
        'add': '0000000',
        'sub': '0100000',
        'xor': '0000000',
        'or': '0000000',
        'and': '0000000',
        'sll': '0000000',
        'srl': '0000000',
        'sra': '0100000',
        'slt': '0000000',
        'sltu': '0000000',
    }
    return tabla_funct7[opcode]
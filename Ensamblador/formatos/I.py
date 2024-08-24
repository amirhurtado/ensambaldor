def obtener_opcode_tipo_i(opcode):
    tabla_opcodes = {
        'addi': '0010011',
        'xori': '0010011',
        'ori': '0010011',
        'andi': '0010011',
        'slli': '0010011',
        'srli': '0010011',
        'srai': '0010011',
        'slti': '0010011',
        'sltiu': '0010011',
        'lb': '0000011',
        'lh': '0000011',
        'lw': '0000011',
        'lbu': '0000011',
        'lhu': '0000011',
        'jalr': '1100111',
        'ecall': '1110011',
        'ebreak': '1110011'
    }
    return tabla_opcodes[opcode]



def obtener_funct3_tipo_i(opcode):
    tabla_funct3 = {
        'addi': '000',
        'xori': '100',
        'ori': '110',
        'andi': '111',
        'slli': '001',
        'srli': '101',
        'srai': '101',
        'slti': '010',
        'sltiu': '011',
        'lb': '000',
        'lh': '001',
        'lw': '010',
        'lbu': '100',
        'lhu': '101',
        'jalr': '000',
        'ecall': '000',
        'ebreak': '000'
    }
    return tabla_funct3[opcode]
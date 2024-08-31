def obtener_opcode_tipo_u(op):
    tabla_opcode = {
        'lui': '0110111',
        'auipc': '0010111',
    }
    return tabla_opcode[op]
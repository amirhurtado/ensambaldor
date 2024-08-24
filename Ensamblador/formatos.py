def codificar_tipo_r(partes):
    opcode = "0110011"  # opcode para las instrucciones tipo R
    funct3 = obtener_funct3(partes[0])
    funct7 = obtener_funct7(partes[0])
    
    
    #partes [1] es el rd, [2] es el rs1, [3] es el rs2
    #[1:] para quitar el x
    #format(int, '05b') para convertir el entero a binario de 5 bits
    rd = format(int(partes[1][1:]), '05b')   
    rs1 = format(int(partes[2][1:]), '05b') 
    rs2 = format(int(partes[3][1:]), '05b')  
    
    return f"{funct7} {rs2} {rs1} {funct3} {rd} {opcode}"
    


def obtener_funct3(opcode):  #3 bits
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

def obtener_funct7(opcode): #7 bits
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
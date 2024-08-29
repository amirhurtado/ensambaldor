import sys

from .R import obtener_funct3_tipo_r, obtener_funct7_tipo_r
from .I import obtener_opcode_tipo_i, obtener_funct3_tipo_i
from .S import obtener_funct3_tipo_s
from .B import obtener_funct3_tipo_b
from utilidades import labels, distancia_label, numero_a_binario

def codificar_tipo_r(partes):
    opcode = "0110011"  # opcode para las instrucciones tipo R
    funct3 = obtener_funct3_tipo_r(partes[0])
    funct7 = obtener_funct7_tipo_r(partes[0])
    
    
    #partes [1] es el rd, [2] es el rs1, [3] es el rs2
    #[1:] para quitar el x
    #format(int, '05b') para convertir el entero a binario de 5 bits
    rd = format(int(partes[1][1:]), '05b')   
    rs1 = format(int(partes[2][1:]), '05b') 
    rs2 = format(int(partes[3][1:]), '05b')  
    
    return f"{funct7} {rs2} {rs1} {funct3} {rd} {opcode}"



def codificar_tipo_i(partes):
    opcode = obtener_opcode_tipo_i(partes[0])
    funct3 = obtener_funct3_tipo_i(partes[0])

    
     # Verificamos el formato de la instrucción
    if '(' in partes[2]:
        # Formato lb x1, 10(x2)
        inmediato, rs1 = partes[2].split('(') # separamos el inmediato y el rs1
        rs1 = rs1[:-1]  # Quitamos el paréntesis de cierre
    else:
        # Formato addi x1, x2, 10
        rs1 = partes[2]
        inmediato = partes[3]
    
    if "0x" in inmediato:
        inmediato = int(inmediato, 16)
    if( int(inmediato) < -2048 or int(inmediato) > 2047):
        sys.exit("Inmediato fuera de rango para tipo I")
    
    
    rd = format(int(partes[1][1:]), '05b') # Quitamos la x y convertimos el rd a binario
    rs1_bin = format(int(rs1[1:]), '05b') # Quitamos la x y convertimos el rs1 a binario
    # imm_bin = format(int(inmediato), '012b')  
    imm_bin = numero_a_binario(inmediato, 12) # Convierte el inmediato a 12 bits
    
    # Verificamos si la instrucción es de tipo srai o srli
    if(partes[0] == "srai"):
        imm_bin = imm_bin[:1] + "1" + imm_bin[2:]
    
    return f"{imm_bin} {rs1_bin} {funct3} {rd} {opcode}"
    
    
def codificar_tipo_s(partes):
    opcode = "0100011"  # opcode para las instrucciones tipo S
    funct3 = obtener_funct3_tipo_s(partes[0])
    
    rs1 = partes[1]
    inmediato, rs2 = partes[2].split('(') # separamos el inmediato y el rs1
    rs2 = rs2[:-1]  # Quitamos el paréntesis de cierre
    
    if( int(inmediato) < -2048 or int(inmediato) > 2047):
        sys.exit("Inmediato fuera de rango para tipo S")
    
    rs1 = format(int(rs1[1:]), '05b') # Quitamos la x y convertimos el rs1 a binario
    rs2 = format(int(rs2[1:]), '05b') # Quitamos la x y convertimos el rs2 a binario
    imm = format(int(inmediato), '012b') # Convierte el inmediato a 12 bits
    
    return f"{imm[0:7]} {rs2} {rs1} {funct3} {imm[7:12]} {opcode}"
    
    
def codificar_tipo_b(partes, i):
    opcode = "1100011"  # opcode para las instrucciones tipo B
    funct3 = obtener_funct3_tipo_b(partes[0])
    
    rs1 = format(int(partes[1][1:]), '05b') # Quitamos la x y convertimos el rs1 a binario
    rs2 = format(int(partes[2][1:]), '05b') # Quitamos la x y convertimos el rs2 a binario
    
    
    inmediato = partes[3]
    linea_label = labels.get(inmediato)
    distancia = distancia_label(linea_label, i)
    # if inmediato < 0:
    #     # Convertir a complemento a 2 para un número de 13 bits
    #     inmediato = (1 << 13) + inmediato  
    
    # if( int(inmediato) < -4096 or int(inmediato) > 4094):
    #     sys.exit("Inmediato fuera de rango para tipo B")

    # Convertir el inmediato a una cadena binaria de 13 bits
    # imm = format(inmediato, '013b')
    distancia = distancia[-12:]

    return f"{distancia[0]} {distancia[2:8]} {rs2} {rs1} {funct3} {distancia[8:12]} {distancia[1]} {opcode}"


def codificar_tipo_u(partes):
    opcode = "0110111"  # opcode para las instrucciones tipo U
    rd = format(int(partes[1][1:]), '05b') # Quitamos la x y convertimos el rd a binario
    inmediato = format(int(partes[2]), '032b')  # Convierte el inmediato a 20 bits
    
    
    return f"{inmediato[0:20]} {rd} {opcode}"
    
def codificar_tipo_j(partes, i):
    opcode = "1101111"
    rd = format(int(partes[1][1:]), '05b')
    inmediato = partes[2]
    linea_label = labels.get(inmediato)
    distancia = distancia_label(linea_label, i)
    distancia = distancia[-20:]
    
    return f"{distancia[0]}{distancia[10:]}{distancia[9]}{distancia[1:9]}{rd}{opcode}"
    
    
    
from formatos import codificar_tipo_r

def ensamblar_instrucciones(instrucciones): #Recibe una lista de instrucciones
    instrucciones_binarias = [] #Lista vacía para guardar las instrucciones binarias
    
    for instruccion in instrucciones:  #Recorre cada instrucción en la lista de instrucciones
        instruccion_binaria = ensamblar_instruccion(instruccion) #Va y ensambla la instrucción
        instrucciones_binarias.append(instruccion_binaria) #Agrega la instrucción binaria a la lista de instrucciones binarias
        
    return instrucciones_binarias #Devuelve la lista de instrucciones binarias

        
def ensamblar_instruccion(instruccion):
    partes = instruccion.replace(",", "").split() #Quita las comas y divide la instrucción en partes
    opcode = partes[0]
    
    if opcode in ['add', 'sub', 'xor', 'or', 'and', 'sll', 'srl', 'sra', 'slt', 'sltu']:  #Si la instrucción es de tipo R
        return codificar_tipo_r(partes)
    
    elif opcode in ['addi', 'xori', 'ori', 'andi', 'slli', 'srli', 'srai', 'slti', 'sltiu', 'lb', 'lh', 'lw', 'lbu', 'lhu', 'jalr', 'ecall', 'ebreak']:  #Si la instrucción es de tipo I
        return "Tipo I"
    
    elif opcode in ['sb', 'sh', 'sw']: #Si la instrucción es de tipo S
        return "Tipo S"
    
    elif opcode in ['beq', 'bne', 'blt', 'bge', 'bltu', 'bgeu']: #Si la instrucción es de tipo B
        return "Tipo B"
    
    elif opcode in ['lui', 'auipc']: #Si la instrucción es de tipo U
        return "Tipo U"
    
    elif opcode in ['jal']: #Si la instrucción es de tipo J
        return "Tipo J"
    
    else:
        return "Instrucción no válida"
    

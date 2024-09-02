from utilidades import leer_instrucciones, leer_labels, equivalencia_pseudo_instructions
from ensamblador import ensamblar_instrucciones

instrucciones: list

def main():
    archivo_entrada = './entrada.txt'  # Archivo de entrada
    global instrucciones
    instrucciones = leer_instrucciones(archivo_entrada) #Va y lee las instrucciones del archivo de entrada
    leer_labels(instrucciones)
    instrucciones = [inst for inst in instrucciones if not(":" in inst or inst == "")]
    instrucciones = equivalencia_pseudo_instructions(instrucciones)
    instrucciones_binarias = ensamblar_instrucciones(instrucciones) #Va y ensambla las instrucciones
    
    # for instruccion_binaria in instrucciones_binarias:
    #     print(instruccion_binaria)
    #     print(f"Len: {len(instruccion_binaria)}")
    
    return instrucciones_binarias
    

instrucciones_binarias = main()

# values = ['00000000000000010000000010000011', '11111111110000100001000110000011', '00000000100000110010001010000011', '00000000110001000100001110000011', '00000001000001010101010010000011', '11111110101101100000011000100011', '00000000110101110001110000100011', '00000000111110000010111000100011', '00000000001100010000000010110011', '01000000011000101000001000110011', '00000001001010001111100000110011', '00000001010110100110100110110011', '00000001100010111100101100110011', '00000000111111010001110010110011', '00000000100011100101110110110011', '00000001111111110010111010110011', '11111100001000001000000011100011', '11111100010000011001111011100011', '11111110011000101100110011100011', '00000000100000111101011001100011', '11111011000111111111001001101111', '00000000000001001000000011100111', '00000000000001100100001000010111', '00000000000011001000001010110111', '00000001000011100000111010010011']

values = ['00000000000000010000000010000011', '11111111110000100001000110000011', '00000000100000110010001010000011', '00000000110001000100001110000011', '00000001000001010101010010000011', '11111110101101100000011000100011', '00000000110101110001110000100011', '00000000111110000010111000100011', '00000000001100010000000010110011', '01000000011000101000001000110011', '00000001001010001111100000110011', '00000001010110100110100110110011', '00000001100010111100101100110011', '00000000111111010001110010110011', '00000000100011100101110110110011', '00000001111111110010111010110011', '11111100001000001000000011100011', '11111100010000011001111011100011', '11111110011000101100110011100011', '00000000100000111101011001100011', '11111011000111111111001001101111', '00000000000001001000000011100111', '00000000000001100100001000010111', '00000000000011001000001010110111', '00000001000011100000111010010011']

for value, binary, inst in zip(values, instrucciones_binarias, instrucciones):
    if value != binary:
        print(f"Diferent value: {binary}\nExpected:\t{value}\nInstruction: {inst}")
    else:
        print(f"Value: {binary}\nInstruction: {inst}")
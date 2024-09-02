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



for  binary, inst in zip( instrucciones_binarias, instrucciones):
    print(f"Diferent value: {binary}\nInstruction: {inst}")
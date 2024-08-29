from utilidades import leer_instrucciones, leer_labels
from ensamblador import ensamblar_instrucciones

def main():
    archivo_entrada = './entrada.txt'  # Archivo de entrada
    instrucciones = leer_instrucciones(archivo_entrada) #Va y lee las instrucciones del archivo de entrada
    leer_labels(instrucciones)
    instrucciones_binarias = ensamblar_instrucciones(instrucciones) #Va y ensambla las instrucciones
    
    for instruccion_binaria in instrucciones_binarias:
        print(instruccion_binaria)
        print(f"Len: {len(instruccion_binaria.replace(" ", ""))}")

main()
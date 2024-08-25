from utilidades import leer_instrucciones
from ensamblador import ensamblar_instrucciones

def main():
    archivo_entrada = 'Ensamblador\entrada.txt'  # Archivo de entrada
    instrucciones = leer_instrucciones(archivo_entrada)  #Va y lee las instrucciones del archivo de entrada
    instrucciones_binarias = ensamblar_instrucciones(instrucciones) #Va y ensambla las instrucciones
    
    for instruccion_binaria in instrucciones_binarias:
        print(instruccion_binaria)

main()